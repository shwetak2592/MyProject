import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="../resources/chromedriver_new80.exe")
        self.driver.maximize_window()
        self.driver.get("http://cookbook.seleniumacademy.com/DoubleClickDemo.html")

    def test_color_click(self):
        element = self.driver.find_element_by_id("message")
        print(element.value_of_css_property("background-color"))
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        print(element.value_of_css_property("background-color"))