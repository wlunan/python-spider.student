# 1.导入selenium
from selenium import webdriver

# 2.创建谷歌浏览器操作对象
path = 'chromedriver.exe'

browser  = webdriver.Chrome(path)

# 3.访问网站
url = 'https://www.jd.com/'

browser.get(url)

# page_source获取网页源码
content = browser.page_source
print(content)