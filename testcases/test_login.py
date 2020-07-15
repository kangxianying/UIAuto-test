import pytest
from appPage.login_page import LoginPage

@pytest.mark.usefixtures('get_driver')
class TestLogin:

    user_info = [('139297789022', '123456')]


    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.lp = LoginPage(get_driver)


    @pytest.mark.parametrize('phone, password', user_info)
    def test_login_page_sucess(self, phone, password):
        self.lp.login(phone, password)
        res = self.lp.verifyLoginSuccessful()
        assert res == True









