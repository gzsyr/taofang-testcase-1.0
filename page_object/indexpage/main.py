import allure

from page_object.base_page.base_page import BasePage
from page_object.newhouse.newhouselist import NewHouseList


class Main(BasePage):
    """
    首页，各点击入口
    """
    def cancel_update(self):
        """
        取消更新的提示框
        :return:
        """
        with allure.step("更新弹框的按钮，点击取消更新"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def cancel_index_adv(self):
        """
        取消首页大屏广告
        :return:
        """
        with allure.step("关闭首页大屏广告"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self


    #以下是功能入口
    def goto_func_entrance_newhouse(self):
        """
        点击:功能入口-新房
        :return:
        """
        with allure.step("点击功能入口的新房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return NewHouseList(self._driver)

    def goto_func_entrance_esf(self):
        """
        点击:功能入口-二手房
        :return:
        """
        with allure.step("点击功能入口的二手房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_zf(self):
        """
        点击:功能入口-租房
        :return:
        """
        with allure.step("点击功能入口的租房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_spbg(self):
        """
        点击:功能入口-商铺办公
        :return:
        """
        with allure.step("点击功能入口的商铺办公icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_fyfb(self):
        """
        点击:功能入口-房源发布
        :return:
        """
        with allure.step("点击功能入口的房源发布icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_gfgj(self):
        """
        点击:功能入口-购房工具
        :return:
        """
        with allure.step("点击功能入口的购房工具icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_map(self):
        """
        点击:功能入口-地图
        :return:
        """
        with allure.step("点击功能入口的地图icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_school_map(self):
        """
        点击:功能入口-学校地图
        :return:
        """
        with allure.step("点击功能入口的学校地图icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_check_price(self):
        """
        点击:功能入口-查房价
        :return:
        """
        with allure.step("点击功能入口的查房价icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_find_community(self):
        """
        点击:功能入口-找小区
        :return:
        """
        with allure.step("点击功能入口的找小区icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_trade_process(self):
        """
        点击：功能入口-第二屏-买房流程
        :return:
        """
        with allure.step("点击功能入口的买房流程icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_find_house(self):
        """
        点击：功能入口-第三屏-求租
        :return:
        """
        with allure.step("点击功能入口的求租icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def func_entrance_swape_left(self, pos_text=None):
        """
        作为功能入口的左滑，滑到下一屏
        :param text: 起点位置的文字
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("点住" + self._params["pos_text"] + "向左滑动到下一屏"):
            self.steps("../../page_object/indexpage/main.yaml", replace=True)
        self.tsleep(2)
        return self

