import allure

from page_object.base_page.base_page import BasePage
from page_object.sellhouse.publishmore import PublishMore


class PublishHouse(BasePage):
    """
    发布房源 页面
    """

    def close_house_type(self):
        """
        关闭物业类型弹窗
        :return:
        """
        with allure.step("点击发布房源的物业类型右侧箭头，弹出物业类型选择弹窗"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_reset(self):
        """
        目的：重置发布房源信息
        步骤：1、点击“重置”
             2、点击“确定”
        :return:
        """
        with allure.step("点击重置房源信息"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def select_pubilshhouse_type(self, house_item="物业类型", house_type="住宅"):
        """
        选择 房屋类型
        :param:  house_item: 选择项，用户步骤中展示
                 house_type: 房屋类型，默认为“住宅”
        :return:
        """
        self._params["house_type"] = house_type
        with allure.step("选择”" + house_item + "“的内容：" + house_type):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_type(self):
        """
        点击发布房源的物业类型
        :return:
        """
        with allure.step("点击发布房源的物业类型右侧箭头，弹出物业类型选择弹窗"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_name(self):
        """
        点击发布房源的小区名称
        :return:
        """
        with allure.step("点击发布房源的小区名称右侧箭头，进入小区搜索页"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_name_search(self, keyword="万科红郡住宅"):
        """
        执行搜索
        :param keyword: 输入搜索关键词，默认“万科红郡住宅”
        :return:
        """
        self._params["house_name"] = keyword
        with allure.step("输入搜索关键词: " + self._params["house_name"]):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)

        # 切换输入法，使用键盘的“搜索”键
        # self.adbshell('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        # self.tsleep(3)
        # self._driver.press_keycode('66')  # os.system("adb shell input keyevent 66")
        # self.adbshell('adb shell ime set io.appium.settings/.UnicodeIME')
        # self.tsleep(3)

        return self

    def select_publishhouse_name_result(self):
        """
        选择小区搜索结果
        :return:
        """
        with allure.step("选择小区搜索结果"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_dong(self, keyword="10"):
        """
        输入发布房源楼栋号，默认10栋
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入发布房源楼栋号：" + self._params["house_detail"] + "栋"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_danyuan(self, keyword='1'):
        """
        输入发布房源单元，默认1单元
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入发布房源单元：" + self._params["house_detail"] + "单元"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_shi(self, keyword='506'):
        """
        输入发布房源室
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入发布房源室" + self._params["house_detail"] + "室"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_price(self, keyword='300'):
        """
        输入出售房源期望价格，默认300万元
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入出售房源期望价格" + self._params["house_detail"] + "万元"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_area(self, keyword='120'):
        """
        输入出售房源面积，默认120平
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入出售房源面积" + self._params["house_detail"] + "面积"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_property(self):
        """
        点击发布房源的房屋权属
        :return:
        """
        with allure.step("点击发布房源的点击发布房源的房屋权属右侧箭头，弹出权属选择弹窗"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_seller(self, keyword='钱女士'):
        """
        输入出售房源您的称呼，默认钱女士
        :return:
        """
        self._params["house_detail"] = keyword
        with allure.step("输入出售房源您的称呼" + self._params["house_detail"]):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_next(self):
        """
        点击下一步
        :return:
        """
        with allure.step("点击出售房源下一步"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return PublishMore(self._driver)

    def goto_next_all(self, house_type="住宅",  name="测试正式小区2", dong='8', danyuan='1', shi='502',
                      price='450', area='120', house_ownership='产权房', seller='365公司'):
        """
        输入出售房源信息
        :return:
        """
        self._params["house_type"] = house_type
        self._params["name"] = name
        self._params["dong"] = dong
        self._params["danyuan"] = danyuan
        self._params["shi"] = shi
        self._params["price"] = price
        self._params["area"] = area
        self._params["house_ownership"] = house_ownership
        self._params["seller"] = seller
        with allure.step("输入出售房源信息，点击下一步"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self
