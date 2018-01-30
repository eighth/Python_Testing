# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.google.ru/?gws_rd=ssl")
    wd.find_element_by_name("btnI").click()
    wd.find_element_by_link_text("О проекте").click()
    wd.find_element_by_id("logo").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
