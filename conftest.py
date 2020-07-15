from appium import webdriver
import pytest
import yaml


@pytest.fixture(scope='class')
def get_driver():
    with open('config/chuman_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    caps = {}
    caps['deviceName'] = data['deviceName']
    caps['platformName'] = data['platformName']
    caps['platformVersion'] = data['platformVersion']
    caps['appPackage'] = data['appPackage']
    caps['appActivity'] = data['appActivity']
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', caps)
    # 设置一个全局的等待超时时间 10s
    driver.implicitly_wait(20)
    return driver
