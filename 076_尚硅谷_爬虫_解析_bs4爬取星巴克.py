import urllib.request
from bs4 import BeautifulSoup

# 请求对象伪装
url = 'https://www.starbucks.com.cn/menu/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

request = urllib.request.Request(url=url,headers=headers)

# 获取响应数据
response = urllib.request.urlopen(request)

# 获取数据
content = response.read().decode('utf8')

soup = BeautifulSoup(content,'lxml')
# //ul[@class="grid padded-3 product"]//strong

name_list = soup.select('ul[class="grid padded-3 product"] strong')

with open('./starStuck/name.txt', 'a', encoding='utf8') as fp:
    fp.write('星巴克产品数量'+str(len(name_list)))
    fp.write('\n')

for name in name_list:
    with open('./starStuck/name.txt','a',encoding='utf8') as fp:
        fp.write(name.string)
        fp.write('\n')
