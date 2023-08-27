import json
from os import path


def get_path(file):
    return path.abspath(path.join(path.dirname(__file__), file))


class Config:
    instance = None

    @staticmethod
    def get_instance(*args, **kwargs):
        if not Config.instance:
            Config.instance = Config(*args, **kwargs)

        return Config.instance

    def __init__(self, file_path='config.json'):
        self.file_path = get_path(file_path)
        self.data = {}
        self.load()

    def get(self, key):
        val = None
        try:
            val = self.data[key]
        except KeyError:
            pass
        return val

    def set(self, key, value):
        self.data[key] = value

    def load(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.data = json.load(f)