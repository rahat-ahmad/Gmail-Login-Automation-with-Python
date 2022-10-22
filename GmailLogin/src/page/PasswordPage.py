from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PasswordPage():

    def insertPassword(self,driver,password):
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(password)

    def clickOnSignInButton(self,driver):
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']/div/button"))).click()

    def getErrorMessage(self,driver):
        print(WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@jsname='B34EJ']/span"))).text)
        return WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@jsname='B34EJ']/span"))).text


    def validPasswordSigninCheck(self,driver):
        print(WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@id='headingText']/span"))).text)
        return WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[@id='headingText']/span"))).text