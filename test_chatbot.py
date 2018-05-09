#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       :
# @Author     :
# @File       :

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import selenium

SECONDS = 5
SAVE_SECONDS = 25

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:3000")
time.sleep(SECONDS)
WEB_ELEMENT = driver.find_element_by_id('input-text')
WEB_ELEMENT.send_keys(Keys.ESCAPE)
WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)
WEB_ELEMENT.send_keys('新技術開発財団')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('リコージャパン')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('迫リコー')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('三愛健保')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('山梨電子工業')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('新技術開発財団')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('リコージャパン')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('迫リコー')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('三愛健保')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

WEB_ELEMENT.send_keys('ipad')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SAVE_SECONDS)
WEB_ELEMENT.send_keys('山梨電子工業')
WEB_ELEMENT.send_keys(Keys.ENTER)
time.sleep(SECONDS)

# driver.find_element_by_id('send').click()
# driver.find_element_by_id('password').send_keys('zuikaku22195068')
# driver.find_element_by_class_name('btn-danger').click()
# driver.implicitly_wait(5)
# driver.find_element_by_link_text(u"Query管理").click()
#
# time.sleep(5)
# checkboxs = driver.find_elements_by_name('queryCheck')
# for checkbox in checkboxs:
#     if checkbox.get_attribute('type') == 'checkbox':
#         checkbox.send_keys(selenium.webdriver.common.keys.Keys.SPACE)
#
# driver.execute_script('$("#thresholdSet").show()')
#
# driver.execute_script('$("#batchtest").click()')
# driver.implicitly_wait(5)
# upload = driver.find_element_by_id('selectfile')
# upload.send_keys('C:\\fakepath\\TainingData.csv')
# driver.find_element_by_link_text(u"バッチテスト実行").click()

# driver.find_element_by_id('iconofselectfile').click()

# driver.quit()