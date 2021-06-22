import allure
from page_object.base_page.base_page import BasePage
from page_object.renthouse.brandapartmentlist import BrandApartmentList
from page_object.renthouse.lookroommatelist import LookRoommateList
from page_object.renthouse.officebuildinglist import OfficeBuildingList
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


