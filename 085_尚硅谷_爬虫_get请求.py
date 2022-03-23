import requests

# urllib
# 1.一个类型六个方法
# 2.get请求
# 3.post请求  百度翻译
# 4.ajax的get请求
# 5.ajax的post请求
# 6.cookie登录    微博
# 7.代理

# requests
# 1.一个类型六个属性
# 2.get请求
# 3.post请求
# 4.代理
# 5.cookie  验证码

url = 'https://www.baidu.com/s?'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}
proxy = {
    'http':'14.215.212.37:9168'
}
data = {
    'wd':'ip'
}
# url请求资源路径
# params参数
# kwargs字典
response = requests.get(url=url,headers=headers,params=data,proxies=proxy)


content = response.text
with open('085.html','w',encoding='utf8') as fp:
    fp.write(content)
# print(content)