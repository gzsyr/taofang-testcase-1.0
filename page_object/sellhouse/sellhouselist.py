from page_object.base_page.base_page import BasePage
import allure


class SellHouseList(BasePage):
    """
    二手房列表页面
    """

    def click_search_text(self):
        """
        点击列表搜索框
        :return:
        """
        with allure.step("点击列表页搜索框"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_map(self):
        """
        点击列表页地图
        :return:
        """
        with allure.step("点击列表页地图"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_msg(self):
        """
        点击列表页消息
        :return:
        """
        with allure.step("点击列表页消息"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_neighborhood(self):
        """
        点击列表页功能入口-找小区
        :return:
        """
        with allure.step("点击列表页功能入口-找小区"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_personal_housing(self):
        """
        点击列表页功能入口-个人房源
        :return:
        """
        with allure.step("点击列表页功能入口-个人房源"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_school_map(self):
        """
        点击列表页功能入口-学校地图
        :return:
        """
        with allure.step("点击列表页功能入口-学校地图"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_check_prices(self):
        """
        点击列表页功能入口-查房价
        :return:
        """
        with allure.step("点击列表页功能入口-查房价"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_buy_house(self):
        """
        点击列表页功能入口-我要买房
        :return:
        """
        with allure.step("点击列表页功能入口-我要买房"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_find_room(self):
        """
        点击列表页帮你找房icon
        :return:
        """
        with allure.step("点击列表页帮你找房icon"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_fast_selling(self):
        """
        点击列表页快速卖房icon
        :return:
        """
        with allure.step("点击列表页快速卖房icon"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_consultant(self):
        """
        点击列表页买房咨询师icon
        :return:
        """
        with allure.step("点击列表页买房咨询师icon"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_headlines(self):
        """
        点击列表页楼市头条
        :return:
        """
        with allure.step("点击列表页楼市头条"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_screening_location(self):
        """
        点击列表位置
        :return:
        """
        with allure.step("点击列表页位置"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

    def click_filter_position_menu(self, text="不限"):
        """
        点击筛选项“位置”的菜单
        :param text: 传入的需要点击的位置参数
                     默认不限
        :return:
        """
        self._params["filter_postion"] = text
        with allure.step("点击筛选项的“位置”的" + text):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml", replace=True)
        self.tsleep(2)

        return self

    def click_empty(self):
        """
        清空按钮
        :return:
        """
        with allure.step("点击清空按钮"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

