# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chromedriver")
driver.get('https://music.bugs.co.kr/')
# driver.implicitly_wait(5)
title = driver.find_element_by_xpath('//*[@id="gnbBody"]/div/div[1]/nav/ul/li[1]/a')    # 하이퍼링크는 따로 처리/ 가장 안쪽 태그까지 들어가기

print(title.text)

