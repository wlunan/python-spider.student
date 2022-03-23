from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

def share_browser():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    # path 是自己Chrome浏览器的路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)



input = browser.find_element_by_id('kw')
input.send_keys('周杰伦')
browser.save_screenshot('baidi.jpg')
button = browser.find_element_by_id('su')
button.click()
import time
time.sleep(3)
browser.save_screenshot('zjl.jpg')

