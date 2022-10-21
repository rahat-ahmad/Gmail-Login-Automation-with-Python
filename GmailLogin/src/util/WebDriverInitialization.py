

import undetected_chromedriver


class WebDriverInitialization():

    def undetectedChromeDriverInitialization(self):
        driver = undetected_chromedriver.Chrome(use_subprocess=True)
        driver.implicitly_wait(100)
        driver.maximize_window()
        return driver

# if __name__ == '__main__':
#     WebDriverInitialization().undetectedChromeDriverInitialization()