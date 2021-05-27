# 新房详情页面
from test_case.base_test.test_base import TestBase


class TestNewHouseDetail(TestBase):
    """
    新房详情页用例
    """
    _house = "万科翡翠天域"

    def test_goto_housedetail(self):
        """
        进入新房详情页
        :return:
        """