# -*- coding: utf-8 -*-

from configparser import ConfigParser
from Common import Log
import os


class Config:

    # path
    path_dir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = Config.path_dir + '\\Conf\\config.ini'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        self.config.read(self.conf_path, encoding='utf-8')
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    c = Config()