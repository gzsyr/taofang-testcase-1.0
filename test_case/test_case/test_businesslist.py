import allure
import pytest

from test_case.base_test.test_base import TestBase


class TestBusinessList(TestBase):
    """
    商业写字楼频道
    """
    def goto_shopmalllist(self):
        """
        进入商业写字楼列表页
        :return:
        """
        return self.shouye.goto_func_entrance_spbg()

    @allure.description("点击功能入口")
    @pytest.mark.parametrize("func_entry", ["买商铺", "租商铺", "买写字楼", "租写字楼",
                                            "产业园区", "买二手商铺", "买二手写字楼", "买二手公寓"])
    def test_goto_officelist(self, func_entry):
        """
        点击功能入口
        """
        self.goto_shopmalllist().goto_officelist(func_entry).screenshot()

    @allure.description("点击最新商讯")
    def test_goto_officenews(self):
        """
        点击最新商讯
        """
        self.goto_shopmalllist().goto_newslist().screenshot()

    @allure.description("点击帮你找铺")
    def test_find_office(self):
        """
        点击帮你找铺
        """
        self.goto_shopmalllist().find_office().screenshot()

    @allure.description("点击买商铺tab")
    def test_select_buy_shop(self):
        """
        点击买商铺tab
        """
        self.goto_shopmalllist().select_buy_shop().screenshot()

    @allure.description("点击租商铺tab")
    def test_select_rent_shop(self):
        """
        点击租商铺tab
        """
        self.goto_shopmalllist().select_rent_shop().screenshot()

    @allure.description("点击买写字楼tab")
    def test_select_buy_office(self):
        """
        点击买写字楼tab
        """
        self.goto_shopmalllist().select_buy_office().screenshot()

    @allure.description("点击租写字楼tab")
    def test_select_rent_office(self):
        """
        点击租写字楼tab
        """
        self.goto_shopmalllist().select_rent_office().screenshot()

    @allure.description("点击买商铺-建邺区")
    def test_select_shop_position(self):
        """
        点击买商铺-建邺区
        """
        self.goto_shopmalllist().select_buy_shop().select_filter_office().screenshot()

    @allure.description("点击买商铺-120到180万元")
    def test_select_shop_price(self):
        """
        点击买商铺-120到180万元
        """
        self.goto_shopmalllist().select_buy_shop().select_filter_office("120-180万元").screenshot()

    @allure.description("点击买商铺-房源")
    def test_goto_buy_shop(self):
        """
        点击买商铺-房源
        """
        self.goto_shopmalllist().select_buy_shop().goto_buy_shop_list().screenshot()

    @allure.description("点击租商铺-房源")
    def test_goto_rent_shop(self):
        """
        点击租商铺-房源
        """
        self.goto_shopmalllist().select_rent_shop().goto_rent_shop_detial().screenshot()

    @allure.description("点击买写字楼-建邺区")
    def test_select_office_position(self):
        """
        点击买写字楼-建邺区
        """
        self.goto_shopmalllist().select_buy_office().select_filter_office("建邺区").screenshot()

    @allure.description("点击买写字楼-10000到15000元/平米")
    def test_select_office_price(self):
        """
        点击买写字楼-10000到15000元/平米
        """
        self.goto_shopmalllist().select_buy_office().select_filter_office("10000-15000元/m²").screenshot()

    @allure.description("点击买写字楼-房源")
    def test_goto_buy_office(self):
        """
        点击买写字楼-房源
        """
        self.goto_shopmalllist().select_buy_office().goto_buy_office_detial().screenshot()

    @allure.description("点击租写字楼-房源")
    def test_goto_rent_office(self):
        """
        点击租写字楼-房源
        """
        self.goto_shopmalllist().select_rent_office().goto_rent_office_detial().screenshot()
