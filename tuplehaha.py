from appium import webdriver

import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(2)
# driver.quit()