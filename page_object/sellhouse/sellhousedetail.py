import allure

from page_object.base_page.base_page import BasePage


class SellHouseDetail(BasePage):
    """
    二手房详情页面
    """

    def click_sellhouse_detail_action_share(self):
        """
        点击二手房详情页分享按钮
        """
        with allure.step(""):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_action_fav(self):
        """
        点击二手房详情页收藏按钮
        """
        with allure.step("点击二手房详情页收藏按钮"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_iv_msg(self):
        """
        点击二手房详情页消息按钮
        """
        with allure.step("点击二手房详情页消息按钮"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_numindicator(self):
        """
        点击二手房详情页相册按钮
        """
        with allure.step("点击二手房详情页相册按钮"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_loan(self):
        """
        点击二手房详情页房贷计算器按钮
        """
        with allure.step("点击二手房详情页房贷计算器按钮"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_house_down_payment(self):
        """
        点击首付及月供咨询?
        """
        with allure.step("点击首付及月供咨询?"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_image_view(self):
        """
        点击所属小区右侧箭头
        """
        with allure.step("点击所属小区右侧箭头"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_school(self):
        """
        点击学校
        """
        with allure.step(""):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_fang_bo_shi(self):
        """
        点击二手房买卖有疑问右侧箭头
        """
        with allure.step("点击二手房买卖有疑问右侧箭头"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_fyms_bt_more_ico(self):
        """
        点击房源描述向下的箭头
        """
        with allure.step("点击房源描述向下的箭头"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_report(self):
        """
        点击举报
        """
        with allure.step("点击举报"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_wanna_assess(self):
        """
        点击房价评估
        """
        with allure.step("点击房价评估"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_map_image(self):
        """
        点击小区地址的地图
        """
        with allure.step("点击小区地址的地图"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_xqdzdt_more_ico(self):
        """
        点击小区地址地图下方的向下箭头
        """
        with allure.step("点击小区地址地图下方的向下箭头"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_house_sell_count(self):
        """
        点击同小区房源右边的“全部”
        """
        with allure.step("点击同小区房源右边的全部"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_appointment(self):
        """
        点击悬浮-预约看房
        """
        with allure.step("点击悬浮-预约看房"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_ll_arrow(self):
        """
        点击悬浮-提问
        """
        with allure.step("点击悬浮-提问"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_person_photo(self):
        """
        点击经纪人头像
        """
        with allure.step("点击经纪人头像"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_call_business_novrdk(self):
        """
        点击电话咨询
        """
        with allure.step("点击电话咨询"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
        self.tsleep(2)
        return self

    def click_sellhouse_detail_im_business_novrdk(self):
        """
        点击在线咨询
        """
        with allure.step("点击电话咨询"):
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml")
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
            self.steps("../../page_object/sellhouse/sellhousedetail.yaml", replace=True)
        self.tsleep(2)
        return self



