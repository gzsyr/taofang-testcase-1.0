# 新房详情页面
from test_case.base_test.test_base import TestBase


class TestNewHouseDetail(TestBase):
    """
    新房详情页用例，通过搜索的方式进入新房详情页
    """
    _house = "华侨城翡翠天域"

    def test_goto_housedetail(self):
        """
        进入新房详情页
        :return:
        """
        self.shouye.goto_search().action_search(self._house).select_search_result().screenshot()