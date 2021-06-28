import allure

from page_object.base_page.base_page import BasePage


class RentHouseDetail(BasePage):
    """
    租房房源详情页面
    """
    def click_renthouse_detail_back(self):
        """
        点击租房房源详情返回按钮
        :return:
        """
        with allure.step("点击租房房源详情返回按钮"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_share(self):
        """
        点击租房房源详情返回按钮
        :return:
        """
        with allure.step("点击租房房源详情返回按钮"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_fav(self):
        """
        点击租房房源详情收藏按钮
        :return:
        """
        with allure.step("点击租房房源详情收藏按钮"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_msg(self):
        """
        点击租房房源详情IM按钮
        :return:
        """
        with allure.step("点击租房房源详情IM消息按钮"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_photo(self):
        """
        点击租房房源详情相册
        :return:
        """
        with allure.step("点击租房房源详情相册"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_im_price(self):
        """
        点击租房房源详情IM咨询租金
        :return:
        """
        with allure.step("点击租房房源详情租金IM咨询"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_block(self):
        """
        点击租房房源详情所属小区
        :return:
        """
        with allure.step("点击租房房源详情所属小区"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_im_lookhouse(self):
        """
        点击租房房源详情预约看房IM
        :return:
        """
        with allure.step("点击租房房源详情预约看房IM"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def show_renthouse_detail_desc_more(self):
        """
        点击租房房源详情描述更多
        :return:
        """
        with allure.step("点击租房房源详情描述展开更多"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_im_desc(self):
        """
        点击租房房源详情IM咨询详情
        :return:
        """
        with allure.step("点击租房房源详情IM咨询详情"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_im_question(self):
        """
        点击租房房源详情提问IM
        :return:
        """
        with allure.step("点击租房房源详情悬浮提问IM"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_report(self):
        """
        点击租房房源详情举报
        :return:
        """
        with allure.step("点击租房房源详情举报"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_map(self):
        """
        点击租房房源详情小区地图
        :return:
        """
        with allure.step("点击租房房源详情小区地图"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def show_renthouse_detail_facilities(self):
        """
        展开租房房源详情配套设施
        :return:
        """
        with allure.step("展开租房房源详情配套设施"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_list_more(self):
        """
        点击租房房源详情同小区全部房源列表
        :return:
        """
        with allure.step("点击租房房源详情同小区全部房源列表"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_other(self):
        """
        点击租房房源详情其他同小区房源
        :return:
        """
        with allure.step("点击租房房源详情其他同小区房源"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_top(self):
        """
        点击租房房源详情置顶按钮
        :return:
        """
        with allure.step("点击租房房源详情置顶按钮"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_business(self):
        """
        点击租房房源详情经纪人头像
        :return:
        """
        with allure.step("点击租房房源详情经纪人头像"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_call(self):
        """
        点击租房房源详情经纪人电话
        :return:
        """
        with allure.step("点击租房房源详情经纪人电话"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
        self.tsleep(2)
        return self

    def click_renthouse_detail_im(self):
        """
        点击租房房源详情经纪人IM咨询
        :return:
        """
        with allure.step("点击租房房源详情经纪人IM咨询"):
            self.steps("../../page_object/renthouse/renthousedetail.yaml")
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
            self.steps("../../page_object/renthouse/renthousedetail.yaml", replace=True)
        self.tsleep(2)
        return self
