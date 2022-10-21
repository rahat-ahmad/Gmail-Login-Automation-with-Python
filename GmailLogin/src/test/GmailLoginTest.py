import time
import unittest

from src.page import EmailPage, PasswordPage
from src.util import WebDriverInitialization, TestResult


class GmailLoginTest(unittest.TestCase):
    global emailPage
    global passwordPage
    global testStatus
    emailPage = EmailPage.EmailPage()
    passwordPage = PasswordPage.PasswordPage()
    testStatus = TestResult.TestResult()


    def setUp(self):
        print("Starting the tests.")
        global driver
        webDriverInitialization = WebDriverInitialization.WebDriverInitialization()
        driver = webDriverInitialization.undetectedChromeDriverInitialization()
        if driver is None:
            raise unittest.SkipTest("Driver Not Loaded")



    # @unittest.skip
    def test_0001_LoginWithEmptyEmail(self):
        print("Case-01: Login with Empty Email or Phone")
        driver.get("https://www.gmail.com")
        emailPage.emailOrPhoneInsert(driver,"")
        emailPage.nextButtonClick(driver)
        time.sleep(2)
        testStatus.writingTestResult("G2","Pass")

    # @unittest.skip
    def test_0002_LoginWithInvalidEmailOrPhone(self):
        print("Case-02: Login with invalid Email or Phone")
        driver.get("https://www.gmail.com")
        emailPage.emailOrPhoneInsert(driver, testStatus.readTestData(1,2))
        emailPage.nextButtonClick(driver)
        time.sleep(2)
        testStatus.writingTestResult("G3", "Pass")

    # @unittest.skip
    def test_0003_LoginWithoutPassword(self):
        print("Case-03: Login with Empty Password")
        driver.get("https://www.gmail.com")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,"")
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        testStatus.writingTestResult("G4", "Pass")

    # @unittest.skip
    def test_0004_LoginWithInvalidPassword(self):
        print("Case-04: Login with Invalid Password")
        driver.get("https://www.gmail.com")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,testStatus.readTestData(1,3))
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        testStatus.writingTestResult("G5", "Pass")

    def test_0005_LoginWithValidPassword(self):
        print("Case-05: Login with valid Password")
        driver.get("https://www.gmail.com")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,testStatus.readTestData(2,3))
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        testStatus.writingTestResult("G6", "Pass")

    def tearDown(self):
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()