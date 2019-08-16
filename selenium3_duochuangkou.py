#!user/bin/env python
# coding:utf-8

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://mail.sina.com.cn/")
driver.implicitly_wait(30)
now_handle=driver.current_window_handle
sleep(2)
driver.find_element_by_link_text('注册').click()
sleep(2)
handles=driver.window_handles
for handle in handles:
    if handle != now_handle:
        driver.switch_to_window(handle)
        sleep(2)
        driver.find_element_by_name('email').send_keys('zhangji')
        sleep(2)
        driver.close()
driver.switch_to_window(now_handle)
sleep(3)
driver.find_element_by_id('freename').send_keys('zhangji')
sleep(4)
driver.quit()
