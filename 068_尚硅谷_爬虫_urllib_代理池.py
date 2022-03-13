import random
import urllib.request

url = "https://www.baidu.com/s?wd=ip"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers = headers)

# 制作代理池
proxiesPool = [
    {'http':'42.194.146.199:1080'},
    {'http':'122.9.101.6:8888'},
    {'http':'101.34.214.152:8001'}
]

proxies = random.choice(proxiesPool)

# 1.获取handler对象
handler = urllib.request.ProxyHandler(proxies)

# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用open方法
response = opener.open(request)

content = response.read().decode('utf8')

with open('html/daili.html', 'w', encoding='utf8') as fp:
    fp.write(content)