import requests

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
# 'Accept':' application/json, text/javascript, */*; q=0.01',
# 'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# 'Connection':' keep-alive',
# 'Content-Length':' 237',
# 'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'OUTFOX_SEARCH_USER_ID=-27795306@10.110.96.157; JSESSIONID=aaaWP0SjG8C5rbCr2dx_x; OUTFOX_SEARCH_USER_ID_NCOO=567549300.1885794; fanyi-ad-id=305110; fanyi-ad-closed=0; ___rl__test__cookies=1647506852159',
# 'DNT':' 1',
# 'Host':' fanyi.youdao.com',
# 'Origin: https':'//fanyi.youdao.com',
# 'Referer: https':'//fanyi.youdao.com/',
# 'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
# 'sec-ch-ua-mobile':' ?0',
# 'sec-ch-ua-platform':' "Windows"',
# 'Sec-Fetch-Dest':' empty',
# 'Sec-Fetch-Mode':' cors',
# 'Sec-Fetch-Site':' same-origin',
# 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
# 'X-Requested-With':' XMLHttpRequest',
}

data = {
'i':' eye',
'from':' AUTO',
'to':' AUTO',
'smartresult':' dict',
'client':' fanyideskweb',
'salt':' 16475068521708',
'sign':' fdb069ee7e3cd0e02f608cce83538056',
'lts':' 1647506852170',
'bv':' cdd63870d07eb5030b9324cc7f7de35b',
'doctype':' json',
'version':' 2.1',
'keyfrom':' fanyi.web',
'action':' FY_BY_REALTlME',
}

# post请求
response = requests.post(url=url, headers=headers, data=data)

content = response.text

import json

# content = json.loads(content)
print(content)
