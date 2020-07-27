import yaml
from utils.log import CustomLogger



logger = CustomLogger.get_logger()
def get_yaml_data(yaml_file):
    env_config = {}
    with open(yaml_file, encoding='utf-8') as config_file_obj:
        yaml_obj = yaml.load(config_file_obj, Loader=yaml.FullLoader)

    for key, value in yaml_obj.items():
        env_config[key] = value

    return env_config











