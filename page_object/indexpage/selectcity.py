import allure

from page_object.base_page.base_page import BasePage


class SelectCity(BasePage):
    """
    选择城市页面
    """
    def select_name(self, name="南京"):
        """
        按照内容选择
        :param name: 默认“南京”
        :return:
        """
        self._params["name"] = name
        with allure.step("选择内容：" + self._params["name"]):
            self.steps("../../page_object/indexpage/selectcity.yaml", replace=True)
        return self

    def select_letter(self, letter='A'):
        """
        选择右侧的大写字母
        :param letter: 默认'A'
        :return:
        """
        return self.select_name(letter)

    def select_city(self, cityname="南京"):
        """
        选择城市名称
        :param cityname: 默认 南京
        :return:
        """
        return self.select_name(cityname)
