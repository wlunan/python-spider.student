import requests

url = 'https://www.baidu.com'

response = requests.get(url=url)


# 一个类型六个属性
# Response类型
# print(type(response))

# 设置响应的编码格式，解决获取网页源码出现中文乱码问题
response.encoding = 'utf8'

# 以字符串方式获取网页源代码
# print(response.text)

# 返回网页的url
# print(response.url)

# 返回的是二进制数据
# print(response.content)

# 返回响应的状态码
# print(response.status_code)

# 返回响应头
# print(response.headers)
