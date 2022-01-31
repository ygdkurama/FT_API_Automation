import allure
import pytest

from Common.Assert import Assertions
from Common.Config import Config
from Common.Log import MyLog
from Common.Request import Request
from Params.params import GetParameter


@allure.feature('chopOrder')
class TestFantuanReviews:
    data = GetParameter('fantuanReviews').get_params()
    env = Config().get_conf('comm', 'env')
    host = Config().get_conf(env, 'host')
    log = MyLog()
    rq = Request()
    ast = Assertions()



    @allure.step('得到Token')
    def test_gettoken(self):
        case_num = 1
        Geturl = self.host + self.data[case_num]['url']
        params = self.data[case_num]['data']
        params['unionId'] = "oorAnwyz6RKEpj5zhmbMkxWSPqmY"
        r1 = self.rq.post_request(Geturl, params)
        TestFantuanReviews.token = r1["user"]["loginToken"]
        self.ast.assert_code(r1['code'], 1)
        print(r1)
        print(r1["user"]["loginToken"])
        print(self.token+"sdddd")

    @allure.step('订单砍价')
    def test_chop(self):
        case_num = 2
        Geturl = self.host + self.data[case_num]['url']
        params = self.data[case_num]['data']
        header = self.data[case_num]['header']
        header['token'] = self.token
        r2 = self.rq.post_request(Geturl,params,header)
        self.ast.assert_text(r2["msg"],'非待支付订单，无法继续砍价。')
        print(r2)


if __name__ == '__main__':

    pytest.main()


