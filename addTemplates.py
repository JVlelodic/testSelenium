#!/usr/bin/env python
# coding: utf-8

#PATHS, USERNAMES & PASSWORDS have been changed for privacy 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import templates

EXE_PATH = r'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get('https://seido.ytml.com.au')
time.sleep(5)

driver.find_element_by_id("Email").send_keys("username")
driver.find_element_by_id ("Password").send_keys("password")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(8)

driver.find_element_by_xpath("//a[@data-seido = 'nav_settings']").click()
time.sleep(2)

driver.find_element_by_xpath("//a[text() = 'System']").click()
WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'wrapper wrapper-content']/div/div/div/ul")))

driver.find_element_by_xpath("//span[@style = 'color: rgb(255, 255, 255); background-color: rgb(46, 84, 130);']").click()

driver.find_element_by_xpath("//a[text() = 'Email Templates']").click()

for title in templates.templates.keys():

    #Click add template button 
    driver.find_element_by_xpath("//button[@tooltip = 'Add Template']").click()
    WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH, "//button[text() = 'Cancel']")))
    time.sleep(2)

    #Enter details 
    driver.find_element_by_xpath("//input[@placeholder = 'Template name']").send_keys(title)
    subject = templates.templates[title][0]
    driver.find_element_by_xpath("//input[@placeholder = 'Email subject']").send_keys(subject)
    
    #Writing to Iframe
    content = templates.templates[title][1]
    driver.switch_to.frame(driver.find_element_by_xpath("//editor/div/div/div/iframe"))
    driver.find_element_by_xpath("//html/body[@id= 'tinymce']").send_keys(content)
    driver.switch_to.default_content()

    #Selecting the FSG
    if templates.templates[title][2] is True:
        driver.find_element_by_xpath("//div[@class = 'c-btn']").click()
        WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH, "//div[@style= 'overflow: auto; max-height: 300px;']")))
        driver.find_element_by_xpath("//label[text() = 'Account: Adviser Info | FSG']").click()

    #Save the template
    driver.find_element_by_xpath("//button[text() = 'Save']").click()
    WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH, '//a[text() = "%s" ]' % title)))

driver.find_element_by_xpath("//li[@class ='ng-star-inserted']/a[text() = 'Accounts']").click() 
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//a[@href ="mailto:email"]')))
time.sleep(5)

for email in templates.emails: 

        #Press add account button 
        driver.find_element_by_xpath("//button[@tooltip='Add Account']").click()

        #Select administrator 
        role = driver.find_element_by_xpath("//select[@name='selectedRole']")
        role.click()
        driver.find_element_by_xpath("//select[@name='selectedRole']/option[1]").click()

        #Add user email 
        driver.find_element_by_xpath("//div[@class='col-sm-12'] /div[@class='form-group']/input[@placeholder='Email Address']").send_keys(email)

        #Add the account
        form = driver.find_elements_by_xpath("//div[@class='form-group text-center']/button[@class='btn btn-primary']")[1].click()
        # time.sleep(20)
        email_value = " " + email 
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//div[text() = "User has been created"]')))


