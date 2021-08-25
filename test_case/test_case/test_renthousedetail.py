# -- by yfl
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房房源详情页面的测试")
class TestRentHouseDetail(TestBase):
    """
    租房房源详情用例
    """
    def goto_renthoustdetail(self):
        """
        进入整租、中介、住宅筛选的第一个租房房源详情
        """
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("整租").\
            click_filter_more().click_filter_position_menu("中介").\
            click_filter_position_menu("住宅").click_definite().goto_renthouse_detail()

    @allure.description("点击租房房源详情页返回按钮")
    def test_click_renthouse_detail_back(self):
        """
        点击租房房源详情返回按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_back().screenshot()

    @allure.description("点击租房房源详情页分享按钮")
    def test_click_renthouse_detail_share(self):
        """
        点击租房房源详情分享按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_share().screenshot()

    @allure.description("点击租房房源详情页收藏按钮")
    def test_click_renthouse_detail_fav(self):
        """
        点击租房房源详情收藏按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_fav().screenshot()

    @allure.description("点击租房房源详情页右上角IM咨询按钮")
    def test_click_renthouse_detail_msg(self):
        """
        点击租房房源详情右上角IM咨询按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_msg().screenshot()

    @allure.description("进入租房房源详情页相册")
    def test_click_renthouse_detail_photo(self):
        """
        点击租房房源详情图片
        """
        self.goto_renthoustdetail().click_renthouse_detail_photo().screenshot()

    @allure.description("点击租房房源详情页租金咨询")
    def test_click_renthouse_detail_im_price(self):
        """
        点击租房房源详情租金咨询
        """
        self.goto_renthoustdetail().click_renthouse_detail_im_price().screenshot()

    @allure.description("进入租房房源详情页所属小区")
    def test_click_renthouse_detail_block(self):
        """
        点击租房房源详情所属小区
        """
        self.goto_renthoustdetail().click_renthouse_detail_block().screenshot()

    @allure.description("点击租房房源详情页预约看房IM")
    def test_click_renthouse_detail_im_lookhouse(self):
        """
        点击租房房源详情预约看房IM
        """
        self.goto_renthoustdetail().func_swipe("举报").click_renthouse_detail_im_lookhouse().\
            click_renthouse_detail_im_lookhouse().screenshot()

    @allure.description("展开租房房源详情页房源描述")
    def test_show_renthouse_detail_desc_more(self):
        """
        点击租房房源详情页房源描述展开按钮
        """
        self.goto_renthoustdetail().func_swipe("举报").show_renthouse_detail_desc_more().screenshot()

    @allure.description("点击租房房源详情页咨询详情IM")
    def test_click_renthouse_detail_im_desc(self):
        """
        点击租房房源详情咨询详情IM
        """
        self.goto_renthoustdetail().func_swipe("举报").click_renthouse_detail_im_desc().\
            click_renthouse_detail_im_desc().screenshot()

    @allure.description("点击租房房源详情页举报按钮")
    def test_click_renthouse_detail_report(self):
        """
        点击租房房源详情举报
        """
        self.goto_renthoustdetail().func_swipe("同小区房源").click_renthouse_detail_report().screenshot()

    @allure.description("点击租房房源详情页悬浮提问按钮")
    def test_click_renthouse_detail_im_question(self):
        """
        点击租房房源详情悬浮提问按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_im_question().screenshot()

    @allure.description("点击租房房源详情页小区地图")
    def test_click_renthouse_detail_map(self):
        """
        点击租房房源详情小区地图
        """
        self.goto_renthoustdetail().func_swipe("同小区房源").click_renthouse_detail_map().screenshot()

    @allure.description("展开租房房源详情页周边配套")
    def test_show_renthouse_detail_facilities(self):
        """
        展开租房房源详情页周边配套
        """
        self.goto_renthoustdetail().func_swipe("同小区房源").show_renthouse_detail_facilities().screenshot()

    @allure.description("进入租房房源详情页同小区房源全部列表")
    def test_click_renthouse_detail_list_more(self):
        """
        进入租房房源详情页同小区房源全部列表
        """
        self.goto_renthoustdetail().func_swipe("buttom").click_renthouse_detail_list_more().screenshot()

    @allure.description("点击租房房源详情页同小区房源第一个房源")
    def test_click_renthouse_detail_other(self):
        """
        点击租房房源详情页同小区房源第一个房源
        """
        self.goto_renthoustdetail().func_swipe("buttom").click_renthouse_detail_other().screenshot()

    @allure.description("跳转租房房源详情页顶部")
    def test_click_renthouse_detail_to_top(self):
        """
        租房房源详情置顶按钮
        """
        self.goto_renthoustdetail().func_swipe("buttom").click_renthouse_detail_top().screenshot()

    @allure.description("点击租房房源详情页经纪人头像")
    def test_click_renthouse_detail_business(self):
        """
        点击租房房源详情经纪人头像
        """
        self.goto_renthoustdetail().click_renthouse_detail_business().screenshot()

    @allure.description("点击租房房源详情页电话咨询按钮")
    def test_click_renthouse_detail_call(self):
        """
        点击租房房源详情页电话咨询按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_call().screenshot()

    @allure.description("点击租房房源详情页在线咨询按钮")
    def test_click_renthouse_detail_im(self):
        """
        点击租房房源详情在线咨询按钮
        """
        self.goto_renthoustdetail().click_renthouse_detail_im().screenshot()
