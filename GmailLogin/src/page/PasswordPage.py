from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PasswordPage():

    def insertPassword(self,driver,password):
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(password)

    def clickOnSignInButton(self,driver):
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']/div/button"))).click()