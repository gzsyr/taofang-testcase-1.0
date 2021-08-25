# -- by hzc
import allure

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 租房-发布找室友页面的测试")
class TestLookRoommateRelease(TestBase):
    """
    发布找室友房源相关用例
    """

    def goto_lookroom_release(self):
        """
        找室友列表点击发布
        """
        return self.shouye.goto_func_entrance_zf().rent_house_function_entrance("找室友").click_lookroom_release()

    def goto_second_page(self):
        """
        填写第一页数据，去到第二页
        """
        return self.goto_lookroom_release().lookroommate_house_rent().lookroommate_upload_photos(). \
            lookroommate_add_photos().lookroommatehouse_choose_photos("2").lookroommate_add_photos().lookroommatehouse_choose_photos("1"). \
            lookroommate_add_photos().lookroommatehouse_choose_photos("3").click_take_picture_complete(). \
            click_title().click_village_name().click_name_search().click_search_result().click_month_rent().click_month_rent_price(). \
            click_month_rent_determine().click_door_model().choose_door_model().func_swipe("房屋配置").click_check_in_time(). \
            choose_check_in_time().choose_have_elevator().choose_housing_allocation().click_next_step()

    def goto_next_page(self):
        """
        无房求租，填写第一页数据，去到第二页
        """
        return self.goto_lookroom_release().click_housing_price().click_title_input_box().click_expect_place().choose_gulou_district(). \
            click_expect_place_determine().click_rent_budget().choose_rent_budget_determine().click_check_time().click_check_in_time_determine(). \
            click_people_live().click_people_live_determine().click_expect_alone_toilet().click_the_next_step()

    @allure.description("找室友列表点击发布点击有房出租")
    def test_lookroommate_house_rent(self):
        """
        找室友列表点击发布点击有房出租
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().screenshot()

    @allure.description("图片上传页选择拍照上传一张图片")
    def test_lookroommatehouse_take_pictures(self):
        """
        上传一张拍照房源图片
        少于3张图片完成时需二次确定
        :return:
        """
        step1 = self.goto_lookroom_release().lookroommate_house_rent(). \
            lookroommate_upload_photos().lookroommate_add_photos().lookroommatehouse_take_pictures()
        step1.screenshot()
        step2 = step1.click_take_picture_complete().click_take_picture_need()
        step2.screenshot()

    @allure.description("图片上传页选择相册上传图片")
    def test_lookroommatehouse_choose_photos(self):
        """
        图片上传页选择相册上传图片
        :return:
        """
        step1 = self.goto_lookroom_release().lookroommate_house_rent().lookroommate_upload_photos(). \
            lookroommate_add_photos().lookroommatehouse_choose_photos()
        step1.screenshot()
        step1.click_take_picture_complete().click_take_picture_need().screenshot()

    @allure.description("图片上传页点击小铃铛后关闭")
    def test_click_bell(self):
        """
        图片上传页点击小铃铛后关闭
        :return:
        """
        step1 = self.goto_lookroom_release().lookroommate_house_rent().lookroommate_upload_photos(). \
            click_bell()
        step1.screenshot()
        step1.click_bell_close().screenshot()

    @allure.description("图片上传页点击小技巧点击关闭")
    def test_click_skills(self):
        """
        图片上传页点击小技巧后点击关闭
        :return:
        """
        step1 = self.goto_lookroom_release().lookroommate_house_rent().lookroommate_upload_photos(). \
            click_skills()
        step1.screenshot()
        step1.click_skills_close().screenshot()

    @allure.description("输入标题")
    def test_click_title(self):
        """
        找室友发布页输入标题
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_title().screenshot()

    @allure.description("选择小区名称")
    def test_send_village_name(self):
        """
        找室友发布页选择小区名，默认选择万科金域蓝湾
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_village_name().click_name_search("万科"). \
            click_search_result().screenshot()

    @allure.description("输入月租金2315")
    def test_send_month_rent(self):
        """
        找室友发布页输入月租金2315
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_month_rent().click_month_rent_price(). \
            click_month_rent_determine().screenshot()

    @allure.description("选择户型和出租类型")
    def test_choose_door_model(self):
        """
        找室友发布页选择户型和出租类型
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_door_model(). \
            choose_door_model().screenshot()

    @allure.description("滑动到”房屋配置“，点击入住时间选择入住时间和已入住情况")
    def test_choose_check_in_time(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.goto_lookroom_release().lookroommate_house_rent().func_swipe("房屋配置").click_check_in_time(). \
            choose_check_in_time().screenshot()

    @allure.description("滑动到”房屋配置“，房屋亮点选择有电梯")
    def test_choose_check_in_time(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.goto_lookroom_release().lookroommate_house_rent().func_swipe("房屋配置").choose_have_elevator().screenshot()

    @allure.description("滑动到”房屋配置“，选择房屋配置")
    def test_choose_housing_allocation(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.goto_lookroom_release().lookroommate_house_rent().func_swipe("房屋配置").choose_housing_allocation().screenshot()

    @allure.description("填写第一页，点击下一步")
    def test_click_next_step(self, cancel_adv):
        cancel_adv(self.app._driver)
        self.goto_lookroom_release().lookroommate_house_rent().lookroommate_upload_photos(). \
            lookroommate_add_photos().lookroommatehouse_choose_photos("2").lookroommate_add_photos().lookroommatehouse_choose_photos("1"). \
            lookroommate_add_photos().lookroommatehouse_choose_photos("3").click_take_picture_complete(). \
            click_title().click_village_name().click_name_search().click_search_result().click_month_rent().click_month_rent_price(). \
            click_month_rent_determine().click_door_model().choose_door_model().func_swipe("房屋配置").click_check_in_time(). \
            choose_check_in_time().choose_have_elevator().choose_housing_allocation().click_next_step().screenshot()

    @allure.description("室友性别选择限男生")
    def test_choose_roommate_gender(self):
        """
        室友性别选择限男生
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_next_step().choose_roommate_gender().screenshot()

    @allure.description("室友期望选择一个人住")
    def test_choose_roommate_expectations(self):
        """
        室友期望选择一个人住
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_next_step().choose_roommate_expectations().screenshot()

    @allure.description("输入补充说明")
    def test_click_added_text(self):
        """
        输入补充说明
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_next_step().click_added_text().screenshot()

    @allure.description("身份选择租户")
    def test_choose_identity(self):
        """
        身份选择租户
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_next_step().func_swipe("先生").choose_identity().screenshot()

    @allure.description("输入姓名")
    def test_chlick_enter_name(self):
        """
        输入姓名
        :return:
        """
        self.goto_lookroom_release().lookroommate_house_rent().click_next_step().func_swipe("先生").click_enter_name().screenshot()

    @allure.description("填写第一页数据和第二页数据点击确认发布按钮")
    def test_chlick_enter_name(self):
        """
        填写第一页数据和第二页数据点击确认发布按钮
        :return:
        """
        self.goto_second_page().choose_roommate_gender().choose_roommate_expectations().click_added_text().func_swipe("先生"). \
            choose_identity().click_enter_name().click_confirm_release().screenshot()


        """
        找室友发布无房求租
        """

    @allure.description("找室友发布点击无房求租")
    def test_click_housing_price(self):
        """
        找室友发布点击无房求租
        :return:
        """
        self.goto_lookroom_release().click_housing_price().screenshot()

    @allure.description("找室友发布无房求租输入标题")
    def test_click_title_input_box(self):
        """
        找室友发布无房求租输入标题
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_title_input_box().screenshot()

    @allure.description("找室友发布无房求租选择期望地点")
    def test_choose_gulou_district(self):
        """
        找室友发布无房求租选择期望地点
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_expect_place().choose_gulou_district().click_expect_place_determine(). \
            screenshot()

    @allure.description("找室友发布无房求租选择租金预算")
    def test_choose_rent_budget(self):
        """
        找室友发布无房求租选择租金预算
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_rent_budget().choose_rent_budget_determine(). \
            screenshot()

    @allure.description("找室友发布无房求租选择入住时间")
    def test_click_check_time(self):
        """
        找室友发布无房求租选择入住时间
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_check_time().click_check_in_time_determine().screenshot()

    @allure.description("找室友发布无房求租选择入住人数")
    def test_click_people_live(self):
        """
        找室友发布无房求租选择入住人数
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_people_live().click_people_live_determine().screenshot()

    @allure.description("找室友发布无房求租选择对房子的期望")
    def test_click_expect_alone_toilet(self):
        """
        找室友发布无房求租选择对房子的期望
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_expect_alone_toilet().screenshot()

    @allure.description("找室友发布无房求租填写第一页点击下一步")
    def test_click_expect_alone_toilet(self):
        """
        找室友发布无房求租填写第一页点击下一步
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_title_input_box().click_expect_place().choose_gulou_district(). \
            click_expect_place_determine().click_rent_budget().choose_rent_budget_determine().click_check_time().click_check_in_time_determine(). \
            click_people_live().click_people_live_determine().click_expect_alone_toilet().click_the_next_step().screenshot()

    @allure.description("找室友发布无房求租选择室友性别")
    def test_choose_gender_boy(self):
        """
        找室友发布无房求租选择室友性别
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_the_next_step().choose_gender_boy().screenshot()

    @allure.description("找室友发布无房求租选择室友期望")
    def test_choose_roommate_expectation_alone(self):
        """
        找室友发布无房求租选择室友期望
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_the_next_step().choose_roommate_expectation_alone().screenshot()

    @allure.description("找室友发布无房求租输入补充说明")
    def test_enter_supplementary_text(self):
        """
        找室友发布无房求租输入补充说明
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_the_next_step().enter_supplementary_text().screenshot()

    @allure.description("找室友发布无房求租输入姓名")
    def test_enter_the_name(self):
        """
        找室友发布无房求租输入姓名
        :return:
        """
        self.goto_lookroom_release().click_housing_price().click_the_next_step().enter_the_name().screenshot()

    @allure.description("找室友发布无房求租填写第一页数据和第二页数据点击确认发布按钮")
    def test_click_confirm_the_release(self):
        """
        找室友发布无房求租填写第一页数据和第二页数据点击确认发布按钮
        :return:
        """
        self.goto_next_page().choose_gender_boy().choose_roommate_expectation_alone().enter_supplementary_text(). \
            enter_the_name().click_confirm_the_release().screenshot()




