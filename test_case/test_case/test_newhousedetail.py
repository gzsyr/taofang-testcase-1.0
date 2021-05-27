# 新房详情页面
import allure

from test_case.base_test.test_base import TestBase


class TestNewHouseDetail(TestBase):
    """
    新房详情页用例，通过搜索的方式进入新房详情页
    """
    _house = "华侨城翡翠天域"

    def goto_housedetail(self):
        """
        进入新房详情页
        :return:
        """
        return self.shouye.goto_search().action_search(self._house).select_search_result()

    @allure.description("点击新房详情页相册")
    def test_click_photo(self):
        """
        点击相册
        :return:
        """
        pass

    @allure.description("点击新房详情页“查看更多”")
    def test_click_photo_more(self):
        """
        点击相册的“查看更多”
        :return:
        """
        # self.goto_housedetail().goto_photo().screenshot()
        pass

