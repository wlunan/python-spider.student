# 1.导入selenium
from selenium import webdriver

# 2.创建谷歌浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 3.访问网站
url = 'http://www.baidu.com'

browser.get(url)

# 根据id来找到对象
button = browser.find_element_by_id('su')

# 根据标签的属性值(name)来获取对象
# button = browser.find_element_by_name('wd')

# 根据xpath语句来获取对象
# button = browser.find_element_by_xpath('//input[@id="su"]')

# 根据标签的名字来获取对象
# button = browser.find_elements_by_tag_name('input')

# 根据bs4语法来获取对象
# button = browser.find_element_by_css_selector('#su')

# 根据界面文本内容获取对象
# button = browser.find_element_by_link_text('新闻')
# <selenium.webdriver.remote.webelement.WebElement (session="dd9c5464db164671a3e5d9aec9b1abae",
# element="bb9e5585-d891-45ae-8103-36a389152f1d")>
# <selenium.webdriver.remote.webelement.WebElement (session="2d37406ba0a8d984d543f250db51f015",
# element="80de4a8b-af0b-42d1-b5d0-fcf58561dacd")>
# button = browser.find_element(by='id',value='su')

print(button)