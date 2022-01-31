from Common.Assert import Assertions
from Common.Config import Config
from Common.Log import MyLog
import os
from Common.ReadExcel import get_cases
from Common.Request import Request
from Params.params import GetParameter
import json

from TestCase.loginApi import LoginApi

if __name__ == '__main__':
    data = GetParameter('fantuanReviews').get_params()
    env = Config().get_conf('comm', 'env')
    host = Config().get_conf(env, 'host')
    log = MyLog()
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\Params\\Param\\Excel\\case.xlsx'
    cases = get_cases(filepath, "点评测试")
    ast = Assertions()
    case_num = "1"
    Geturl = host + cases[case_num]['url']
    params = eval(cases[case_num]['params'])
    expected = cases[case_num]['expected']
    result = Request().post_request(Geturl, params)



    # log = MyLog()
    # Geturl = host + data[1]['url']
    # params = data[1]['data']
    # hearder = data[1]['header']
    # rq = Request()
    # r1 = rq.post_request(Geturl,params)
    # print(r1)


    # filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\Params\\Param\\Excel\\case.xlsx'
    # result = get_cases(filepath,"点评测试")
    # #result = sss.json()
    # print(result)
    # print(result["1"]["name"])
    # case_num = "1"
    # Geturl = host + result[case_num]['url']
    # print(Geturl)
    # params = eval(result[case_num]['params'])
    # print(params)
    # expected = result[case_num]['expected']
    # print(expected)
    #
    # r1 = Request().post_request(Geturl, params)
    # print(r1["code"])
    #
    # case_num ="2"
    # params = eval(result[case_num]['params'])
    # r2 = Request().post_request(Geturl, params)
    # print(r2)


