import allure

from page_object.base_page.base_page import BasePage
from page_object.business.shopmalllist import ShopMallList
from page_object.community.communitylist import CommunityList
from page_object.housedoctor.housedoctormain import HouseDoctorMain
from page_object.housetour.housetour import HouseTour
from page_object.indexpage.buyingtools import BuyingTools
from page_object.indexpage.indexsearch import IndexSearch
from page_object.indexpage.selectcity import SelectCity
from page_object.maphouse.housemap import MapFindHouse
from page_object.newhouse.newhouselist import NewHouseList
from page_object.news.newslist import NewsList
from page_object.renthouse.renthouse import RentHouse
from page_object.sellhouse.checkhouseprice import CheckHousePrice
from page_object.sellhouse.publishindex import PublishIndex
from page_object.sellhouse.buyinghouse import BuyingHouse
from page_object.sellhouse.sellhouselist import SellHouseList
from page_object.minepage.minepage import MinePage


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

    # 功能入口第一屏，参数化------add by： zsy
    def goto_func_entrance_first(self, func_entry="新房"):
        """
        功能入口统一，参数化使用
        :param: func_entry功能入口的名称
        :return:
        """
        self._params["func_entry"] = func_entry
        with allure.step("点击功能入口：" + self._params["func_entry"]):
            self.steps("../../page_object/indexpage/main.yaml", replace=True)
        self.tsleep(1)
        if "找小区" == self._params["func_entry"]:
            return CommunityList(self._driver)
        if "购房工具" == self._params["func_entry"]:
            return BuyingTools(self._driver)
        if "新房" == self._params["func_entry"]:
            return NewHouseList(self._driver)
        if "看房团" == self._params["func_entry"]:
            return HouseTour(self._driver)
        else:
            return self

    # 以下是功能入口 , 暂时合并第一屏的代码------by： zsy
    def goto_func_entrance_newhouse(self):
        """
        点击:功能入口-新房
        :return:
        """
        self.goto_func_entrance_first("新房")
        return NewHouseList(self._driver)

    def goto_func_entrance_esf(self):
        """
        点击:功能入口-二手房
        :return:
        """
        self.goto_func_entrance_first("二手房")
        return SellHouseList(self._driver)

    def goto_func_entrance_zf(self):
        """
        点击:功能入口-租房
        :return:
        """
        self.goto_func_entrance_first("租房")
        return RentHouse(self._driver)

    def goto_func_entrance_spbg(self):
        """
        点击:功能入口-商铺办公
        :return:
        """
        # with allure.step("点击功能入口的商铺办公icon"):
        #     self.steps("../../page_object/indexpage/main.yaml")
        # self.tsleep(2)
        self.goto_func_entrance_first("商铺办公")
        return ShopMallList(self._driver)
    #
    # def goto_func_entrance_fyfb(self):
    #     """
    #     点击:功能入口-房源发布
    #     :return:
    #     """
    #     with allure.step("点击功能入口的房源发布icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    # def goto_func_entrance_gfgj(self):
    #     """
    #     点击:功能入口-购房工具
    #     :return:
    #     """
    #     with allure.step("点击功能入口的购房工具icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    # def goto_func_entrance_map(self):
    #     """
    #     点击:功能入口-地图
    #     :return:
    #     """
    #     with allure.step("点击功能入口的地图icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self

    # def goto_func_entrance_school_map(self):
    #     """
    #     点击:功能入口-学校地图
    #     :return:
    #     """
    #     with allure.step("点击功能入口的学校地图icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    def goto_func_entrance_check_price(self):
        """
        点击:功能入口-查房价
        :return:
        """
        self.goto_func_entrance_first("查房价")
        return CheckHousePrice(self._driver)
    #
    # def goto_func_entrance_find_community(self):
    #     """
    #     点击:功能入口-找小区
    #     :return:
    #     """
    #     with allure.step("点击功能入口的找小区icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self

    def goto_func_entrance_news(self):
        """
        点击:功能入口-房产资讯
        :return:
        """
        with allure.step("点击功能入口的房产资讯icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self
    #
    # def goto_func_entrance_group_house(self):
    #     """
    #     点击:功能入口-看房团
    #     :return:
    #     """
    #     with allure.step("点击功能入口的看房团icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    # def goto_func_entrance_live(self):
    #     """
    #     点击:功能入口-直播
    #     :return:
    #     """
    #     with allure.step("点击功能入口的直播icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    # def goto_func_entrance_video_house(self):
    #     """
    #     点击:功能入口-视频说房
    #     :return:
    #     """
    #     with allure.step("点击功能入口的视频说房icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self
    #
    # def goto_func_entrance_online_shop(self):
    #     """
    #     点击:功能入口-签到
    #     :return:
    #     """
    #     with allure.step("点击功能入口的签到icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self

    def goto_func_entrance_trade_process(self):
        """
        点击:功能入口-买房流程
        :return:
        """
        with allure.step("点击功能入口的买房流程icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_doctor(self):
        """
        点击:功能入口-房博士
        :return:
        """
        with allure.step("点击功能入口的房博士icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_calculator(self):
        """
        点击:功能入口-计算器
        :return:
        """
        with allure.step("点击功能入口的计算器icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_zhimai_list(self):
        """
        点击:功能入口-365直卖
        :return:
        """
        with allure.step("点击功能入口的365直卖icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_home_improvement(self):
        """
        点击:功能入口-家居
        :return:
        """
        with allure.step("点击功能入口的家居icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_want_buy(self):
        """
        点击:功能入口-求购
        :return:
        """
        with allure.step("点击功能入口的求购icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return BuyingHouse(self._driver)

    def goto_func_entrance_publish_sell(self):
        """
        点击:功能入口-我要卖房
        :return:
        """
        with allure.step("点击功能入口的我要卖房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return PublishIndex(self._driver)

    def goto_func_entrance_financial_service(self):
        """
        点击:功能入口-金融服务
        :return:
        """
        with allure.step("点击功能入口的金融服务icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_VR_list(self):
        """
        点击:功能入口-VR看房
        :return:
        """
        with allure.step("点击功能入口的VR看房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_pension_channel(self):
        """
        点击:功能入口-养老频道
        :return:
        """
        with allure.step("点击功能入口的养老频道icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_find_house(self):
        """
        点击:功能入口-求租
        :return:
        """
        with allure.step("点击功能入口的求租icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_publish_rent(self):
        """
        点击:功能入口-我要出租
        :return:
        """
        with allure.step("点击功能入口的我要出租icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    # def goto_func_entrance_lottery_query(self):
    #     """
    #     点击:功能入口-摇号查询
    #     :return:
    #     """
    #     with allure.step("点击功能入口的摇号查询icon"):
    #         self.steps("../../page_object/indexpage/main.yaml")
    #     self.tsleep(2)
    #     return self

    def func_entrance_swipe_left(self, pos_text=None):
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

    def goto_news_more(self):
        """
        点击淘房头条更多
        """
        with allure.step("点击淘房头条更多"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return NewsList(self._driver)

    def goto_news_live(self):
        """
        点击淘房头条更多
        """
        with allure.step("点击淘房头条更多"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_message(self):
        """
        点击：首页-消息
        """
        with allure.step("点击首页消息"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_city(self):
        """
        点击城市
        """
        with allure.step("点击城市"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return SelectCity(self._driver)

    def goto_search(self):
        """
        点击搜索框
        """
        with allure.step("点击搜索框"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return IndexSearch(self._driver)

    def goto_scan(self):
        """
        点击扫一扫
        """
        with allure.step("点击扫一扫"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_map(self):
        """
        点击地图
        """
        with allure.step("点击地图"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return MapFindHouse(self._driver)

    def goto_lpdt(self):
        """
        点击楼盘动态
        """
        with allure.step("点击楼盘动态"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_zmlp(self):
        """
        点击直卖楼盘
        """
        with allure.step("点击直卖楼盘"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_jqkp(self):
        """
        点击近期开盘
        """
        with allure.step("点击近期开盘"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def func_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/indexpage/main.yaml", replace=True)
        self.tsleep(2)
        return self

    def goto_find_newhouse_tab(self):
        """
        点击找新房
        """
        with allure.step("点击找新房"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_find_newhouse(self):
        """
        点击找新房马上找房
        """
        with allure.step("点击找新房马上找房"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_find_second_tab(self):
        """
        点击找二手房tab
        """
        with allure.step("点击二手房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_find_second(self):
        """
        点击找二手房马上找房
        """
        with allure.step("点击找二手房马上找房"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_find_rent_tab(self):
        """
        点击找租房tab
        """
        with allure.step("点击找租房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_find_rent(self):
        """
        点击找租房马上找房
        """
        with allure.step("点击找租房马上找房"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_my_house_tab(self):
        """
        点击我的房子tab
        """
        with allure.step("点击我的房子tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_my_house(self):
        """
        点击我的房子tab
        """
        with allure.step("点击我的房子tab房子"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_sell_house_tab(self):
        """
        点击帮你卖房
        """
        with allure.step("点击帮你卖房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_release_house(self):
        """
        点击帮你卖房发布房源
        """
        with allure.step("点击帮你卖房tab发布房源"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_live_house(self):
        """
        点击直播房源
        """
        with allure.step("点击直播房源"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_live_house_more(self):
        """
        点击直播房源查看更多
        """
        with allure.step("点击直播房源查看更多"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_price_evaluate(self):
        """
        点击房价评估
        """
        with allure.step("点击房价评估"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_second_price(self):
        """
        点击南京二手房均价
        """
        with allure.step("点击南京二手房均价"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_doctor_more(self):
        """
        点击房博士更多
        """
        with allure.step("点击房博士更多"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def swipe_live_left(self):
        """
        直播看房模块，左滑
        :return:
        """
        with allure.step("直播看房模块左滑"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_doctor_photo(self):
        """
        点击房博士头像
        """
        with allure.step("点击房博士头像"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_doctor_consult(self):
        """
        点击房博士咨询按钮
        """
        with allure.step("点击房博士咨询按钮"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_doctor_question(self):
        """
        点击房博士问答数据
        """
        with allure.step("点击房博士问答数据"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_doctor(self):
        """
        点击房博士tab
        """
        with allure.step("点击首页房博士tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return HouseDoctorMain(self._driver)

    def goto_find(self):
        """
        点击首页发现tab
        """
        with allure.step("点击首页发现tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_my(self):
        """
        点击首页我的tab
        """
        with allure.step("点击首页我的tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return MinePage(self._driver)

    def goto_newhouse_tab(self):
        """
        点击首页新房tab
        """
        with allure.step("点击首页新房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_tab_item(self, des="新房"):
        """
        点击首页新房tab、二手房tab、租房tab楼盘
        """
        with allure.step("点击首页" + des + "tab楼盘"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_second_tab(self):
        """
        点击首页二手房tab
        """
        with allure.step("点击首页二手房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_rent_tab(self):
        """
        点击首页租房tab
        """
        with allure.step("点击首页租房tab"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self
