# -*- coding: utf-8 -*-

"""
定义所有测试数据

"""
import os
from Common import Log, ReadYml

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class GetParameter:
    def __init__(self, name):
        self.name = name

    def get_params(self):
        aa = self.name
        log.info('解析yaml, Path' + path_dir + '\Params\Yaml\%s.yml' % self.name)
        print('解析yaml, Path' + path_dir + '\Params\Yaml\%s.yml' % self.name)
        data = ReadYml.GetPages().get_page_list()
        params = data[self.name]
        cases = {}
        for i in range(0, len(params)):
            cases[params[i]['id']] = {'desc': params[i]['desc'],
                                      'url': params[i]['url'],
                                      'data': params[i]['data'],
                                      'header': params[i]['header'],
                                      'res': params[i]['res']}
        return cases
