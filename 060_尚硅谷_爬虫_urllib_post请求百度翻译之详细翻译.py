import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    # 'Accept':' */*',
# 'Accept-Encoding':' gzip, deflate, br',
# 'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# 'Connection':' keep-alive',
# 'Content-Length':' 134',
# 'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'PSTM=1630224261; __yjs_duid=1_8a90c11bc0c9535a0929f80ced264c731630224266652; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BAIDUID=BC9A721F4BD422A003868853E7327D9A:FG=1; BIDUPSID=5AF8F87ED46303785E12515E8B7FEAA1; APPGUIDE_10_0_2=1; BDUSS=BESU9DOC1sZ2NDbHE3cHFqWU44a1VmRzBQSjhOWFJwN3Y1VTBHS25kN3dYeGRpRVFBQUFBJCQAAAAAAAAAAAEAAAAB2iFt4pi65bCP55m94pi6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDS72Hw0u9hbl; BDUSS_BFESS=BESU9DOC1sZ2NDbHE3cHFqWU44a1VmRzBQSjhOWFJwN3Y1VTBHS25kN3dYeGRpRVFBQUFBJCQAAAAAAAAAAAEAAAAB2iFt4pi65bCP55m94pi6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDS72Hw0u9hbl; BAIDUID_BFESS=BC9A721F4BD422A003868853E7327D9A:FG=1; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=5xkstq0m9et&ss=l06s3a2m&sl=1&tt=1at&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2u1&ul=1jdv&hd=1jel"; delPer=0; PSINO=1; BDRCVFR[OEHfjv-pq1f]=I67x6TjHwwYf0; BDRCVFR[77Ms7oRaB-6]=I67x6TjHwwYf0; H_PS_PSSID=31254_26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ZD_ENTRY=baidu; BA_HECTOR=85810k2lah04al8gde1h1rphr0r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1646124782,1646126213,1646126830,1646126907; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1646126907',
# 'DNT':' 1',
# 'Host':' fanyi.baidu.com',
# 'Origin': 'https://fanyi.baidu.com',
# 'Referer': 'https://fanyi.baidu.com/',
# 'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
# 'sec-ch-ua-mobile':' ?0',
# 'sec-ch-ua-platform':' "Windows"',
# 'Sec-Fetch-Dest':' empty',
# 'Sec-Fetch-Mode':' cors',
# 'Sec-Fetch-Site':' same-origin',
# 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
# 'X-Requested-With':' XMLHttpRequest',
}

data = {
'from':' en',
'to':' zh',
'query':' like',
'transtype':' realtime',
'simple_means_flag':' 3',
'sign':' 272503.52038',
'token':' 9b36cb97492bfeecfc558219f44ab397',
'domain':' common',
}

# post请求必须进行编码，并且使用encode方法
data = urllib.parse.urlencode(data).encode("utf8")

# 请求对象的定制
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

import json
content = json.loads(content)
print(content)