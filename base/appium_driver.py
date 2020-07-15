from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utils.log import CustomLogger
import time
import os


class AppiumDriver:
    log = CustomLogger.get_logger()

    def __init__(self, driver):
        self.driver = driver



    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          f" 不正确/不支持")



    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f"元素找到 locator: " + locator +
                      " and  locatorType: " + locatorType)

        except:
            self.log.info(f"元素没有找到 locator: " + locator +
                          " and  locatorType: " + locatorType)

        return element



    def elementClick(self, locator="", locatorType="id", element=None):
        """
        点击按钮事件
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f"点击元素成功" + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info(f"无法点击元素成功" + locator +
                          " locatorType: " + locatorType)
            print_stack()



    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        发送文本信息
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"发送文本信息" + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info(f"无法发送文本信息" + locator +
                  " locatorType: " + locatorType)
            print_stack()



    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        页面元素是否存在
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False


















