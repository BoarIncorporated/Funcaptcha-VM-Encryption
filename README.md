You need to AES encrypt the payload first just like you did for previous version and then rsa encrypt it
### **Currently it's not possible to decrypt the BDA afterwards, you can obviously see it using breakpoints but it's pretty annoying, ~~so I made an endpoint on my site that allows you to view your 4.0.5 BDA without any hassle, you can find it [here](https://fingerprinting.my/my-fingerprint)~~**
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

## Known site-keys on 4.x.x

| Version | Site Key | Site Name | RSA Key |
|---------|----------|-----------|----------|
| 4.0.7 | `717C7D7F-8ED2-4587-AF41-E7E34907A6FB` | Badoo - Bumble: phone - web - login | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `73C53A42-FEEA-4097-8B08-F9F3E8B143CE` | Badoo - Bumble: social (Facebook / Apple) - web - login | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `EEE19E8E-9269-2EBD-7AD5-EE149237BA46` | LevelBlue | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `7D76E2A2-89F4-4CD7-AB0E-416683BF595D` | Payoneer: Development | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `EE844FC3-499D-4A4D-A643-D7400F0FD4DE` | Payoneer: Production | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `FE9DC8DA-5E83-495F-A762-582267EEACDE` | Snapchat: login (development) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `07EAB4B8-2D80-4234-B897-A2CD1F194866` | Snapchat: login (production) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `152E1D0C-D805-4060-A111-6AC82CA6821B` | Snapchat: signup (development) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `EA4B65CB-594A-438E-B4B5-D0DBA28C9334` | Snapchat: signup (production) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `C383A903-0809-41A2-A832-5F7ACC690EA6` | Snapchat: wwwLogin (development) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `D99D7D11-158A-408C-A6C5-29F2B60EFADE` | Snapchat: wwwLogin (production) | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `C07CAFBC-F76F-4DFD-ABFA-A6B78ADC1F29` | Twitter: Contact - https://help.x.com | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `BF5FA6C8-9668-4AF9-AFA2-E362F56E5B71` | Twitter: arkose_challenge_lo_web_notification_dev | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `6A2FD110-7C1A-47CD-82EE-D01FFB4810D7` | Twitter: arkose_challenge_lo_web_notification_mobile_prod | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `50706BFE-942C-4EEC-B9AD-03F7CD268FB1` | Twitter: arkose_challenge_lo_web_notification_prod | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `2F4F0B28-BC94-4271-8AD7-A51662E3C91C` | Twitter: arkose_challenge_login_web_prod | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `560C66A3-C8EB-4D11-BE53-A8232734AA62` | Twitter: arkose_challenge_open_app_dev | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `006B5E87-7497-403E-9E0C-8FFBAAC6FA67` | Twitter: arkose_challenge_signup_mobile_dev | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `DF58DD3B-DFCC-4502-91FA-EDC0DC385CFF` | Twitter: arkose_challenge_signup_web_dev | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `6627C16B-DA60-47A5-85F7-CFF23BD2BE69` | Twitter: arkose_challenge_transparent_signup_dev | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `4CB8C8B0-40FF-439C-9D0D-9A389ADA18CB` | Twitter: arkose_challenge_transparent_signup_prod | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `E3EFEFBF-8DE4-42ED-9E7F-92F35B1FD3CF` | UNKNOWN SITE | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `6375512B-BEE6-458C-87B0-3E4DEED2C5E3` | Uber: Development | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.7 | `3C5073B0-3106-423D-8D6B-81FE82CF5C2C` | Wells Fargo: Development | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0i/vlOMMlP2xds9jL+0e3yBrFxpfOvOMf4BHdzmz9ntkZQXk450leaP56iaaxTMvj2QoRO2Yz1ja7Ll7nrbPjZ/8oPx280k56ywivU9GzUCLjd3y5G8f2fsukncPVTwJ8YVbYhywEz7LyevDGOgLznuoMPF+Xp4NIIUFvbLb6yvWHu1ibCLHlRrFps+puFDMUE8a/qHMk3mo4VIoSjqtiRfiGpqF0qhKho/4mxK6U8xlqImGVp6840NFQybsQXZMGZ1VgE1iZitiVLlILTXFHa2ggEPmzKHqOI5E5qI1lT4W61S5uvKhG4PLM+/R5OlCH+kQLgrpODhFWmHIYptlewIDAQAB` |
| 4.0.8 | `CC30DB96-0C88-4DEB-86E5-6601927ACBB4` | Roblox: GENERIC_CHALLENGE | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `63E4117F-E727-42B4-6DAA-C8448E9B137F` | Roblox: SUPPORT_REQUEST | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `1B154715-ACB4-2706-19ED-0DC7E3F7D855` | Roblox: WEB_GAMECARD_REDEMPTION | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `476068BF-9607-4799-B53D-966BE98E2B81` | Roblox: WEB_RESET_PASSWORD | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F` | Roblox: WEB_SIGNUP | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `4D297134-67EC-B943-E0E9-79E2E0D9F8DB` | Singapore Airlines | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `DE0B0BB7-1EE4-4D70-1853-31B835D4506B` | UNKNOWN SITE | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `30000F36-CADF-490C-929A-C6A7DD8B33C4` | Uber: Production | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `1BE2475D-0F5A-4188-B20A-A9943639840C` | Uber: unknown | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |
| 4.0.8 | `9B8ED233-984B-4DE5-A7B6-3A370D9FF48B` | Wells Fargo: Production | `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwpmnjHirsn/oniK7GYh6HYqNbJdlUjK0WEgUZE/Jm+rru41d2zNDUlqb3M6IKJxRyRGQBf0SKpIWu789boBDd3CrSyK4DD/hJxXN9junJehtOUa5eXh+m+jKdawInF17DspzTFzzbi9SfP2o9kcRA3kzRdrTw6I1yPjMUzrV4Vn6J2smDDgPVxCZvnXxrjEWl81kPlNQpD+0jmVs/7p2RPU4L/tYFRyR7deZO7tCOJu/HT8qnZ4U285aFrDiNYD88CXt1HLSa0X2In135MLHE/0umbOYVPAxDqvjP3bwx3bcF+L9GCi5P3729XoYDMtiWjL7Mi2XxHI4QZHs69n/6wIDAQAB` |

**Total keys:** 34

## Credits
- [@tylerdevx](https://github.com/tylerdevx/) for the vm dump
