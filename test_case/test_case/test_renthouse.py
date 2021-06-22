import allure
import pytest
from test_case.base_test.test_base import TestBase

class TestRentHouse(TestBase):

    """
    租房首页用例
    """

    @allure.description("租房首页点击搜索入口")
    def test_rent_house_search(self):
        """
        租房首页点击搜索入口
        :return:
        """
        self.rent_house_search().screenshot()
