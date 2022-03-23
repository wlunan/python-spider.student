from selenium import webdriver

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# 获取文本输入框对象
input = browser.find_element_by_id('kw')
# 在文本框输入周杰伦 send_keys()
input.send_keys('周杰伦')

import time
# 休眠一秒
time.sleep(2)

# 获取百度一下的按钮并点击
button = browser.find_element_by_id('su')
button.click()

time.sleep(1)

# 滑到页面底端
js_button = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_button)

time.sleep(1)
# 获取下一页的按钮
next = browser.find_element_by_xpath('//a[@class="n"]')
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(1)

# 回去
browser.forward()

time.sleep(1)

# 获取文本框输入对象
input = browser.find_element_by_id('kw').clear()
input = browser.find_element_by_id('kw')
input.send_keys('李方圆')

time.sleep(1)
# 获取百度一下按钮并点击
button = browser.find_element_by_id('su')
button.click()
# 退出
# browser.quit()