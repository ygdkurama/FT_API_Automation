# -*- coding: utf-8 -*-

"""

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""

import allure
import pytest
from Common.Config import Config


@pytest.fixture()
def action():
    # 定义环境，确定是测试还是线上
    conf = Config()
    env = conf.get_conf('comm', 'env')
    host = conf.get_conf(env, 'host')
    """
    以下代码暂时无用
    version = conf.get_conf(env, 'version')
    tester = conf.get_conf(env, 'account')
    """

    """
    allure 2.0不用此方法，后续优化
    allure.environment(environment=env)
    allure.environment(hostname=host)
    allure.environment(version=version)
    allure.environment(tester=tester)
    """

    return env




