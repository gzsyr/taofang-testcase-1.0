import allure

from page_object.base_page.base_page import BasePage
from page_object.newhouse.newhousedetail import NewHouseDetail


class IndexSearch(BasePage):
    """
    首页，点击搜索框后的页面
    """
    def action_search(self, keyword="华侨城翡翠天域"):
        """
        执行搜索
        :param keyword: 输入搜索关键词，默认“华侨城翡翠天域”
        :return:
        """
        self._params["house_name"] = keyword
        with allure.step("输入搜索关键词: " + self._params["house_name"]):
            self.steps("../../page_object/indexpage/main.yaml", replace=True)

        # 切换输入法，使用键盘的“搜索”键
        self.adbshell('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        self.tsleep(3)
        self._driver.press_keycode('66')  # os.system("adb shell input keyevent 66")
        self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        self.tsleep(3)

        return self

    def select_search_result(self, housename = None):
        # self._params["house_name"] = housename
        with allure.step("点击搜索结果楼盘页面"):
            self.steps("../../page_object/indexpage/main.yaml", replace=True)

        return NewHouseDetail(self._driver)


