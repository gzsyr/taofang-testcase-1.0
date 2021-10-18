import allure

from page_object.base_page.base_page import BasePage


class ShopMallList(BasePage):
    """
    商铺办公
    """
    def goto_officelist(self, text='买商铺'):
        """
        点击功能入口，进入商铺写字楼子页面
        :param text: 传入的需要点击的文本内容
                     默认买商铺
        :return:
        """
        self._params["func_entry"] = text
        with allure.step("点击商业写字楼频道首页的功能入口" + text):
            self.steps("../../page_object/business/shopmalllist.yaml", replace=True)
        self.tsleep(2)
        return self

    def goto_newslist(self):
        """
        点击最新商讯
        :return:
        """
        with allure.step("点击最新商讯"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def find_office(self):
        """
        点击帮你找铺
        :return:
        """
        with allure.step("点击帮你找铺"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def select_buy_shop(self):
        """
        点击买商铺tab
        :return:
        """
        with allure.step("点击买商铺tab"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def select_rent_shop(self):
        """
        点击租商铺tab
        :return:
        """
        with allure.step("点击租商铺tab"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def select_buy_office(self):
        """
        点击买写字楼tab
        :return:
        """
        with allure.step("点击买写字楼tab"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def select_rent_office(self):
        """
        点击租写字楼tab
        :return:
        """
        with allure.step("点击租写字楼tab"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def select_filter_office(self, text='建邺区'):
        """
        点击推荐房源筛选项
        :param text: 传入的需要点击的文本内容
                     默认建邺区
        :return:
        """
        self._params["menu"] = text
        with allure.step("点击商业写字楼频道推荐房源筛选项" + text):
            self.steps("../../page_object/business/shopmalllist.yaml", replace=True)
        self.tsleep(2)
        return self

    def goto_buy_shop_list(self):
        """
        点击买商铺房源
        :return:
        """
        with allure.step("点击买商铺tab列表下房源"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def goto_rent_shop_detial(self):
        """
        点击租商铺tab列表下房源
        :return:
        """
        with allure.step("点击租商铺tab列表下房源"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def goto_buy_office_detial(self):
        """
        点击买写字楼tab列表下房源
        :return:
        """
        with allure.step("点击买写字楼tab列表下房源"):
            self.steps("../../page_object/business/shopmalllist.yaml")
        self.tsleep(2)
        return self

    def goto_rent_office_detial(self):
        """
        点击租写字楼tab列表下房源
        :return:
        """
        with allure.step("点击租写字楼tab列表下房源"):
            self.steps("../../page_object/business/shopmalllist.yaml")
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
