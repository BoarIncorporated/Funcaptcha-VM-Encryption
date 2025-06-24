import base64
from typing import Optional
from os import urandom

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, asymmetric, hashes


DEFAULT_PUBKEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzjl0t5bLoeEA1f3uTVUEfEfOoSH3hCfFEu6dFvrxeZML84tv2d5r3x5KEhc7eJfFUGHyA/W5cAS8gGKzIrA433mWP5m4gZUwMIL8wSuusqNMcohIVObwWn8imhS+Bt0yH8q0q/Zz1WyACxbkrGhQqzllqc0gHbZkjNfQC2h5Si4jIYJXBF5X6asM07WJmeZynXTCdrJJUnzDZNERmbpkmsvkpoBrLnZ2XMY1bR9o+X4PFIBDpF+LdYXPuvAby/iIVfFzlVh/pX1n9ZIdSgFplM5+2TL+rlmPiC26ekxIsUBv/yHInwPMr6xpe0XolOvPu8D3xzpIIVX9BAJvyU/H/QIDAQAB"


def b64encode(content: bytes) -> str:
    return base64.b64encode(content).decode('utf-8')


def rsa_encrypt(content: str, pubkey: Optional[str] = None) -> str:
    pubkey = pubkey or DEFAULT_PUBKEY
    key = urandom(32)
    iv = urandom(12)
    encoded_fingerprint = content.encode('utf-8')

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(encoded_fingerprint) + encryptor.finalize()
    tag = encryptor.tag

    raw_aes_key = key

    pki_key_der = base64.b64decode(pubkey)
    public_key = serialization.load_der_public_key(pki_key_der, backend=default_backend())

    encrypted_key = public_key.encrypt(
        raw_aes_key,
        asymmetric.padding.OAEP(
            mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    iv_encode = b64encode(iv)
    tag_encode = b64encode(tag)
    encrypted_key_encode = b64encode(encrypted_key)
    encrypted_body_encode = b64encode(ciphertext)

    return f"{iv_encode}{tag_encode}{encrypted_key_encode}{encrypted_body_encode}"
