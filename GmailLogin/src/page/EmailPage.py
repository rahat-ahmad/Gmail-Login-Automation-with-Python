from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class EmailPage():

    def emailOrPhoneInsert(self,driver,emailOrPhone):
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(emailOrPhone)


    def nextButtonClick(self,driver):
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='identifierNext']/div/button"))).click()

    def getErrorMessage(self,driver):
        print(WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='o6cuMc']"))).text)
        return WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='o6cuMc']"))).text

    def validEmailSigninCheck(self,driver):
        print(WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@id='headingText']/span"))).text)
        return WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@id='headingText']/span"))).text