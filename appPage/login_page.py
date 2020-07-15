from selenium.webdriver.common.by import By
from base.appium_driver import AppiumDriver


class LoginPage(AppiumDriver):

    # Locators
    _go_to_login = "com.mallestudio.gugu.app:id/tv_go_to_login"
    _phone_field = "com.mallestudio.gugu.app:id/et_phone"
    _password_field = "com.mallestudio.gugu.app:id/et_pwd"
    _login_button = "com.mallestudio.gugu.app:id/tv_login"
    _popUp_cancel_button = "com.mallestudio.gugu.app:id/tv_cancel"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver



    def login(self, phone="", password=""):

        el1 = self.driver.find_element(By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout")
        el1.click()
        self.driver.implicitly_wait(10)

        # 点击去登录
        self.elementClick(self._go_to_login)

        # 输入手机号码
        self.sendKeys(phone, self._phone_field)

        # 输入密码
        self.sendKeys(password, self._password_field)

        # 点击登录按钮
        self.elementClick(self._login_button)

        self.driver.implicitly_wait(10)
        # 登录成功之后，进入首页，会出现弹窗


    def verifyLoginSuccessful(self):
        # 登录成功之后，出现首页弹窗
        result = self.isElementPresent(self._popUp_cancel_button)
        self.elementClick(self._popUp_cancel_button)
        return result



















