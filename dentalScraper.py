# # -*- coding: utf-8 -*-
# import sys
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import re
# def rePlaceData(value):
#     numbers = re.findall("\d+", value)
#     result = ""
#     for i in numbers:
#         decodedNumber = i.decode('utf-8');
#         result += decodedNumber

# def getLinaData(name, birth, gender):
#     driver = webdriver.Chrome("./chromedriver")
#     scrapingResult = {
#         'company': "라이나",
#         'price': 0,
#         'contents': []
#     }
#     driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')
#     driver.implicitly_wait(3)

#     inputBirth = driver.find_element_by_xpath('//*[@id="birthday"]')
#     inputBirth.send_keys(birth)
#     if gender == 1:
#         driver.find_element_by_xpath('//*[@id="main_btn_male"]').click()
#     else:
#         driver.find_element_by_xpath('//*[@id="main_btn_female"]').click()

#     driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]').click()

#     driver.implicitly_wait(5)
#     htmlResult = driver.find_element_by_xpath('//*[@id="mo_amount_span"]').text
#     resultValue = rePlaceData(htmlResult)
#     scrapingResult['price'] = resultValue

#     driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]').click()
#     driver.implicitly_wait(3)
#     tableBody = driver.find_element_by_xpath('//*[@id="planPonA2"]/div/div[2]/div/div/table[1]/tbody')
#     rows = tableBody.find_elements_by_tag_name("tr")
#     contentsList = []
#     for index, value in enumerate(rows):
#         if index != 0:
#             # print value.find_elements_by_tag_name('th')[0].text
#             contentsList.append(value.find_elements_by_tag_name('th')[0].text.encode('utf-8'))
#     scrapingResult['contents'] = contentsList
#     print scrapingResult

# def getAIAData(name, birth, gender):
#     scrapingResult = {
#         'company': "라이나",
#         'price': 0,
#         'contents': []
#     }

#     driver = webdriver.Chrome("./chromedriver")
#     driver.get('https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
#     if gender == 2:
#         selectGender = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
#         selectGender.click()
#     else:
#         selectGender = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
#         selectGender.click()

#     inputBirth = driver.find_element_by_xpath('//*[@id="aia644363719"]')
#     inputBirth.send_keys(birth)
#     driver.implicitly_wait(3)

#     driver.find_element_by_xpath('//*[@id="btn806817556"]').click()
#     cost = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]').text
#     # print(cost)
#     scrapingResult['price'] = cost

#     # showDetail = driver.find_element_by_xpath('//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]/span')
#     # showDetail.click()

#     tableBody = driver.find_element_by_xpath('//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
#     driver.find_element_by_xpath('//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
#     rows = tableBody.find_elements_by_tag_name("tr")
#     contentsList = []
#     for index, value in enumerate(rows):
#         if index != 0:
#             print value.find_elements_by_tag_name('td')[0].text
#             contentsList.append(value.find_elements_by_tag_name('td')[0].text.encode('utf-8'))

#     scrapingResult['contents'] = contentsList
#     print scrapingResult


# # getAIAData('이윤하','19931123',2)
# # print(getLinaData('이윤하', '931123', 2))


# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import re

def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i.decode('utf-8')
        result += decodedNumber
    return result

def getLinaData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver.implicitly_wait(3)
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')
    driver.implicitly_wait(3)

    textBox = driver.find_element_by_xpath('//*[@id="birthday"]')#//*[@id="birthday"]
    textBox.send_keys(birth);

    if gender == 2:
        femaleBtn = driver.find_element_by_xpath('//*[@id="main_btn_female"]')
        femaleBtn.click();
    else:
        maleBtn = driver.find_element_by_xpath('//*[@id="main_btn_male"]')
        maleBtn.click();

    resultBtn = driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]')
    resultBtn.click();

    htmlResult = driver.find_element_by_xpath('//*[@id="mo_amount_span"]').text;
    resultValue = rePlaceData(htmlResult)
    print(htmlResult);
    scrapingResult['price'] = resultValue
    detailBtn = driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]')
    detailBtn.click();
    tableBody = driver.find_element_by_xpath('//*[@id="planPonA2"]/div/div[2]/div/div/table[1]').find_element_by_tag_name('tbody')
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print value.find_elements_by_tag_name('th')[0].text
            contentsList.append(value.find_elements_by_tag_name('th')[0].text.encode('utf-8'))
    scrapingResult['contents'] = contentsList
    return scrapingResult
    
def getAIAData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "AIA",
        'price': 0,
        'contents': []
    }
    driver.implicitly_wait(3)
    driver.get('https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    driver.implicitly_wait(3)
    # name.decode('utf-8').encode('euc-kr')
    textBox = driver.find_element_by_xpath('//*[@id="aia644363719"]');
    textBox.send_keys("19"+birth);
    if gender == 2:
        femaleBtn = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        femaleBtn.click();
    else:
        maleBtn = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        maleBtn.click();
    resultBtn = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    resultBtn.click();
    driver.implicitly_wait(3)
    htmlResult = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]').text;
    resultValue = rePlaceData(htmlResult)
    scrapingResult['price'] = resultValue
    tableBody = driver.find_element_by_xpath('//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
    driver.find_element_by_xpath('//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print value.find_elements_by_tag_name('td')[0].text
            contentsList.append(value.find_elements_by_tag_name('td')[0].text.encode('utf-8'))
    scrapingResult['contents'] = contentsList
    return scrapingResult

def getAXAData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "AXA",
        'price': 0,
        'contents': []
    }
    driver.implicitly_wait(3)
    driver.get('https://www.axa.co.kr/ActionControler.action?screenID=SHLI0000&actionID=I16#')
    driver.implicitly_wait(3)
    
    birthBox = driver.find_element_by_xpath('//*[@id="if_02"]')
    birthBox.send_keys(birth)
    genderBox = driver.find_element_by_xpath('//*[@id="frmStep01"]/div[1]/table/tbody/tr/td/input[2]');
    genderBox.send_keys(gender);

    driver.find_element_by_xpath('//*[@id="frmStep01"]/div[2]/div').click()
    driver.implicitly_wait(3)

    delay = 3
    WebDriverWait(driver, delay).until(
        expected_conditions.invisibility_of_element(
            (By.CSS_SELECTOR, "#overlay overlay_loading")
                )
    )

    htmlResult = driver.find_element_by_xpath('//*[@id="paya_prem"]').text
    resultValue = rePlaceData(htmlResult)
    scrapingResult['price'] = resultValue

    tableBody = driver.find_element_by_xpath('//*[@id="cov_disp"]')
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print value.find_elements_by_tag_name('td')[0].text
            contentsList.append(value.find_elements_by_tag_name('td')[0].text.encode('utf-8'))
    scrapingResult['contents'] = contentsList
    print(scrapingResult)
    return scrapingResult
