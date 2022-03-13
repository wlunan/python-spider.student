import json
import jsonpath
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1647162812761_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'accept-language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'cookie':' _samesite_flag_=true; cookie2=1fa8b7cf096b69f74fcf38d1ff200f45; t=1ee9175b75bbac166c2e0545faf8ce12; _tb_token_=ee43874313f48; v=0; cna=naO0GgFz1gsCAXWf3xgI8gmy; l=eBPAzGRqLrRtNu0MBO5BPurza77TmQAb8kPzaNbMiInca61CtFT7LNCnAO3XSdtfgtfFhetPi3JuJRh9SdUpbgiMW_N-1NKcvYv6-; tfstk=cJ-NB7YEZcnaBbjjyGsq1x9EUb_Oa91GOoXPSFesiQMUqvbGasxLM9Da5tX3LSbG.; isg=BAUFcrMpy6nGmu_1woQjsmq4FEE_wrlU_RNZ8wdoyjxLniQQzxG-JK1wqEJoxdEM',
'dnt':' 1',
'referer': 'https://dianying.taobao.com/',
'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
'sec-ch-ua-mobile':' ?0',
'sec-ch-ua-platform':' "Windows"',
'sec-fetch-dest':' empty',
'sec-fetch-mode':' cors',
'sec-fetch-site':' same-origin',
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
'x-requested-with':' XMLHttpRequest',
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 获取响应数据
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf8')

# 对获取的json数据进行切割
content = content.split('(')[1].split(')')[0]

# 将数据保存到本地
with open('074_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'w', encoding='utf8') as fp:
    fp.write(content)

# 解析JSON数据
obj = json.load(open('074_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'r', encoding='utf8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

# 写入城市总数
desc = '可以使用淘票票的城市总数'+str(len(city_list))
with open('074_city_list.txt', 'a', encoding='utf8') as fp:
    fp.write(desc)
# 将读取到的城市列表写到本地
with open('074_city_list.txt','a', encoding='utf8') as fp:
    for i in range(len(city_list)):
        fp.write('\n')
        fp.write(city_list[i])
