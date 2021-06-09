import allure

from test_case.base_test.test_base import TestBase


class TestPublishHouse(TestBase):
    """
    发布房源相关测试用例
    """
    def goto_publish_sell(self):
        """
        首页功能入口竟然我要卖房页面
        """
        return self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_publish_sell()

    @allure.description("点击引导页的发布房源按钮")
    def test_click_publish(self):
        """
        点击引导页的发布房源按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().screenshot()

    @allure.description("点击引导页的帮助按钮")
    def test_click_help(self):
        """
        点击引导页的帮助按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_help().screenshot()

    @allure.description("点击引导页的服务按钮")
    def test_click_service(self):
        """
        点击引导页的服务按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_service().screenshot()

    @allure.description("点击引导页的评估房价按钮")
    def test_click_pinggu_img(self):
        """
        点击引导页的评估房价按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_pinggu_img().screenshot()

    @allure.description("点击引导页的学校地图按钮")
    def test_click_xuequ_img(self):
        """
        点击引导页的学校地图按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_xuequ_img().screenshot()

    @allure.description("点击引导页的房贷计算器按钮")
    def test_click_jisuanqi_img(self):
        """
        点击引导页的房贷计算器按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_jisuanqi_img().screenshot()

    @allure.description("点击出售发布页的重置按钮")
    def test_click_reset(self):
        """
        点击重置按钮
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().click_publishhouse_reset().screenshot()

    @allure.description("选择物业类型-住宅")
    def test_publish_type(self):
        """
        选择物业类型-住宅
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().\
            click_publishhouse_type().select_pubilshhouse_type(house_item="物业类型", house_type="住宅").screenshot()

    @allure.description("点击小区名称-搜索-万科红郡住宅")
    def test_publish_name(self):
        """
        点击小区名称-搜索-万科红郡住宅
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().\
            click_publishhouse_name().send_publishhouse_name_search("万科红郡住宅").\
            select_publishhouse_name_result().screenshot()

    @allure.description("输入楼栋：5栋")
    def test_publish_building(self):
        """
        输入楼栋
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_dong("5").screenshot()

    @allure.description("输入单元：1单元")
    def test_publish_unit(self):
        """
        输入单元
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_danyuan("5").screenshot()

    @allure.description("输入室：1006室")
    def test_publish_room(self):
        """
        输入室
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_shi("1006").screenshot()

    @allure.description("输入售价：400万元")
    def test_publish_price(self):
        """
        输入期望售价
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_price("400").screenshot()

    @allure.description("输入面积：116平")
    def test_publish_area(self):
        """
        输入面积
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_area("116").screenshot()

    @allure.description("房屋权属-产权房")
    def test_publish_property(self):
        """
        选择房屋权属
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().click_publishhouse_property().\
            select_pubilshhouse_type(house_item="房屋权属", house_type="产权房").screenshot()

    @allure.description("输入称呼：李女士")
    def test_publish_seller(self):
        """
        输入出售人名称
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().send_publishhouse_seller("李女士").screenshot()

    @allure.description("点击出售房源下一步，进入更多资料页")
    def test_publish_more(self):
        """
        点击出售房源下一步，进入更多资料页
        :return:
        """
        step1 = self.goto_publish_sell().click_publishindex_m_publish().goto_next_all()
        step1.screenshot()
        step2 = step1.click_publishhouse_next()
        step2.screenshot()

    @allure.description("更多资料页选择户型")
    def test_publish_layout(self):
        """
        更多资料页选择户型
        :return:
        """
        self.goto_publish_sell().click_publishindex_m_publish().goto_next_all().click_publishhouse_next().\
            click_publishhouse_room().click_publishhouse_confirm().screenshot()

