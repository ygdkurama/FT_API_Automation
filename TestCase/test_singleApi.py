import os

import allure

from Common.Config import Config
from Common.Log import MyLog
from Common.ReadExcel import get_cases
from Common.Request import Request
from Params.params import GetParameter
from Common.Assert import Assertions
from TestCase import loginApi
from TestCase.loginApi import LoginApi


@allure.feature('singleApi')
class TestLoginWithPwd:
    data = GetParameter('fantuanReviews').get_params()
    env = Config().get_conf('comm', 'env')
    host = Config().get_conf(env, 'host')
    log = MyLog()
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\Params\\Param\\Excel\\case.xlsx'
    cases = get_cases(filepath, "点评测试")
    ast = Assertions()

    #研就action的传递test2

    def postBase(self, host, case_num):
        Geturl = host + self.cases[case_num]['url']
        header = eval(self.cases[case_num]['headers'])
        params = eval(self.cases[case_num]['params'])
        expected = self.cases[case_num]['expected']
        result = Request().post_request(Geturl, params, header)
        return self.ast.assert_code(result["code"], expected)


    def test_pass(self):
        case_num = "1"
        self.postBase(self.host, case_num)

    def test_name_fail(self):
        case_num = "2"
        self.postBase(self.host, case_num)

    def test_pwd_fail(self):
        case_num = "3"
        self.postBase(self.host, case_num)



