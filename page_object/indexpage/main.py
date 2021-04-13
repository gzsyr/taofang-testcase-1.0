import allure

from page_object.base_page.base_page import BasePage
from page_object.newhouse.newhouselist import NewHouseList


class Main(BasePage):
    """
    首页，各点击入口
    """



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