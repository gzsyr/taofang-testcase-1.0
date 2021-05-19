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
    # 以下是功能入口
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
        return

    def goto_func_entrance_news(self):
        """
        点击:功能入口-房产资讯
        :return:
        """
        with allure.step("点击功能入口的房产资讯icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_group_house(self):
        """
        点击:功能入口-看房团
        :return:
        """
        with allure.step("点击功能入口的看房团icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_live(self):
        """
        点击:功能入口-直播
        :return:
        """
        with allure.step("点击功能入口的直播icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_video_house(self):
        """
        点击:功能入口-视频说房
        :return:
        """
        with allure.step("点击功能入口的视频说房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

    def goto_func_entrance_online_shop(self):
        """
        点击:功能入口-签到
        :return:
        """
        with allure.step("点击功能入口的签到icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

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
        return self

    def goto_func_entrance_publish_sell(self):
        """
        点击:功能入口-我要卖房
        :return:
        """
        with allure.step("点击功能入口的我要卖房icon"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

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

    def goto_func_entrance_lottery_query(self):
        """
        点击:功能入口-摇号查询
        :return:
        """
        with allure.step("点击功能入口的摇号查询icon"):
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

    def func_entrance_swipe(self, pos_text=None):
        """
        滑动到pos_text的位置
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step(self._params["pos_text"] + "com.house365.newhouse:id/m_title"):
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
        return self

    def goto_search(self):
        """
        点击搜索框
        """
        with allure.step("点击搜索框"):
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return self

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
        return self




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


