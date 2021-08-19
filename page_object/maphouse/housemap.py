import allure

from page_object.base_page.base_page import BasePage


class MapFindHouse(BasePage):
    """
    新房地图找房页面
    """
    def goto_search(self, house_name='万象天地四季'):
        """
        进入搜索页
        :return:
        """
        self._params["house_name"] = house_name
        with allure.step("点击搜索按钮"):
            self.steps("../../page_object/maphouse/housemap.yaml", replace=True)

        return self

    def show_select(self):
        """
        展开筛选项
        :returen:
        """
        with allure.step('展开筛选栏'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def select_filter_item(self, text='不限'):
        """
        选择筛选项
        :returen:
        """
        self._params["filter"] = text
        with allure.step('选择筛选项'):
            self.steps("../../page_object/maphouse/housemap.yaml", replace=True)
            return self

    def empty_filter(self):
        """
        清空筛选项
        :returen:
        """
        with allure.step('清空筛选项'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def confirm_filter(self):
        """
        确定筛选
        :returen:
        """
        with allure.step('确定筛选'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def show_metro(self):
        """
        展开地图选项
        :returen:
        """
        with allure.step('展开地铁选项'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def show_filter_conditions(self):
        """
        展开已筛选项
        :returen:
        """
        with allure.step('展开已筛选项'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def goto_housedetail(self):
        """
        进入房源详情
        :returen:
        """
        with allure.step('进入房源详情'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def click_location(self):
        """
        点击定位
        :returen:
        """
        with allure.step('点击定位'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def goto_community(self):
        """
        进入小区详情
        :returen:
        """
        with allure.step('进入小区详情'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def select_housetab(self, housetab='新房'):
        """
        切换地图tab
        :returen:
        """
        self._params["housetab"] = housetab
        with allure.step('切换地图tab'):
            self.steps("../../page_object/maphouse/housemap.yaml", replace=True)
            return self

    def goto_schoolmap(self):
        """
        进入学校地图
        :returen:
        """
        with allure.step('进入学校地图'):
            self.steps("../../page_object/maphouse/housemap.yaml")
            return self

    def func_swipe(self, pos_text='buttom'):
        """
        滑动到pos_text的位置，滑动
        :param pos_text: 1、写入页面存在的元素
                         2、如果写pos_text=buttom，则滑动到页面底部
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("滑动到" + self._params["pos_text"]):
            self.steps("../../page_object/maphouse/housemap.yaml", replace=True)
        self.tsleep(2)
        return self
