import urllib.request

url = "http://plutos.top"

# 模拟浏览器发送请求
response = urllib.request.urlopen(url)
# 一个类型六个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read(5)
# print(content)

# readline一次读取一行
# content = response.readline()
# print(content)

# readlines一次读取多行
# content = response.readlines()
# print(content)

# getcode返回状态码 200证明逻辑没有问题
# print(response.getcode())

# geturl返回的是url地址
# print(response.geturl())

# getheaders返回头信息
# print(response.getheaders())