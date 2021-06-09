import allure

from page_object.base_page.base_page import BasePage


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
        return self

    def goto_next_all(self, type="住宅",  name="万科红郡住宅", dong='8', danyuan='1', shi='502',
                      price='450', area='120', property='产权房', seller='365公司'):
        """
        输入出售房源信息
        :return:
        """
        self._params["type"] = type
        self._params["name"] = name
        self._params["dong"] = dong
        self._params["danyuan"] = danyuan
        self._params["shi"] = shi
        self._params["price"] = price
        self._params["area"] = area
        self._params["property"] = property
        self._params["seller"] = seller
        with allure.step("输入出售房源信息，点击下一步"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_room(self):
        """
        更多资料页点击户型
        :return:
        """
        with allure.step("更多资料页点击户型"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_cancel(self):
        """
        更多资料页选择点击取消
        :return:
        """
        with allure.step("更多资料页取消选择"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_confirm(self):
        """
        更多资料页选择点击确定
        :return:
        """
        with allure.step("更多资料页确定选择"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_floor(self):
        """
        更多资料页点击楼层
        :return:
        """
        with allure.step("更多资料页点击楼层"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_floor_cancel(self):
        """
        更多资料页点击楼层取消选择
        :return:
        """
        with allure.step("更多资料页确定楼层取消选择"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_floor_confirm(self):
        """
        更多资料页点击确定
        :return:
        """
        with allure.step("更多资料页确定楼层选择"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def select_publishhouse_flat(self):
        """
        更多资料页楼层选择点击单层
        :return:
        """
        with allure.step("更多资料页楼层选择点击单层"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def select_publishhouse_jump(self):
        """
        更多资料页楼层选择点击跃层
        :return:
        """
        with allure.step("更多资料页楼层选择点击跃层"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self


    def click_publishhouse_pictures(self):
        """
        更多资料页点击房屋照片
        :return:
        """
        with allure.step("更多资料页进入房屋照片页"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_prompt(self):
        """
        更多资料页房屋照片点击提示
        :return:
        """
        with allure.step("更多资料页点击房屋照片提示"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_add_pictures(self):
        """
        更多资料页添加房屋照片
        :return:
        """
        with allure.step("更多资料页添加房屋照片"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_taking_pictures(self):
        """
        更多资料页房屋照片选择拍照
        :return:
        """
        with allure.step("更多资料页房屋照片选择拍照"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_taking_pictures_finish(self):
        """
        更多资料页房屋照片完成添加
        :return:
        """
        with allure.step("更多资料页房屋照片完成添加"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_back(self):
        """
        更多资料页左上角返回
        :return:
        """
        with allure.step("更多资料页子页面左上角返回"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_back_confirm(self):
        """
        更多资料页返回二次确定
        :return:
        """
        with allure.step("更多资料页返回二次确定"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_back_cancel(self):
        """
        更多资料页子页面取消返回
        :return:
        """
        with allure.step("更多资料页子页面取消返回"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_desc(self):
        """
        更多资料页点击房源描述
        :return:
        """
        with allure.step("更多资料页点击房源描述"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_text(self, keyword='电梯房，满五唯一'):
        """
        更多资料页输入文本内容
        :return:
        """
        self._params["text"] = keyword
        with allure.step("更多资料页输入文本内容"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml", replace=True)
        self.tsleep(2)
        return self


    def click_publishhouse_feature(self):
        """
        更多资料页点击房源特色
        :return:
        """
        with allure.step("更多资料页点击房源特色"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self


    def click_publishhouse_identity(self):
        """
        更多资料页进入上传证件照页面
        :return:
        """
        with allure.step("更多资料页进入上传证件照页面"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_add_identity(self):
        """
        更多资料页添加证件照
        :return:
        """
        with allure.step("更多资料页添加证件照"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self


    def click_publishhouse_identity_confirm(self):
        """
        更多资料页上传证件照完成
        :return:
        """
        with allure.step("更多资料页上传证件照完成"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self


    def click_publishhouse_ownership(self):
        """
        更多资料页进入权属认证页
        :return:
        """
        with allure.step("更多资料页进入权属认证页"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_ownership_type(self):
        """
        更多资料页-权属认证页-证件类型
        :return:
        """
        with allure.step("更多资料页-权属认证页-证件类型"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_ownership_number(self, keyword='宁（2020）市不动产权第0041921号'):
        """
        更多资料页-区属认证-证件号码
        :return:
        """
        self._params["ownership_number"] = keyword
        with allure.step("输入更多资料页-区属认证-证件号码"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_property_owner(self, keyword='钱女士'):
        """
        更多资料页-权属认证-产权人姓名
        :return:
        """
        self._params["property_owner"] = keyword
        with allure.step("更多资料页-权属认证-产权人姓名"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_owner_identity(self, keyword='32011122011252123'):
        """
        更多资料页-权属认证-产权人身份证号
        :return:
        """
        self._params["owner_identity"] = keyword
        with allure.step("更多资料页点击户型"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_submit(self):
        """
        更多资料页完成按钮点击
        :return:
        """
        with allure.step("更多资料页完成按钮点击"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_title(self):
        """
        更多资料页点击标题
        :return:
        """
        with allure.step("更多资料页点击标题"):
            self.steps("../../page_object/sellhouse/publishhouse.yaml")
        self.tsleep(2)
        return self


