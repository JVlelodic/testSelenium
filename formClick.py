from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



#Initiate and load webpage
EXE_PATH = r'path_to_chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get('https://seido.ytml.com.au')
time.sleep(5)

username = "username"
password = "password"

#Login into Seido
driver.find_element_by_id("Email").send_keys(username)
driver.find_element_by_id ("Password").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(8)

i= 1
accounts = driver.find_elements_by_xpath("//a[@class='ellipsis dropdown-item ng-star-inserted']")


while i < len(accounts):
    driver.find_element_by_xpath("//span[@class='ellipsis inline-block mt-2 current-name']").click()
    time.sleep(2)
    driver.find_elements_by_xpath("//a[@class='ellipsis dropdown-item ng-star-inserted']")[i].click()
    print("account clicked")
    WebDriverWait(driver,120).until(EC.presence_of_element_located((By.XPATH, "//span[text() = 'Settings']")))
    i+=1
    print(i)

    #Press Settings Button
    settings = driver.find_elements_by_class_name('has-second-level')[3]
    settings.click()
    print("this has happened")
    time.sleep(2)

    #Press account button
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(settings, 5, 50)
    action.click()
    action.perform()
    WebDriverWait(driver,120).until(EC.presence_of_element_located((By.XPATH, "//div[@class= 'ibox-content no-padding no-borders no-margins group-detail-vsScroll vSscroll']")))

    #Email Accounts
    emails = ["list", "of", "emails", "to", "be", "added"]

    for email in emails:

        #Press add account button
        driver.find_element_by_xpath("//button[@tooltip='Add Account']").click()
        print("add clicked")
        time.sleep(2)

        #Select administrator
        role = driver.find_element_by_xpath("//select[@name='selectedRole']")
        role.click()
        time.sleep(2)
        driver.find_element_by_xpath("//select[@name='selectedRole']/option[1]").click()
        time.sleep(2)

        #Add user email
        driver.find_element_by_xpath("//div[@class='col-sm-12'] /div[@class='form-group']/input[@placeholder='Email Address']").send_keys(email)
        time.sleep(1)

        #Add the account
        form = driver.find_elements_by_xpath("//div[@class='form-group text-center']/button[@class='btn btn-primary']")[1].click()
        # time.sleep(20)
        email_value = " " + email
        WebDriverWait(driver,150).until(EC.presence_of_element_located((By.XPATH, '//a[text() = "%s" ]' % email_value)))
        print("buttons Pressed")


print("finished")
