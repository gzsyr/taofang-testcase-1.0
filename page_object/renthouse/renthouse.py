import allure
from page_object.base_page.base_page import BasePage
from page_object.renthouse.brandapartmentlist import BrandApartmentList
from page_object.renthouse.lookroommatelist import LookRoommateList
from page_object.renthouse.officebuildinglist import OfficeBuildingList
from page_object.renthouse.publishrentalindex import PublishRentalIndex
from page_object.renthouse.rentfindhouse import RentFindHouse
from page_object.renthouse.renthouselist import RentHouseList
from page_object.renthouse.singleapartmentlist import SingleApartmentList


class RentHouse(BasePage):
    """
    租房首页
    """
    def rent_house_search(self):
        """
        租房首页点击搜索框
        :return:
        """
        with allure.step("租房首页点击搜索框"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def map_find_room(self):
        """
        租房首页点击地图找房
        :return:
        """
        with allure.step("租房首页点击地图找房"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def commuting_find_room(self):
        """
        租房首页点击通勤找房、
        :return:
        """
        with allure.step("租房首页点击通勤找房"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_news(self):
        """
        租房首页点击消息
        :return:
        """
        with allure.step("租房首页点击消息"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_function_entrance(self, func_entry="整租"):
        """
        功能入口统一，参数化使用
        :param: func_entry功能入口的名称
        :return:
        """
        self._params["func_entry"] = func_entry
        with allure.step("点击功能入口：" + self._params["func_entry"]):
            self.steps("../../page_object/renthouse/renthouse.yaml", replace=True)
        self.tsleep(1)
        if "整租" == self._params["func_entry"]:
            return RentHouseList(self._driver)
        elif "找室友" == self._params["func_entry"]:
            return LookRoommateList(self._driver)
        elif "品牌公寓" == self._params["func_entry"]:
            return BrandApartmentList(self._driver)
        elif "写字楼" == self._params["func_entry"]:
            return OfficeBuildingList(self._driver)
        elif "独栋公寓" == self._params["func_entry"]:
            return SingleApartmentList(self._driver)
        elif "我要求租" == self._params["func_entry"]:
            return RentFindHouse(self._driver)
        else:
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

    def rent_house_nearby(self):
        """
        租房首页点击附近tab
        :return:
        """
        with allure.step("租房首页点击附近tab"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_apartment(self):
        """
        租房首页点击公寓tab
        :return:
        """
        with allure.step("租房首页点击公寓tab"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_strict_selection(self):
        """
        租房首页点击严选tab
        :return:
        """
        with allure.step("租房首页点击严选tab"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_office(self):
        """
        租房首页点击写字楼tab
        :return:
        """
        with allure.step("租房首页点击写字楼tab"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_release_house(self):
        """
        租房首页点击发布房源
        :return:
        """
        with allure.step("租房首页点击发布房源"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return PublishRentalIndex(self._driver)

    def rent_house_mine(self):
        """
        租房首页点击我的
        :return:
        """
        with allure.step("租房首页点击我的"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self

    def rent_house_rent_consultant(self):
        """
        租房首页点击租房顾问
        :return:
        """
        with allure.step("租房首页点击租房顾问"):
            self.steps("../../page_object/renthouse/renthouse.yaml")
        self.tsleep(2)

        return self


