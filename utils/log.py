import logging
import logging.config
import yaml


class CustomLogger:
    """
    自定义日志类
    """
    __logging_config_file = 'config/logging_config.yaml'
    __logger = ''

    @classmethod
    def get_logger(cls, logger_name="console_and_file"):
        if cls.__logger:
            return cls.__logger
        with open(cls.__logging_config_file, encoding='utf-8') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        cls.__logger = logging.getLogger(logger_name)
        return cls.__logger
