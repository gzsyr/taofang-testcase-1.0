import allure

from page_object.base_page.base_page import BasePage


class NewHouseDetail(BasePage):
    """
    新房详情页面，页面元素
    """
    def goto_photo(self):
        """
        点击相册上面的“查看更多”
        :return:
        """
        with allure.step("点击相册上面的“查看更多”"):
            self.steps("../../page_object/newhouse/newhousedetail.yaml")
        self.tsleep(2)

        return self
