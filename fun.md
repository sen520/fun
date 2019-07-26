##### node 定时任务

```js
var schedule = require('node-schedule');

function scheduleCronstyle(){
  // 秒 分 时 日 月 年 周
  schedule.scheduleJob('30 * * * * *', function(){
    console.log('scheduleCronstyle:' + new Date());
  });
}

scheduleCronstyle();
```

##### zoom加密规则

```js
const base64JS = require('js-base64');
const hmacSha256 = require('crypto-js/hmac-sha256');
const encBase64 = require('crypto-js/enc-base64');

function generateSignature(data) {
  let signature = '';
  const ts = new Date().getTime();
  const msg = base64JS.Base64.encode(data.apiKey + data.meetingNumber + ts + data.role);
  const hash = hmacSha256(msg, data.apiSecret);
  signature = base64JS.Base64.encodeURI(`${data.apiKey}.${data.meetingNumber}.${ts}.${data.role}.${encBase64.stringify(hash)}`);
  return signature;
}

const data = {apiKey: "" ,
  apiSecret: "",
  meetingNumber: 888,
  role: 0};

console.log(generateSignature(data));
```

