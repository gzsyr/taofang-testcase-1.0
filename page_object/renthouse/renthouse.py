import allure
from page_object.base_page.base_page import BasePage

class RentHouse(BasePage):

    """
    租房首页相关元素
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
        return self

