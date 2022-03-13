import urllib.request
import urllib.parse

baseUrl = "https://www.baidu.com/s?"

data = {
    "wd":"周杰伦",
    "sex":"男",
    "location":"中国台湾"
}

newData = urllib.parse.urlencode(data)

# 请求资源路径

url = baseUrl+newData
print(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

print(content)