import allure

from page_object.base_page.base_page import BasePage


class SingleApartmentList(BasePage):
    """
    独栋公寓页面
    """
    def click_singleapartmentlist_filter(self,text = None):
        """
        筛选项
        """
        self._params["single_filter"] = text
        with allure.step("点击筛选项"+ text):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml", replace=True)
        self.tsleep(1)
        return self

    def click_singleapartmentlist_location(self):
        """
        点击区域
        """
        with allure.step("点击区域"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_singleapartmentlist_rent(self):
        """
        点击租金
        """
        with allure.step("点击租金"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_singleapartmentlist_area(self):
        """
        点击面积
        """
        with allure.step("点击面积"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self


    def click_singleapartmentlist_brand(self):
        """
        点击品牌
        """
        with allure.step("点击品牌"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_singleapartmentlist_confirm(self):
        """
        点击确定
        """
        with allure.step("点击确定"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self


    def click_singleapartmentlist_empty(self):
        """
        点击清空
        """
        with allure.step("点击清空"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self

    def click_singleapartmentlist_house(self):
        """
        点击列表页第一个房源
        """
        with allure.step("点击房源"):
            self.steps("../../page_object/renthouse/singleapartmentlist.yaml")
        self.tsleep(1)
        return self


