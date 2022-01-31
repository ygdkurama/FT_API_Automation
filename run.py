# -*- coding: utf-8 -*-

"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
# '--html=Report/report.html' 使用pytest-html生成HTML报告,--self-contained-html使用该参数，则生成的css和HTML合为一个文件

"""
import pytest, sys

from Common import Log, Config
from Common import Shell

import os

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    report_path = str(os.path.dirname(os.path.abspath(__file__)))
    xml_report_path = report_path + '\\Report\\xml'
    html_report_path = report_path + '\\Report\\html --clean'

    # 定义测试集
    # allure_list可指定具体的features
    # allure_list = '--allure_features=littleYellowMan'
    # args = ['-x', '-s', '-q', '--alluredir', xml_report_path, allure_list, '--html=Report/report.html',
    #         '--self-contained-html']
    args = ['-x', '-s', '-q', '--alluredir', xml_report_path, '--html=Report/report.html',
            '--self-contained-html']
    pytest.main(args)

    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
    #
    # try:
    #     mail = Email.SendMail()
    #     mail.sendMail()
    # except Exception as e:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise