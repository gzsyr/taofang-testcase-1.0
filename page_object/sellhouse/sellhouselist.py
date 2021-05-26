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

    def click_filter_position_menu(self, text="不限"):
        """
        点击筛选项的菜单
        :param text: 传入的需要点击的位置参数
                     默认不限
        :return:
        """
        self._params["filter_postion"] = text
        with allure.step("点击筛选项的“位置”的" + text):
            self.steps("../../page_object/newhouse/newhouselist.yaml", replace=True)
        self.tsleep(2)

    def click_filter_price(self):
        """
        二手房列表筛选-总价
        :return:
        """
        with allure.step("二手房列表筛选-总价"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self



    def click_filter_lowest_price(self):
        """
        点击二手房列表筛选-总价-自定义：最低价
        :return:
        """
        with allure.step("点击二手房列表筛选-总价-自定义：最低价"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self


    def click_filter_highest_price(self):
        """
        点击二手房列表筛选-总价-自定义：最高价
        :return:
        """
        with allure.step("点击二手房列表筛选-总价-自定义：最高价"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_confirm(self):
        """
        点击筛选页确定按钮
        :return:
        """
        with allure.step("点击筛选页确定按钮"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self



    def click_filter_room(self):
        """
        点击二手房列表筛选-房型
        :return:
        """
        with allure.step("点击二手房列表筛选-房型"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self



    def click_filter_more(self):
        """
        点击筛选-更多
        :return:
        """
        with allure.step("点击筛选-更多"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self

    def click_filter_reset(self):
        """
        点击筛选-更多-重置
        :return:
        """
        with allure.step("点击筛选-更多-重置"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self




    def click_filter_sort(self):
        """
        点击筛选-排序
        :return:
        """
        with allure.step("点击筛选-排序"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self



    def click_north(self):
        """
        点击标签筛选-南北通透
        :return:
        """
        with allure.step("点击标签筛选-南北通透"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self


    def click_vr_see(self):
        """
        点击标签筛选-VR带看
        :return:
        """
        with allure.step("点击标签筛选-VR带看"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self



    def click_mediation(self):
        """
        点击标签筛选-中介
        :return:
        """
        with allure.step("点击标签筛选-中介"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self


    def click_personal(self):
        """
        点击标签筛选-个人
        :return:
        """
        with allure.step("点击标签筛选-个人"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self

    def click_office_buildings(self):
        """
        点击标签筛选-写字楼
        :return:
        """
        with allure.step("点击标签筛选-写字楼"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)
        return self

    def goto_sellhouse_detail(self):
        """
        点击列表项第一个房源
        :return:
        """
        with allure.step("点击列表项第一个房源"):
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


    def click_empty(self):
        """
        清空按钮
        :return:
        """
        with allure.step("点击清空按钮"):
            self.steps("../../page_object/sellhouse/sellhouselist.yaml")
        self.tsleep(2)

        return self

