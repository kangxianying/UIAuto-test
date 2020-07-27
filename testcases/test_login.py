import pytest
import allure
from appPage.login_page import LoginPage



@allure.feature('登录模块')
@pytest.mark.usefixtures('get_driver')
class TestLogin:

    user_info = [('139297789022', '123456')]


    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.lp = LoginPage(get_driver)



    @allure.story('账号密码登录')
    @allure.title('账号密码登录成功')
    @pytest.mark.parametrize('phone, password', user_info)
    def test_login_page_sucess(self, phone, password):
        self.lp.login(phone, password)
        res = self.lp.verifyLoginSuccessful()
        self.lp.save_screenshot('verifyLoginSuccessful')
        assert res == True









