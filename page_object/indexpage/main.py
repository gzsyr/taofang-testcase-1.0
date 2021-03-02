import allure

from page_object.base_page.base_page import BasePage
from page_object.newhouse.newhouselist import NewHouseList


class Main(BasePage):
    """
    首页，各点击入口
    """
    def goto_newhouse(self):
        """
        点击横幅广告
        :return:
        """
        with allure.step("点击新房icon"):
            # self.steps("../../page_object/indexpage/main.yaml")
            self.steps("../../page_object/indexpage/main.yaml")
        self.tsleep(2)
        return NewHouseList(self._driver)

