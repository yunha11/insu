# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i.decode('utf-8');
        result += decodedNumber

def getLinaData(name, birth, gender):
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver = webdriver.Chrome("./chromedriver")
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')

    inputBirth = driver.find_element_by_xpath('//*[@id="birthday"]')
    inputBirth.send_keys(birth)
    if gender == 1:
        driver.find_element_by_xpath('//*[@id="main_btn_male"]').click()
    else:
        driver.find_element_by_xpath('//*[@id="main_btn_female"]').click()

    driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]').click()

    driver.implicitly_wait(5)
    cost = driver.find_element_by_xpath('//*[@id="mo_amount_span"]').text
    resultValue = rePlaceData(cost)
    scrapingResult['price'] = resultValue
    driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]').click()
    driver.implicitly_wait(3)
    nameDental = driver.find_element_by_xpath('//*[@id="planPonA2"]/div/div[2]/div/div/h2[1]').text
    result.append(nameDental)
    result.append(resultValue)
    tableBody = driver.find_element_by_xpath('//*[@id="planPonA2"]/div/div[2]/div/div/table[1]/tbody')
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            # print value.find_elements_by_tag_name('th')[0].text
            contentsList.append(value.find_elements_by_tag_name('th')[0].text.encode('utf-8'))
    scrapingResult['contents'] = contentsList
    print scrapingResult

def getAIAData(name, birth, gender):
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }

    driver = webdriver.Chrome("./chromedriver")
    driver.get('https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    if gender == 2:
        selectGender = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        selectGender.click()
    else:
        selectGender = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        selectGender.click()

    inputBirth = driver.find_element_by_xpath('//*[@id="aia644363719"]')
    inputBirth.send_keys(birth)
    driver.implicitly_wait(3)

    driver.find_element_by_xpath('//*[@id="btn806817556"]').click()
    cost = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]').text
    # print(cost)
    scrapingResult['price'] = cost

    # showDetail = driver.find_element_by_xpath('//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]/span')
    # showDetail.click()

    tableBody = driver.find_element_by_xpath('//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
    driver.find_element_by_xpath('//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print value.find_elements_by_tag_name('td')[0].text
            contentsList.append(value.find_elements_by_tag_name('td')[0].text.encode('utf-8'))

    scrapingResult['contents'] = contentsList
    print scrapingResult


getAIAData('이윤하','19931123',2)
# print(getLinaData('이윤하', '931123', 2))
