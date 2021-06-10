import allure

from page_object.base_page.base_page import BasePage
from page_object.sellhouse.publishhouse import PublishHouse


class PublishIndex(BasePage):
    """
    发布房源  引导页面
    """

    def click_publishindex_m_publish(self):
        """
        点击发布房源引导页的发布房源按钮
        :return:
        """
        with allure.step("点击发布房源引导页的发布房源按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return PublishHouse(self._driver)

    def click_publishindex_m_help(self):
        """
        点击右上角帮助按钮
        :return:
        """
        with allure.step("点击发布房源引导页的右上角帮助按钮按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return self

    def click_publishindex_m_service(self):
        """
        点击右上角服务按钮
        :return:
        """
        with allure.step("点击发布房源引导页的服务按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return self

    def click_publishindex_m_pinggu_img(self):
        """
        点击工具评估房价
        :return:
        """
        with allure.step("点击发布房源引导页的评估房价按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return self

    def click_publishindex_m_xuequ_img(self):
        """
        点击学校地图按钮
        :return:
        """
        with allure.step("点击发布房源引导页的学校地图按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return self

    def click_publishindex_m_jisuanqi_img(self):
        """
        点击计算器按钮
        :return:
        """
        with allure.step("点击发布房源引导页的计算器按钮"):
            self.steps("../../page_object/sellhouse/publishindex.yaml")
        self.tsleep(2)
        return self
