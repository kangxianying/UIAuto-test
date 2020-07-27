from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utils.log import CustomLogger
import time
import os
import allure


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


    # def screenShot(self, funcname):
    #     """
    #     Takes screenshot of the current open web page
    #     """
    #     fileName = funcname + "." + str(round(time.time() * 1000)) + ".png"
    #     screenshotDirectory = "../screenshots/"
    #     relativeFileName = screenshotDirectory + fileName
    #     currentDirectory = os.path.dirname(__file__)
    #     destinationFile = os.path.join(currentDirectory, relativeFileName)
    #     destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
    #
    #     try:
    #         if not os.path.exists(destinationDirectory):
    #             os.makedirs(destinationDirectory)
    #         self.driver.save_screenshot(destinationFile)
    #         with open(destinationFile, mode='rb') as f:
    #             file = f.read()
    #         allure.attach(file, '截图，文件目录：' + destinationFile, allure.attachment_type.PNG)
    #         self.log.info("Screenshot save to directory: " + destinationFile)
    #     except:
    #         self.log.error("### Exception Occurred when taking screenshot")

    def save_screenshot(self, func_name):
        '''
        保存截图
        :return:
        '''

        sc_dir = "../screenshots/"
        suffix = time.strftime('%m%d%H%M%S', time.localtime())
        screenshot_name = func_name + suffix + '.png'

        currentDirectory = os.path.dirname(__file__)
        screenshotDir = os.path.join(sc_dir, screenshot_name)

        save_file = os.path.join(currentDirectory, screenshotDir)


        self.save_screenshot(save_file)
        with open(save_file, mode='rb') as f:
            file = f.read()
        allure.attach(file, '截图，文件目录：' + save_file, allure.attachment_type.PNG)















