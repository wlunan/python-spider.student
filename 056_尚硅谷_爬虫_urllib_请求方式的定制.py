import urllib.request

url = "https://www.baidu.com"

# url的组成
# https://www.baidu.com/s?wd=lisa&ie=utf-8&tn=15007414_5_dg
# https 加了反爬的协议，我们需要对爬虫的请求进行浏览器伪装

# 协议 http/https
# 主机 www.baidu.com
# 端口号 80/443
# 路径 s
# 参数   wd = lisa
# 锚点 #

# 常见端口号
# http 80   https 443   mysql 3306  Oracle 1521     redis 6379  MongoDB 27017

# 将伪装信息封装成header字典
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

request = urllib.request.Request(url = url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

print(content)

