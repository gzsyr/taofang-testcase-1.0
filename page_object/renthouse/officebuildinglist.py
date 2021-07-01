import allure

from page_object.base_page.base_page import BasePage
from page_object.renthouse.officebuildingdetail import OfficeBuildingDetail


class OfficeBuildingList(BasePage):
    """
    写字楼页面
    """
    def click_officehouse_search(self):
        """
        点击搜索框
        :return:
        """
        with allure.step("点击搜索框"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return self

    def goto_message(self):
        """
        点击IM消息
        :return:
        """
        with allure.step("点击IM消息"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance(self, text="租写字楼"):
        """
        点击功能入口
        :param text: 传入的需要点击的text
        :return:
        """
        self._params["func_entry"] = text
        with allure.step("点击功能入口"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml", replace=True)
        self.tsleep(2)
        return self

    def goto_office_position(self):
        """
        点击大家都在搜
        :return:
        """
        with allure.step("点击大家都在搜区域名称"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return self

    def goto_office_hotlist(self):
        """
        点击热门楼盘-查看全部
        :return:
        """
        with allure.step("点击热门楼盘-查看全部"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return self

    def goto_office_hotdetail(self):
        """
        点击热门楼盘第一个楼盘，进入详情
        :return:
        """
        with allure.step("点击热门楼盘第一个楼盘，进入详情"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return self

    def goto_office_recommenddetail(self):
        """
        点击推荐楼盘第一个楼盘，进入详情
        :return:
        """
        with allure.step("点击推荐楼盘第一个楼盘，进入详情"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml")
        self.tsleep(2)
        return OfficeBuildingDetail(self._driver)

    def func_swipe(self, text):
        """
        上滑页面
        :param text:滑动到出现元素为止
        """
        self._params["pos_text"] = text
        with allure.step("点击大家都在搜区域名称"):
            self.steps("../../page_object/renthouse/officebuildinglist.yaml", replace=True)
        self.tsleep(2)
        return self
