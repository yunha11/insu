# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chromedriver")
driver.get('http://luris.molit.go.kr/web/index.jsp')

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[1]/ul/li[1]/select'))
sidoSelect.select_by_visible_text('인천광역시')
guSelect = Select(driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[1]/ul/li[2]/select'))
guSelect.select_by_visible_text('부평구')
dongSelect = Select(driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[1]/ul/li[3]/select'))
dongSelect.select_by_visible_text('부평동')
inputBonnum = driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[2]/ul/li[2]/input')
inputBonnum.send_keys('70')
inputBunum = driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[2]/ul/li[4]/input')
inputBunum.send_keys('125')

driver.find_element_by_xpath('//*[@id="gnb_tab11"]/div/div[2]/div/div[3]/button').click()
