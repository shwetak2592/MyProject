import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="../resources/chromedriver_new80.exe")
        self.driver.maximize_window()
        self.driver.get("http://annauniv.edu/")

    def test_dept_link(self):
       # dept_link = self.driver.find_element_by_xpath("//a[@href = 'http://www.annauniv.edu/department/index.php']")
        wait = WebDriverWait(self.driver, 30)
        dept_link1 = self.driver.find_element_by_xpath("(//table)[4]/tbody/tr/td[5]//a")
       # dept_link1 = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,'Departments')))
       # dept_link1.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(dept_link1).click().perform()
        time.sleep(3)