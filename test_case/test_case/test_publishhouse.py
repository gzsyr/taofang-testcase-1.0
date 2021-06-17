import allure

from test_case.base_test.test_base import TestBase


class TestPublishHouse(TestBase):
    """
    发布房源相关测试用例
    """
    def goto_publish_index(self):
        """
        首页功能入口进入我要卖房页面
        :return:
        """
        return self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_publish_sell()

    def goto_publish_sell(self):
        """
        我要卖房页面进入出售发布页
        :return:
        """
        return self.goto_publish_index().click_publishindex_m_publish()

    def goto_publish_more(self):
        """
        我要卖房进入更多资料页
        :return:
        """
        # return self.shouye.func_entrance_swipe_left("找小区").goto_func_entrance_publish_sell(). \
        return self.goto_publish_sell().goto_next_all().click_publishhouse_next()

    @allure.description("点击引导页的发布房源按钮")
    def test_click_publish(self):
        """
        点击引导页的发布房源按钮
        :return:
        """
        self.goto_publish_sell().screenshot()

    @allure.description("点击引导页的帮助按钮")
    def test_click_help(self):
        """
        点击引导页的帮助按钮
        :return:
        """
        self.goto_publish_index().click_publishindex_m_help().screenshot()

    @allure.description("点击引导页的服务按钮")
    def test_click_service(self):
        """
        点击引导页的服务按钮
        :return:
        """
        self.goto_publish_index().click_publishindex_m_service().screenshot()

    @allure.description("点击引导页的评估房价按钮")
    def test_click_pinggu_img(self):
        """
        点击引导页的评估房价按钮
        :return:
        """
        self.goto_publish_index().click_publishindex_m_pinggu_img().screenshot()

    @allure.description("点击引导页的学校地图按钮")
    def test_click_xuequ_img(self):
        """
        点击引导页的学校地图按钮
        :return:
        """
        self.goto_publish_index().click_publishindex_m_xuequ_img().screenshot()

    @allure.description("点击引导页的房贷计算器按钮")
    def test_click_jisuanqi_img(self):
        """
        点击引导页的房贷计算器按钮
        :return:
        """
        self.goto_publish_index().click_publishindex_m_jisuanqi_img().screenshot()

    @allure.description("点击出售发布页的重置按钮")
    def test_click_reset(self):
        """
        点击重置按钮
        :return:
        """
        self.goto_publish_sell().click_publishhouse_reset().screenshot()

    @allure.description("选择物业类型-住宅")
    def test_publish_type(self):
        """
        选择物业类型-住宅
        :return:
        """
        self.goto_publish_sell().click_publishhouse_type().\
            select_pubilshhouse_type(house_item="物业类型", house_type="住宅").screenshot()

    @allure.description("点击小区名称-搜索-万科红郡住宅")
    def test_publish_name(self):
        """
        点击小区名称-搜索-万科红郡住宅
        :return:
        """
        self.goto_publish_sell().\
            click_publishhouse_name().send_publishhouse_name_search("万科红郡住宅").\
            select_publishhouse_name_result().screenshot()

    @allure.description("输入楼栋：5栋")
    def test_publish_building(self):
        """
        输入楼栋
        :return:
        """
        self.goto_publish_sell().send_publishhouse_dong("5").screenshot()

    @allure.description("输入单元：1单元")
    def test_publish_unit(self):
        """
        输入单元
        :return:
        """
        self.goto_publish_sell().send_publishhouse_danyuan("5").screenshot()

    @allure.description("输入室：1006室")
    def test_publish_room(self):
        """
        输入室
        :return:
        """
        self.goto_publish_sell().send_publishhouse_shi("1006").screenshot()

    @allure.description("输入售价：400万元")
    def test_publish_price(self):
        """
        输入期望售价
        :return:
        """
        self.goto_publish_sell().send_publishhouse_price("400").screenshot()

    @allure.description("输入面积：116平")
    def test_publish_area(self):
        """
        输入面积
        :return:
        """
        self.goto_publish_sell().send_publishhouse_area("116").screenshot()

    @allure.description("房屋权属-产权房")
    def test_publish_property(self):
        """
        选择房屋权属
        :return:
        """
        self.goto_publish_sell().click_publishhouse_property().\
            select_pubilshhouse_type(house_item="房屋权属", house_type="产权房").screenshot()

    @allure.description("输入称呼：李女士")
    def test_publish_seller(self):
        """
        输入出售人名称
        :return:
        """
        self.goto_publish_sell().send_publishhouse_seller("李女士").screenshot()

    @allure.description("点击出售房源下一步，进入更多资料页")
    def test_publish_more(self):
        """
        点击出售房源下一步，进入更多资料页
        :return:
        """
        self.goto_publish_more().screenshot()

    @allure.description("更多资料页选择户型，1室0厅0卫")
    def test_publish_layout(self):
        """
        更多资料页选择户型
        :return:
        """
        self.goto_publish_more().click_publishhouse_room().click_publishhouse_confirm().screenshot()

    @allure.description("更多资料页选择楼层，单层第1层共1层")
    def test_publish_floor(self):
        """
        更多资料页选择楼层
        :return:
        """
        self.goto_publish_more().click_publishhouse_floor().click_publishhouse_confirm().screenshot()

    @allure.description("更多资料页选择房屋照片，小技巧提示语")
    def test_publish_tip(self):
        """
        更多资料页选择房屋照片，点击小技巧提示语
        :return:
        """
        self.goto_publish_more().click_publishhouse_pictures().click_publishhouse_prompt().screenshot()

    @allure.description("更多资料页上传一张房源图片")
    def test_publish_house_picture(self):
        """
        更多资料页上传一张拍照房源图片
        少于6张图片完成时需二次确定
        :return:
        """
        step1 = self.goto_publish_more().click_publishhouse_pictures().\
            click_publishhouse_add_pictures().send_publishhouse_take_pictures()
        step1.screenshot()
        step2 = step1.click_publishhouse_submit().click_publishhouse_back_confirm()
        step2.screenshot()

    @allure.description("更多资料页输入房源描述：房源特色 满两年 VR看装修 随时看房 核心卖点 此房满两年 楼层好 采光佳 业主诚心出售")
    def test_publish_describe(self):
        """
        更多资料页输入房源描述：房源特色 满两年 VR看装修 随时看房 核心卖点 此房满两年 楼层好 采光佳 业主诚心出售
        :return:
        """
        self.goto_publish_more().click_publishhouse_desc().\
            send_publishhouse_text('房源特色 满两年 VR看装修 随时看房 核心卖点 此房满两年 楼层好 采光佳 业主诚心出售').\
            click_publishhouse_submit().screenshot()

    @allure.description("更多资料页选择房源特色：有钥匙，南北通透，电梯")
    def test_publish_feature(self):
        """
        更多资料页选择房源特色：有钥匙，南北通透，电梯
        :return:
        """
        self.goto_publish_more().click_publishhouse_feature().\
            select_pubilshhouse_type(house_item="房源特色", house_type="有钥匙").\
            select_pubilshhouse_type(house_item="房源特色", house_type="南北通透"). \
            select_pubilshhouse_type(house_item="房源特色", house_type="电梯").\
            click_publishhouse_confirm().screenshot()

    @allure.description("更多资料页上传证件照")
    def test_publish_identity_picture(self):
        """
        更多资料页上传证件照
        :return:
        """
        step1 = self.goto_publish_more().click_publishhouse_identity().\
            click_publishhouse_add_pictures('com.house365.newhouse:id/m_grid1').send_publishhouse_local_pictures('1'). \
            click_publishhouse_add_pictures('com.house365.newhouse:id/m_grid2').send_publishhouse_local_pictures('2'). \
            click_publishhouse_add_pictures('com.house365.newhouse:id/m_grid3').send_publishhouse_local_pictures('3')
        step1.screenshot()
        step1.click_publishhouse_submit().screenshot()

    @allure.description("更多资料页-权属认证，选择不动产权证号")
    def test_publish_ownership_type(self):
        """
        更多资料页-权属认证-选择不动产权证号
        :return:
        """
        self.goto_publish_more().click_publishhouse_ownership().\
            click_publishhouse_ownership_type().\
            select_pubilshhouse_type(house_item="证件类型", house_type="不动产权证号").screenshot()

    @allure.description("更多资料页-权属认证-输入证件号码：宁（2020）城市不动产权第00521454号")
    def test_publish_ownership_number(self):
        """
        更多资料页-权属认证-输入证件号码
        :return:
        """
        self.goto_publish_more().click_publishhouse_ownership().\
            send_publishhouse_ownership_number('宁（2020）城市不动产权第00521454号').screenshot()

    @allure.description("更多资料页-权属认证-输入产权人姓名：吴女士")
    def test_publish_property_owner(self):
        """
        更多资料页-权属认证-输入产权人姓名
        :return:
        """
        self.goto_publish_more().click_publishhouse_ownership().\
            send_publishhouse_property_owner('吴女士').screenshot()

    @allure.description("更多资料页-权属认证-产权人身份证号：32011155212456322")
    def test_publish_owner_identity(self):
        """
        更多资料页-权属认证-产权人身份证号
        :return:
        """
        self.goto_publish_more().click_publishhouse_ownership().\
            send_publishhouse_owner_identity('32011155212456322').screenshot()

    @allure.description("更多资料页完成权属认证填写")
    def test_publish_ownership(self):
        """
        更多资料页完成权属认证填写
        :return:
        """
        step1 = self.goto_publish_more().click_publishhouse_ownership().finish_ownership()
        step1.screenshot()
        step1.click_publishhouse_submit().screenshot()

    @allure.description("更多资料页修改标题")
    def test_publish_title(self):
        """
        更多资料页修改标题
        :return:
        """
        self.goto_publish_more().click_publishhouse_title().\
            send_publishhouse_text('新标题').click_publishhouse_submit().screenshot()

    @allure.description("发布房源")
    def test_publishhouse_all(self):
        """
        发布房源
        :return:
        """
        step1 = self.goto_publish_more().finish_publishhouse()
        step1.screenshot()
        step1.click_publishhouse_submit().screenshot()
