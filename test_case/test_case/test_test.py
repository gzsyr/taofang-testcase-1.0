import subprocess
from turtle import forward, left
from typing import Union, Dict

import pytest
import allure
import os

from test_case.base_test.test_base import TestBase
from test_case.test_case.test_test_base import TB


@allure.description("teswt")
def test_0001():
    print("0001")

def test_0002():
    a = {'usr': 'my', 'psw': 123455}
    if 'value' in a.keys():
        print("have value")
    else:
        print("no value")

def test_002():
    a = 'abc'
    c = '235435t'
    if a not in c:
        print("not in")
    else:
        print("in")

class TestC(TB):

    def test_001(self):
        # self._params["type"] = "我的"
        print(self._params["type"])
        print("test_001")

    def test_002(self):
        self._params["type"] = "ceshi"
        print(self._params["type"])
        print("test_002")

    def setup_class(self):
        self._params["type"] = "setu的时候"
        print("TestC-setup_class")

    def teardown_class(self):
        print(self._params["type"])
        print("TestC-teardown_class")

def test_get_device():
    # name = os.system("adb devices").
    # name = subprocess.check_output("adb devices")
    # print(type(name))
    # print("原始输出：")
    # print(name)
    # n = name.split(str.encode("\r\n"))
    # print("转化为列表：")
    # print(n)
    # d = n[1]
    # print("取第二个devices：")
    # print(type(d))
    # print(d)
    # dd = d.split(str.encode("\t"))
    # print("devices转化为列表：")
    # print(dd)
    # device = dd[0]
    # print("devices的名字")
    # print(device.decode("UTF-8"))

    print("直接获取：")
    name = subprocess.check_output("adb devices").split(str.encode("\r\n"))[1].split(str.encode("\t"))[0].decode("UTF-8")
    print(name)

    aa = "adb -P 5037 -s " + name + " shell getprop ro.build.version.release"
    print(aa)
    version = subprocess.check_output(aa).split(str.encode("\r\n"))[0].decode("UTF-8")
    print(version)


# def find(by: str = 'by', value: Union[str, Dict] = None):
def find(by: str='by', value: str = None):
    print("this is find")
    print(by)
    print(value)

def test_01():
    loc = tuple(('abc', 'lalala'))

    if isinstance(loc, tuple):
        find(*loc)
    else:
        print("no tuple")


def test_02():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)


class Test000(TestBase):

    def test_0001(self):
        print("OK!----0001")

    def test_0002(self):
        print("OK!----0002")
