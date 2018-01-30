# -*- coding: utf-8 -*-
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class t2unitpy(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_t2unitpy(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.ru/?gws_rd=ssl")
        wd.find_element_by_name("btnI").click()
        wd.find_element_by_link_text("О проекте").click()
        wd.find_element_by_id("logo").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
