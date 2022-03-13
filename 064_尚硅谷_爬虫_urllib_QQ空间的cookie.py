import urllib.request

url = "https://weibo.com/u/6509193378"

headers = {
    # ':authority': ' weibo.com',
    # ':method': ' GET',
    # ':path': ' /ajax/message/whitelist',
    # ':scheme': ' https',
    # 'accept': ' application/json, text/plain, */*',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'XSRF-TOKEN=zZ8ecpiL4bdGIRpwmkOga7iA; login_sid_t=f92b72afc3b03ecbf2827ef67f6ef165; cross_origin_proto=SSL; wb_view_log=1549*8721.2395833730697632; _s_tentry=weibo.com; Apache=8580171705407.891.1646485834807; SINAGLOBAL=8580171705407.891.1646485834807; ULV=1646485834823:1:1:1:8580171705407.891.1646485834807:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhNQbNYopvQVz1PYfsDmV1s5JpX5o275NHD95QcSK54eK.0e0MRWs4DqcjMi--Xi-zRi-iWi--Xi-iWiKncHbH8SCHWxF-4S7tt; SSOLoginState=1646485898; SUB=_2A25PJxHbDeRhGeBL61sQ-S3PzDSIHXVsVQQTrDV8PUNbmtB-LVWikW9NR0bRPlhkG8TED3Z2TAhN7JZaMEJ-ANuL; ALF=1678021897; WBPSESS=naGefjaT0JHKE8gx2EkcrIk1c5XidQuRAHVT_pyLBliMHarbgz1q1koVYWYQ3usbEjKpXagTrYo_heF5PKbOn6u5TvflhPdVdar1S1bLdTj3D6lb4W6oBkKfkdObDvD9fPDCP5THhTjzhw1-4uRDnQ==',
    'dnt': ' 1',
    'referer': 'https://weibo.com/',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'traceparent': ' 00-044e2db2d9d05e931407384223796d58-377ba0ff0edf33a3-00',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'x-requested-with': ' XMLHttpRequest',
    'x-xsrf-token': ' zZ8ecpiL4bdGIRpwmkOga7iA',
}
# 伪装请求
request = urllib.request.Request(url=url,headers = headers)
# 获取响应
response = urllib.request.urlopen(request)
# 写入数据 解码
content = response.read().decode("utf8")
with open("html/qq.html", "w", encoding="utf8") as fp:
    fp.write(content)