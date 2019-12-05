# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chromedriver")
# driver.get('https://www.alimi.or.kr/api/a/vacant/selectApiVacant.do')

# table = driver.find_element_by_class_name('search_list')    # 유일한 이름인 클래스명으로 찾을 수 있다
# tableBody = table.find_element_by_tag_name('tbody')
# trContents = tableBody.find_elements_by_tag_name('tr')

# for index, value in enumerate(trContents):
#     if index != 0:
#         address = value.find_elements_by_tag_name('td')[2]
#         print(address.text)

driver.get('https://music.bugs.co.kr/chart?wl_ref=M_left_02_01')

# table = driver.find_element_by_class_name('list.trackList.byChart')
# tableBody = table.find_element_by_tag_name('tbody')
# trContents = tableBody.find_elements_by_tag_name('tr')

# for index, value in enumerate(trContents):
#     if index < 10:
#         name, artist = value.find_elements_by_tag_name('td')[3], value.find_elements_by_tag_name('td')[4]
#         print(index + 1, name.text, artist.text)
    
tr = driver.find_elements_by_xpath('//*[@id="CHARTrealtime"]/table/tbody/tr[1]')
print(tr)