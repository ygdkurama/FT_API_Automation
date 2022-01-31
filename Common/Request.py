# -*- coding: utf-8 -*-

"""
封装request

"""

import os
import random
import requests
import Common.Consts
import json



class Request:

    def __init__(self):
        self.req = requests.session()

    def get_request(self, url, data=None, header=None, **kwargs):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            response = self.req.get(url=url, params=data, headers=header, **kwargs)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)
        result = json.loads(response.content)
        # response_dicts = dict()
        # response_dicts['code'] = response.status_code
        # response_dicts['headers'] = response.headers
        # response_dicts['cookies'] = response.cookies
        # try:
        #     response_dicts['body'] = response.json()
        # except Exception as e:
        #     print(e, ': Response is not json format, please use response.text() instead of respone.json()')
        #     response_dicts['body'] = ''
        # response_dicts['text'] = response.text
        # response_dicts['time_consuming'] = time_consuming
        # response_dicts['time_total'] = time_total

        return result

    def post_request(self, url, data=None, header=None, **kwargs):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        try:

            response = self.req.post(url=url, data=data, headers=header, **kwargs)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)
        result = response.json()
        # response_dicts = dict()
        # response_dicts['code'] = response.status_code
        # response_dicts['headers'] = response.headers
        # response_dicts['cookies'] = response.cookies
        # try:
        #     response_dicts['body'] = response.text
        # except Exception as e:
        #     print(e, ': Response is not json format, please use response.text() instead of respone.json()')
        #     response_dicts['body'] = ''
        #
        # response_dicts['text'] = response.text
        # response_dicts['time_consuming'] = time_consuming
        # response_dicts['time_total'] = time_total

        return result

    def post_request_multipart(self, url, data, header, file_parm, file, f_type, **kwargs):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = self.req.post(url=url, headers=header, **kwargs)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = self.req.post(url=url, data=data, headers=header, **kwargs)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['headers'] = response.headers
        response_dicts['cookies'] = response.cookies
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e, ': Response is not json format, please use response.text() instead of respone.json()')
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data=None, header=None, **kwargs):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            response = self.req.put(url=url, data=data, headers=header, **kwargs)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['headers'] = response.headers
        response_dicts['cookies'] = response.cookies
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e, ': Response is not json format, please use response.text() instead of respone.json()')
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
