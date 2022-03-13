
# 获取https://www.baidu.com/s?wd=王嘉尔的网页源码

import urllib.request

url = "https://www.baidu.com/s?wd="

# 请求对象的定制解决反爬的一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

# 将汉字转换为unicode编码的格式
name = urllib.parse.quote("李白")

url = url+name

request = urllib.request.Request(url=url,headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")
print(content)