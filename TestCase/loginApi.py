from Common.Request import Request


class LoginApi:

    @classmethod
    def pwdBase(self, host, case_num):
        Geturl = host + self.cases[case_num]['url']
        params = eval(self.cases[case_num]['params'])
        expected = self.cases[case_num]['expected']
        result = Request().post_request(Geturl, params)
        return self.ast.assert_code(result["code"], expected)



