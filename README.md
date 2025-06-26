You need to AES encrypt the payload first just like you did for previous version and then rsa encrypt it
### **Currently it's not possible to decrypt the BDA afterwards, you can obviously see it using breakpoints but it's pretty annoying, so I made an endpoint on my site that allows you to view your 4.0.5 BDA without any hassle, you can find it [here](https://fingerprinting.my/my-fingerprint)**
> [!NOTE]
> You will still have to set breakpoints to get site-specifc presets

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

There are also some new mechanisms to edit the bda values dynamically, for example you can see that `screen_pixel_depth` which is typically `24` on chrome is now `72`, which is `24 * 3`
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

## New values
- `ark-build-id`: new header, you can find the value its set to in api.js, this header is only used in the /gt2/ request

## Updated values
- `navigator_permissions_hash` which was previously renamed in 3.5.0, has been reverted to its original name
- `bda` -> `c`, again this is for the /gt2/ request
- `data[blob]` used to not be set at all in the payload when there was no blob, now if there is no blob the value in tha payload is set to `data[blob]: "undefined"`

## Known site-keys on 4.0.5
- 3C5073B0-3106-423D-8D6B-81FE82CF5C2C -> Wells Fargo
- C07CAFBC-F76F-4DFD-ABFA-A6B78ADC1F29 -> help.x.com
- 2F4F0B28-BC94-4271-8AD7-A51662E3C91C -> X login
- 7D76E2A2-89F4-4CD7-AB0E-416683BF595D -> Payoneer dev
- EE844FC3-499D-4A4D-A643-D7400F0FD4DE -> Payoneer prod
- 73C53A42-FEEA-4097-8B08-F9F3E8B143CE -> Bumble
- 717C7D7F-8ED2-4587-AF41-E7E34907A6FB -> Bumble phone
- E3EFEFBF-8DE4-42ED-9E7F-92F35B1FD3CF -> Demo key

## Credits
- [@tylerdevx](https://github.com/tylerdevx/) for the vm dump
- [@Fr0st3h](https://github.com/Fr0st3h/BDALogger) for the bda logger hosted on my site
