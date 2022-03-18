from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os

def main():
    path = "/usr/bin/geckodriver"
    if(os.path.exists(path) == False):
        print("Please download geckodriver for firefox and place in /usr/bin/")
    else:
        driver = webdriver.Firefox()
        site = "http://localhost/"
        driver.get(site)
        ip = '127.0.0.1'


        usernameBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/input[1]')
        passwordBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/input[2]')
        loginButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/fieldset/p/input')

        usernameBox.send_keys('admin')
        passwordBox.send_keys('password')
        loginButton.click()






if __name__ == "__main__":
    main()