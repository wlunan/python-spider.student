import urllib.request

url = 'https://www.baidu.com/'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}

# 请求对象的定制
request = urllib.request.Request(url = url,headers=headers)

# 模拟浏览器啊发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf8')
# print(content)

from lxml import etree

# 解析网页文件
tree = etree.HTML(content)
# 获取想要的数据 xpath返回值是列表数据
result = tree.xpath('//div/a[@class="toindex"]/text()')[0]

print(result)