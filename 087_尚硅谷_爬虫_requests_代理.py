import requests

url = 'https://www.baidu.com/s?'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}

data = {
    'wd':'ip'
}

proxy = {
    'http':'185.103.168.72:8080'
}
response = requests.get(url=url,headers=headers,params=data,proxies=proxy)

content = response.text

with open('087ip.html','w',encoding='utf8') as fp:
    fp.write(content)