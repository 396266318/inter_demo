# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  15:43
@author: xuanyue
@file: run_task.py
"""
import sys
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests
import xmlrunner
from os.path import dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))
BASE_PATH = BASE_DIR.replace("\\", "/")
sys.path.append(BASE_PATH)

print("运行测试文件:", BASE_PATH)

# 定义扩展的目录
EXTEND_DIR = BASE_PATH + "/testtask_app/extend/"


@ddt
class InterfaceTest(unittest.TestCase):
    @unpack
    @file_data("test_data_list.json")
    def test_run_cases(self, url, method, header, parameter_type, parameter_body, assert_type, assert_text):
        if header == "{}":
            header_dict = {}
        else:
            header_dict = json.loads(header.replace("\'", "\""))

        if parameter_body == "{}":
            parameter_dict = {}
        else:
            parameter_dict = json.loads(parameter_body.replace("\'", "\""))

        if method == "get":
            if parameter_type == "from":
                r = requests.get(url, headers=header_dict, params=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)
        if method == "post":
            if parameter_type == "from":
                r = requests.post(url, headers=header_dict, data=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertIn(assert_text, r.text)

            elif parameter_type == "json":
                r = requests.post(url, headers=header_dict, json=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)  # 断言 r.text 是否等于 assert_text
            else:
                raise NameError("参数类型错误")


def run_cases():
    """运行测试用例"""
    with open(EXTEND_DIR + 'results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False
        )


if __name__ == "__main__":
    run_cases()