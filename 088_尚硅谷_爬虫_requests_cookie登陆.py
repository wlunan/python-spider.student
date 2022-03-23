# 需求：通过登陆，进入古诗词网主界面

# 通过登陆接口发现，登陆需要的参数有很多
# _VIEWSTATE: qxdJHTbou0yV3t8aMl9qnW+nUVZXxjEmnwUKTwD49RIfwMf15c397jWNQB3aMySG1sCJ6MUuAberkhO2lpzJAkV8yx41iJQhKjBjImBUSAVEIP6M2ASoFYoYvlw=
# _VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 2840111670@qq.com
# pwd: sdassdad
# code: 6tqr
# denglu: 登录

# 通过观察发现_VIEWSTATE和_VIEWSTATEGENERATOR是可变的值

# 难点：
# 1._VIEWSTATE和_VIEWSTATEGENERATOR  存在于界面源码的隐藏域
# 通过解析页面中的源码可以获取到
# 2.验证码


import requests

# 获取登录界面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}

response = requests.get(url = url,headers = headers)

content = response.text

# 解析界面源码，获取参数
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')
# 获取_VIEWSTATE和_VIEWSTATEGENERATOR  id选择器   返回一个列表
viewstart = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstartgenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')


# 获取验证码图片 在控制台输入验证码内容即可完成验证
code_url = 'https://so.gushiwen.cn/RandCode.ashx'

# 有坑
# 下载验证码到本地
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')

session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 注意此时用获取二进制数据，因为下载的是图片
content_code = response_code.content
# wb方式就是以二进制方式写入文件
with open('code.jpg','wb') as fp:
        fp.write(content_code)
code_name = input('请输入验证码：')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
'__VIEWSTATE': viewstart,
'__VIEWSTATEGENERATOR': viewstartgenerator,
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': '2840111670@qq.com',
'pwd': '2840670.',
'code': code_name,
'denglu': '登录'
}
# 确保获取验证码和登录是同一个请求
response_post = session.post(url=url_post,headers=headers,data=data_post)

content = response_post.text
# 将登录后的界面下载到本地
with open('login.html','w',encoding='utf8') as fp:
        fp.write(content)

# 登录失败，验证码错误，因为获取验证码的请求和登录的请求不是同一个请求，登录请求的验证码不是一开始获取到的验证码

