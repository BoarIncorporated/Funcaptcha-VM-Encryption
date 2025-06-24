You need to AES encrypt the payload first just like you did for previous version and then rsa encrypt it
### **Currently as BDA is encrypted using RSA, it's not possible to decrypt it afterwards, you can obviously see it using breakpoints but it's pretty annoying, so I made an endpoint on my site that allows you to view your 4.0.5 bda without any hassle, you can find it [here](https://fingerprinting.my/my-fingerprint)**

## New BDA values
- vsadsa
```javascript
return window.navigation.entries().length
```
- basfas
```javascript
const p = window?.performance;
const m = p?.memory;
const limit = m?.jsHeapSizeLimit;

if (!p) return [1, null];
if (!m) return [2, null];
if (!limit) return [3, null];

return [0, limit];
```
- lfasdgs
```javascript
return window.arkl.cbid
```

There are also some new mechanisms to edit the bda values dynamically, for example you can see that for example `screen_pixel_depth` which is typically `24` on chrome is now `72`, which is `24 * 3`
this is caused by code that looks something like this:

```javascript
let enhanced_fp = bda[4]?.value;

if (enhanced_fp[26]?.value) {
    enhanced_fp[26] = {
        key: enhanced_fp[26].key,
        value: enhanced_fp[26].value * 3
    };
}
```

this also happens for `network_info_rtt_type` on something like this:

```javascript
let enhanced_fp = bda[4]?.value;

if (enhanced_fp?.[25] && enhanced_fp?.[1]?.value && enhanced_fp?.[18]?.value) {
    const webgl_extensions_hash = enhanced_fp[1].value;
    const webgl_hash_webgl = enhanced_fp[18].value;
    enhanced_fp[25].value = {
        key: enhanced_fp[25].key,
        value:
            typeof webgl_extensions_hash === "string" && webgl_extensions_hash.length > 12 &&
            typeof webgl_hash_webgl === "string" && webgl_hash_webgl.length > 12
                ? webgl_extensions_hash.slice(0, 3) + webgl_hash_webgl.slice(0, 3)
                : "abcdef"
    };
}
```

## Known site-keys on 4.0.5
- 3C5073B0-3106-423D-8D6B-81FE82CF5C2C
- C07CAFBC-F76F-4DFD-ABFA-A6B78ADC1F29
- 2F4F0B28-BC94-4271-8AD7-A51662E3C91C
- 7D76E2A2-89F4-4CD7-AB0E-416683BF595D
- EE844FC3-499D-4A4D-A643-D7400F0FD4DE
- 73C53A42-FEEA-4097-8B08-F9F3E8B143CE
- 717C7D7F-8ED2-4587-AF41-E7E34907A6FB
- E3EFEFBF-8DE4-42ED-9E7F-92F35B1FD3CF

## Credits
- [@tylerdevx](https://github.com/tylerdevx/) for the vm dump
