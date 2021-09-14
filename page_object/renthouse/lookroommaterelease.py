import allure

from page_object.base_page.base_page import BasePage


class LookRoommateRelease(BasePage):
    """
    找室友房源发布
    """

    def lookroommate_house_rent(self):
        """
        发布找室友房源点击有房出租
        :return:
        """
        with allure.step("找室友发布页点击有房出租"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def lookroommate_upload_photos(self):
        """
        发布找室友点击上传照片
        :return:
        """
        with allure.step("找室友发布页面点击上传照片"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def lookroommate_add_photos(self):
        """
        照片添加页点击添加照片
        :return:
        """
        with allure.step("照片添加也点击添加照片"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def lookroommatehouse_take_pictures(self):
        """
        拍摄一张照片
        :return:
        """
        with allure.step("拍摄一张照片上传"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_take_picture_complete(self):
        """
        图片上传之后点击完成按钮
        """
        with allure.step("图片上传之后点击完成按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_take_picture_need(self):
        """
        图片上传后点击完成按钮点击二次确认的不需要按钮
        """
        with allure.step("图片上传后点击完成按钮点击二次确认的不需要按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def lookroommatehouse_choose_photos(self, keyword="1"):
        """
        更多资料页上传相册图片.默认上传第一张
        :return:
        """
        self._params["index"] = keyword
        with allure.step("图片上传页选择相册上传图片"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_bell(self):
        """
        图片添加页点击小铃铛
        :return:
        """
        with allure.step("图片添加页点击小铃铛"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_bell_close(self):
        """
        图片添加页点击小铃铛点击关闭按钮
        :return:
        """
        with allure.step("图片添加页点击小铃铛点击关闭按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_skills(self):
        """
        图片添加页点击小技巧
        :return:
        """
        with allure.step("图片添加页点击小技巧"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_skills_close(self):
        """
        图片添加页点击小技巧点击关闭
        :return:
        """
        with allure.step("图片添加页点击小技巧点击关闭"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_title(self, keyword="新街口地铁站附近求合租，男女不限"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["title_name"] = keyword
        with allure.step("输入标题: " + self._params["title_name"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def click_village_name(self):
        """
        点击小区名称
        :return:
        """
        with allure.step("发布页点击小区名称"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_name_search(self, keyword="万科"):
        """
        :param keyword: 小区名称输入框输入万科
        :return:
        """
        self._params["village_name"] = keyword
        with allure.step("输入小区名称: " + self._params["village_name"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def click_search_result(self):
        """
        点击小区名称搜索结果，点击万科金域蓝湾
        :return:
        """
        with allure.step("点击小区名称搜索结果"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_month_rent(self):
        """
        发布页点击月租金
        :return:
        """
        with allure.step("点击月租金"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_month_rent_price(self):
        """
        :param keyword: 月租金输入2315
        :return:
        """
        with allure.step("输入月租金2315"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_month_rent_determine(self):
        """
        输入月租金点击确定按钮
        :return:
        """
        with allure.step("点击确定按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_door_model(self):
        """
        点击户型
        :return:
        """
        with allure.step("点击户型"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_door_model(self):
        """
        选择户型和出租类型
        """
        with allure.step("选择户型和出租类型"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
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
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_check_in_time(self):
        """
        点击入住时间
        """
        with allure.step("点击入住时间"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_check_in_time(self):
        """
        选择入住时间和已入住情况
        """
        with allure.step("选择入住时间和已入住情况"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_have_elevator(self):
        """
        房屋亮点选择“有电梯”
        """
        with allure.step("房屋亮点选择有电梯"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_housing_allocation(self):
        """
        选择房屋配置
        """
        with allure.step("选择房屋配置"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_next_step(self):
        """
        点击下一步
        """
        with allure.step("点击下一步"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_roommate_gender(self):
        """
        室友性别选择限男生
        """
        with allure.step("室友性别选择限男生"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_roommate_expectations(self):
        """
        室友期望选择一个人住
        """
        with allure.step("室友期望选择一个人住"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_added_text(self, keyword="希望找一个一起分担房租的小伙伴"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["add_text"] = keyword
        with allure.step("输入补充说明: " + self._params["add_text"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def choose_identity(self):
        """
        身份选择租户
        """
        with allure.step("身份选择租户"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_enter_name(self, keyword="张"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["add_name"] = keyword
        with allure.step("输入姓名: " + self._params["add_name"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def click_confirm_release(self):
        """
        点击确认发布按钮
        """
        with allure.step("点击确认发布按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    """
    找室友发布无房求租
    """


    def click_housing_price(self):
        """
        点击无房求租
        """
        with allure.step("点击无房求租"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_title_input_box(self, keyword="鼓楼区希望找一个一起分担房租的小伙伴"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["tit_name"] = keyword
        with allure.step("输入标题: " + self._params["tit_name"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def click_expect_place(self):
        """
        点击期望地点
        """
        with allure.step("点期望地点"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_gulou_district(self):
        """
        选择鼓楼区
        """
        with allure.step("选择鼓楼区"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_expect_place_determine(self):
        """
        选择鼓楼去点击确定按钮
        """
        with allure.step("选择鼓楼区点击确定按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_rent_budget(self):
        """
        点击租金预算
        """
        with allure.step("点击租金预算"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_rent_budget(self):
        """
        选择租金预算
        """
        with allure.step("选择租金预算"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_rent_budget_determine(self):
        """
        选择租金预算后点击确定按钮
        """
        with allure.step("选择租金预算后点击确定按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_check_time(self):
        """
        点击入住时间
        """
        with allure.step("点击入住时间"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_check_in_time_determine(self):
        """
        点击入住时间的确定按钮
        """
        with allure.step("点击入住时间的确定按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_people_live(self):
        """
        点击我是几人住
        """
        with allure.step("点击我是几人住"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_people_live_determine(self):
        """
        点击我是几人住的确定按钮
        """
        with allure.step("点击我是几人住的确定按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_expect_alone_toilet(self):
        """
        选择对房子的期望有独卫
        """
        with allure.step("选择对房子的期望有独卫"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def click_the_next_step(self):
        """
        点击下一步按钮
        """
        with allure.step("点击下一步按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_gender_boy(self):
        """
        室友性别选择限男生
        """
        with allure.step("室友性别选择限男生"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def choose_roommate_expectation_alone(self):
        """
        室友期望选择一个人住
        """
        with allure.step("室友期望选择一个人住"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self

    def enter_supplementary_text(self, keyword="找个室友一起合租"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["int_text"] = keyword
        with allure.step("输入补充说明: " + self._params["int_text"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def enter_the_name(self, keyword="张"):
        """
        :param keyword: 输入内容
        :return:
        """
        self._params["int_name"] = keyword
        with allure.step("输入姓名: " + self._params["int_name"]):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml", replace=True)
        return self

    def click_confirm_the_release(self):
        """
        点击确认发布按钮
        """
        with allure.step("点击确认发布按钮"):
            self.steps("../../page_object/renthouse/lookroommaterelease.yaml")
        self.tsleep(2)
        return self