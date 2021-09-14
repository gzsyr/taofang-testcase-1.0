# -- by yfl
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 地图找房页面的测试")
class TestMapFindHouse(TestBase):
    """
    地图找房页面
    """
    @allure.description("新房搜索：万象天地四季")
    def test_newhouse_search(self):
        """
        新房搜索返回
        """
        self.shouye.goto_map().goto_search().screenshot()

    @allure.description("新房筛选：在售、30000-3500元/平米、住宅、精装修")
    def test_newhouse_filter(self):
        """
        新房筛选：在售、30000-3500元/平米、住宅、精装修
        """
        self.shouye.goto_map().show_select().select_filter_item('新盘').select_filter_item('30000-35000元/㎡').\
            func_swipe().select_filter_item('住宅').select_filter_item('精装修').confirm_filter().screenshot()

    @allure.description("新房地图-点击已筛选条件")
    def test_newhouse_filter_conditions(self):
        """
        点击已筛选条件
        """
        self.shouye.goto_map().show_filter_conditions().screenshot()

    @allure.description("新房地图-10号线-中胜站")
    def test_newhouse_filter_metro(self):
        """
        新房地图-10号线-中胜站
        """
        self.shouye.goto_map().show_metro().select_filter_item('十号线').select_filter_item('中胜站').screenshot()

    @allure.description("新房地图定位")
    def test_newhouse_location(self):
        """
        新房地图定位
        """
        self.shouye.goto_map().click_location().screenshot()

    @allure.description("新房地图-搜索万象天地四季-进入新房详情")
    def test_goto_newhouse_detail(self):
        """
        新房地图-搜索万象天地-进入新房详情
        """
        self.shouye.goto_map().goto_search().goto_housedetail().screenshot()

    @allure.description("点击二手房TAB")
    def test_switch_secondhouse(self):
        """
        切换二手房地图
        """
        self.shouye.goto_map().select_housetab('二手房').screenshot()

    @allure.description("二手房搜索：万达江南明珠")
    def test_secondhouse_search(self):
        """
        二手房搜索返回
        """
        self.shouye.goto_map().select_housetab('二手房').goto_search('万达江南明珠').screenshot()

    @allure.description("二手房筛选：200-250万、二室、精装")
    def test_secondhouse_filter(self):
        """
        二手房筛选：二手房筛选：200-250万、二室、精装
        """
        self.shouye.goto_map().select_housetab('二手房').show_select().select_filter_item('200-250万').\
            select_filter_item('二室').func_swipe().select_filter_item('精装').confirm_filter().screenshot()

    @allure.description("二手房地图-点击已筛选条件")
    def test_secondhouse_filter_conditions(self):
        """
        点击已筛选条件
        """
        self.shouye.goto_map().select_housetab('二手房').show_select().select_filter_item('200-250万').\
            select_filter_item('二室').func_swipe().select_filter_item('精装').confirm_filter().\
            show_filter_conditions().screenshot()

    @allure.description("二手房地图-1号线-中华门站")
    def test_secondhouse_filter_metro(self):
        """
        二手房地图-1号线-中华门站
        """
        self.shouye.goto_map().select_housetab('二手房').show_metro().select_filter_item('中华门站').screenshot()

    @allure.description("二手房地图-学校")
    def test_secondhouse_filter_school(self):
        """
        二手房地图-学校
        """
        self.shouye.goto_map().select_housetab('二手房').goto_schoolmap().screenshot()

    @allure.description("二手房地图定位")
    def test_secondhouse_location(self):
        """
        二手房地图定位
        """
        self.shouye.goto_map().select_housetab('二手房').click_location().screenshot()

    @allure.description("二手房地图-搜索万达江南明珠-进入小区详情")
    def test_goto_secondhouse_community(self):
        """
        二手房地图-搜索万达江南明珠-进入小区详情
        """
        self.shouye.goto_map().select_housetab('二手房').goto_search('万达江南明珠').goto_community().screenshot()

    @allure.description("二手房地图-搜索万达江南明珠-进入二手房详情")
    def test_goto_secondhouse_detail(self):
        """
        二手房地图-搜索万达江南明珠-进入二手房详情
        """
        self.shouye.goto_map().select_housetab('二手房').goto_search('万达江南明珠').goto_housedetail().screenshot()

    @allure.description("点击租房房TAB")
    def test_switch_renthouse(self):
        """
        切换租房地图
        """
        self.shouye.goto_map().select_housetab('租房').screenshot()

    @allure.description("租房搜索：万达江南明珠")
    def test_renthouse_search(self):
        """
        租房搜索返回
        """
        self.shouye.goto_map().select_housetab('租房').goto_search('万达江南明珠').screenshot()

    @allure.description("租房筛选：1000-1500元、中介、合租、精装")
    def test_renthouse_filter(self):
        """
        租房筛选：1000-1500元、中介、合租、精装
        """
        self.shouye.goto_map().select_housetab('租房').show_select().select_filter_item('1000-1500元'). \
            select_filter_item('中介').select_filter_item('合租').func_swipe().select_filter_item('精装').\
            confirm_filter().screenshot()

    @allure.description("租房地图-点击已筛选条件")
    def test_renthouse_filter_conditions(self):
        """
        点击已筛选条件
        """
        self.shouye.goto_map().select_housetab('租房').show_select().select_filter_item('1000-1500元'). \
            select_filter_item('中介').select_filter_item('合租').func_swipe().select_filter_item('精装').confirm_filter(). \
            show_filter_conditions().screenshot()

    @allure.description("租房地图-1号线-中华门站")
    def test_renthouse_filter_metro(self):
        """
        租房地图-1号线-中华门站
        """
        self.shouye.goto_map().select_housetab('租房').show_metro().select_filter_item('中华门站').screenshot()

    @allure.description("租房地图定位")
    def test_renthouse_location(self):
        """
        租房地图定位
        """
        self.shouye.goto_map().select_housetab('租房').click_location().screenshot()

    @allure.description("租房地图-搜索万达江南明珠-进入小区详情")
    def test_goto_renthouse_community(self):
        """
        租房地图-搜索万达江南明珠-进入小区详情
        """
        self.shouye.goto_map().select_housetab('租房').goto_search('万达江南明珠').goto_community().screenshot()

    @allure.description("租房地图-搜索万达江南明珠-进入租房详情")
    def test_goto_renthouse_detail(self):
        """
        租房地图-搜索万达江南明珠-进入租房详情
        """
        self.shouye.goto_map().select_housetab('租房').goto_search('万达江南明珠').goto_housedetail().screenshot()
