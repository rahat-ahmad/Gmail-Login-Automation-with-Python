import time
import unittest

from src.page import EmailPage, PasswordPage
from src.util import WebDriverInitialization, GetSetDataFromExcel


class GmailLoginTest(unittest.TestCase):
    global emailPage
    global passwordPage
    global testStatus
    emailPage = EmailPage.EmailPage()
    passwordPage = PasswordPage.PasswordPage()
    testStatus = GetSetDataFromExcel.GetSetDataFromExcel()


    def setUp(self):
        global driver
        webDriverInitialization = WebDriverInitialization.WebDriverInitialization()
        driver = webDriverInitialization.undetectedChromeDriverInitialization()
        driver.get("https://www.gmail.com")
        if driver is None:
            raise unittest.SkipTest("Driver Not Loaded")



    # @unittest.skip
    def test_0001_LoginWithEmptyEmail(self):
        print("Case-01: Login with Empty Email or Phone")
        emailPage.emailOrPhoneInsert(driver,"")
        emailPage.nextButtonClick(driver)
        time.sleep(2)
        errorMessage = emailPage.getErrorMessage(driver)
        if 'Enter an email or phone number' in errorMessage:
            testStatus.writingTestResult("G2","Pass")
        else:
            testStatus.writingTestResult("G2", "Failed")


    # @unittest.skip
    def test_0002_LoginWithInvalidEmailOrPhone(self):
        print("Case-02: Login with invalid Email or Phone")
        emailPage.emailOrPhoneInsert(driver, testStatus.readTestData(1,2))
        emailPage.nextButtonClick(driver)
        time.sleep(2)
        errorMessage = emailPage.getErrorMessage(driver)
        if 'Couldn’t find your Google Account' in errorMessage:
            testStatus.writingTestResult("G3", "Pass")
        else:
            testStatus.writingTestResult("G3", "Failed")

    # @unittest.skip
    def test_0003_LoginWithValidEmailOrPhone(self):
        print("Case-03: Login with valid Email or Phone")
        emailPage.emailOrPhoneInsert(driver, testStatus.readTestData(2, 2))
        emailPage.nextButtonClick(driver)
        time.sleep(2)
        welcomeMessage = emailPage.validEmailSigninCheck(driver)
        if 'Welcome' in welcomeMessage:
            testStatus.writingTestResult("G4", "Pass")
        else:
            testStatus.writingTestResult("G4", "Failed")

    # @unittest.skip
    def test_0004_LoginWithoutPassword(self):
        print("Case-04: Login with Empty Password")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,"")
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        errorMessage = passwordPage.getErrorMessage(driver)
        if 'Enter a password' in errorMessage:
            testStatus.writingTestResult("G5", "Pass")
        else:
            testStatus.writingTestResult("G5", "Failed")

    # @unittest.skip
    def test_0005_LoginWithInvalidPassword(self):
        print("Case-05: Login with Invalid Password")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,testStatus.readTestData(1,3))
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        errorMessage = passwordPage.getErrorMessage(driver)
        if 'Wrong password.' in errorMessage:
            testStatus.writingTestResult("G6", "Pass")
        else:
            testStatus.writingTestResult("G6", "Failed")

    # @unittest.skip
    def test_0006_LoginWithValidPassword(self):
        print("Case-06: Login with valid Password")
        emailPage.emailOrPhoneInsert(driver,testStatus.readTestData(2,2))
        emailPage.nextButtonClick(driver)
        passwordPage.insertPassword(driver,testStatus.readTestData(2,3))
        passwordPage.clickOnSignInButton(driver)
        time.sleep(2)
        welcomeMessage = passwordPage.validPasswordSigninCheck(driver)
        if '2-Step Verification' in welcomeMessage:
            testStatus.writingTestResult("G7", "Pass")
        else:
            testStatus.writingTestResult("G7", "Failed")

    def tearDown(self):
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()