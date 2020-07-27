import pytest
# import yaml
import os
from appium import webdriver
from utils.log import CustomLogger
from utils import common



env_config_file = 'config/chuman_caps.yaml'
logger = CustomLogger.get_logger()


def pytest_addoption(parser):
    """
        增加自定义命令行参数
    """
    parser.addoption(
        "--env", action="store", default="api_android", help="testcase execute environment"
    )


def pytest_configure(config):

    env = config.getoption("--env")
    os.environ['env'] = env
    env_config = common.get_yaml_data(env_config_file)[env]
    for key, value in env_config.items():
        os.environ[key] = str(value)


    for key in os.environ:
        print(key, os.environ[key])

    logger.info(f"{'-' * 5}开始执行新一轮的测试用例，测试环境是{env}{'-' * 5}")





# @pytest.fixture(scope='class')
# def get_driver():
#     with open(env_config_file, 'r', encoding='utf-8') as file:
#         data = yaml.load(file, Loader=yaml.FullLoader)
#     caps = {}
#     caps['deviceName'] = data['deviceName']
#     caps['platformName'] = data['platformName']
#     caps['platformVersion'] = data['platformVersion']
#     caps['appPackage'] = data['appPackage']
#     caps['appActivity'] = data['appActivity']
#     driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', caps)
#     # 设置一个全局的等待超时时间 10s
#     driver.implicitly_wait(20)
#     return driver

@pytest.fixture(scope='class')
def get_driver():
    caps = {}
    caps['deviceName'] = os.getenv('deviceName')
    caps['platformName'] = os.getenv('platformName')
    caps['platformVersion'] = os.getenv('platformVersion')
    caps['appPackage'] = os.getenv('appPackage')
    caps['appActivity'] = os.getenv('appActivity')
    print(str(os.getenv('ip')))
    print(str(os.getenv('port')))
    driver = webdriver.Remote('http://'+str(os.getenv('ip'))+':'+str(os.getenv('port'))+'/wd/hub', caps)
    # 设置一个全局的等待超时时间 10s
    driver.implicitly_wait(20)
    return driver


