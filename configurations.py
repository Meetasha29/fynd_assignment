from flask import current_app


class Settings(object):
    def __init__(self, config_dict):
        for key, value in config_dict.items():
            setattr(self, key, value)


settings = Settings(current_app.config)
