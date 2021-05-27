import allure

from page_object.base_page.base_page import BasePage


class NewHouseDetail(BasePage):
    """
    新房详情页面，页面元素
    """
    def cick_newhouse_detail_more(self):
        """
        点击相册上面的“查看更多”
        :return:
        """
        with allure.step("点击相册上面的“查看更多”"):
            self.steps("../../page_object/newhouse/newhousedetail.yaml")
        self.tsleep(2)

        return self

    def click_newhouse_detail_collection(self):
        """
        新房详情页点击收藏按钮
        :return:
        """
        with allure.step("新房详情页点击收藏按钮"):
            self.steps("../../page_object/newhouse/newhousedetail.yaml")
        self.tsleep(2)

        return self

    def cick_newhouse_detail_share(self):
        """
        新房详情页点击分享按钮
        :return:
        """
        with allure.step("新房详情页点击分享按钮"):
            self.steps("../../page_object/newhouse/newhousedetail.yaml")
        self.tsleep(2)

        return self

    def cick_newhouse_detail_picture(self):
        """
        新房详情页点击图片
        :return:
        """
        with allure.step("新房详情页点击图片"):
            self.steps("../../page_object/newhouse/newhousedetail.yaml")
        self.tsleep(2)

        return self
