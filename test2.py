

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/anil.koyuncu/projects/selenium-demo/chromedriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.browserstack.com/users/sign_in")
        time.sleep(10)
        username = driver.find_element(By.ID, "user_email_login")
        password = driver.find_element(By.ID, "user_password")
        login = driver.find_element(By.NAME, "commit")
        username.send_keys("rabbitfish37.43hbub@gmail.com")
        password.send_keys("rabbitfish37.43hbub@gmail.com")
        login.click()
        time.sleep(10)
        actualUrl = "https://app-live.browserstack.com/"
        expectedUrl = driver.current_url
        self.assertTrue(expectedUrl.startswith(actualUrl))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()