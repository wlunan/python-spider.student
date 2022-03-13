
url = "http://fanyi.baidu.com/basetrans"

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        }


# data = {
#     "from": "en",
#     "to": "zh",
#     "query": "spider",
# "transtype": "realtime",
# "simple_means_flag": "3",
# "sign": "63766.268839",
# "token": "89704d5ef37cea13262552ef3955a7fc",
# "domain": "common"
# }

data = {
    "query": "你好世界",
    "from": "zh",
    "to": "en",

}

import urllib.request
import urllib.parse

# post请求的参数必须进行编码

data = urllib.parse.urlencode(data).encode("utf8")

# post请求的参数是放在对象定制的参数中 而且要进行字节编码
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟向浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

import json
content = json.loads(content)
print(content)