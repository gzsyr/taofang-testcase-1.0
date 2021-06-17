import allure

from page_object.base_page.base_page import BasePage


class PublishMore(BasePage):
    """
    发布房源 最后一步“更多资料”页面
    """

    def click_publishhouse_room(self):
        """
        更多资料页点击户型
        :return:
        """
        with allure.step("更多资料页点击户型"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_cancel(self):
        """
        更多资料页选择点击取消
        :return:
        """
        with allure.step("更多资料页取消选择"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_confirm(self):
        """
        更多资料页选择点击确定
        :return:
        """
        with allure.step("更多资料页确定选择"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_floor(self):
        """
        更多资料页点击楼层
        :return:
        """
        with allure.step("更多资料页点击楼层"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def select_publishhouse_flat(self):
        """
        更多资料页楼层选择点击单层
        :return:
        """
        with allure.step("更多资料页楼层选择点击单层"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def select_publishhouse_jump(self):
        """
        更多资料页楼层选择点击跃层
        :return:
        """
        with allure.step("更多资料页楼层选择点击跃层"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_pictures(self):
        """
        更多资料页点击房屋照片
        :return:
        """
        with allure.step("更多资料页进入房屋照片页"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_prompt(self):
        """
        更多资料页房屋照片点击提示
        :return:
        """
        with allure.step("更多资料页点击房屋照片提示"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_take_pictures(self):
        """
        更多资料页房屋照片选择拍照，拍摄一张
        :return:
        """
        with allure.step("更多资料页房屋照片选择拍照"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_local_pictures(self, keyword='1'):
        """
        更多资料页上传相册图片.默认上传第一张
        :return:
        """
        self._params["index"] = keyword
        with allure.step("更多资料页上传相册图片"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_back(self):
        """
        更多资料页左上角返回
        :return:
        """
        with allure.step("更多资料页子页面左上角返回"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_back_confirm(self):
        """
        更多资料页返回二次确定
        :return:
        """
        with allure.step("更多资料页返回二次确定"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_back_cancel(self):
        """
        更多资料页子页面取消返回
        :return:
        """
        with allure.step("更多资料页子页面取消返回"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_desc(self):
        """
        更多资料页点击房源描述
        :return:
        """
        with allure.step("更多资料页点击房源描述"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_text(self, keyword='电梯房，满五唯一'):
        """
        更多资料页输入文本内容
        :return:
        """
        self._params["text"] = keyword
        with allure.step("更多资料页输入文本内容"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_feature(self):
        """
        更多资料页点击房源特色
        :return:
        """
        with allure.step("更多资料页点击房源特色"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_identity(self):
        """
        更多资料页进入上传证件照页面
        :return:
        """
        with allure.step("更多资料页进入上传证件照页面"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_add_pictures(self, keyword='com.house365.newhouse:id/m_grid_back'):
        """
        更多资料页点击添加图片
        :return:
        """
        self._params["picture_num"] = keyword
        with allure.step("更多资料页添加图片"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_identity_confirm(self):
        """
        更多资料页上传证件照完成
        :return:
        """
        with allure.step("更多资料页上传证件照完成"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_ownership(self):
        """
        更多资料页进入权属认证页
        :return:
        """
        with allure.step("更多资料页进入权属认证页"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def click_publishhouse_ownership_type(self):
        """
        更多资料页-权属认证页-证件类型
        :return:
        """
        with allure.step("更多资料页-权属认证页-证件类型"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def send_publishhouse_ownership_number(self, keyword='宁（2020）市不动产权第0041921号'):
        """
        更多资料页-区属认证-证件号码
        :return:
        """
        self._params["ownership_number"] = keyword
        with allure.step("输入更多资料页-区属认证-证件号码"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
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

    def send_publishhouse_property_owner(self, keyword='钱女士'):
        """
        更多资料页-权属认证-产权人姓名
        :return:
        """
        self._params["property_owner"] = keyword
        with allure.step("更多资料页-权属认证-产权人姓名"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_publishhouse_owner_identity(self, keyword='32011122011252123'):
        """
        更多资料页-权属认证-产权人身份证号
        :return:
        """
        self._params["owner_identity"] = keyword
        with allure.step("更多资料页点击户型"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_publishhouse_submit(self, sec='2'):
        """
        更多资料页完成按钮点击
        :return:
        """
        with allure.step("更多资料页完成按钮点击"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(int(sec))
        return self

    def click_publishhouse_title(self):
        """
        更多资料页点击标题
        :return:
        """
        with allure.step("更多资料页点击标题"):
            self.steps("../../page_object/sellhouse/publishmore.yaml")
        self.tsleep(2)
        return self

    def delay_publishhouse(self, sec='5'):
        """
        等待发布完成
        :return:
        """
        self._params["sec"] = sec
        with allure.step("完成发布房源信息填写，等待发布完成"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def finish_ownership(self, certificate_type="房屋所有权号", number="南京市房权证建邺字第123456号",
                         owner='钱女士', identity='320112199912121234'):
        """
        输入出售房源信息
        默认type="房屋所有权号", number="南京市房权证建邺字第123456号", owner='钱女士', identity='320112199912121234'
        :return:
        """
        self._params["certificate_type"] = certificate_type
        self._params["number"] = number
        self._params["owner"] = owner
        self._params["identity"] = identity
        with allure.step("输入权属认证信息"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self

    def finish_publishhouse(self, desc='房源描述：南北通透，精装修', feature='急售', picture_num='com.house365.newhouse:id/m_grid1',
                            num='1', certificate_type='房屋所有权号', number='宁建邺2020第000123号',
                            owner='吴小', identity='32011234567890'):
        """
        输入出售房源信息
        :return:
        """
        self._params["desc"] = desc
        self._params["feature"] = feature
        self._params["picture_num"] = picture_num
        self._params["num"] = num
        self._params["certificate_type"] = certificate_type
        self._params["number"] = number
        self._params["owner"] = owner
        self._params["identity"] = identity
        with allure.step("输入权属认证信息"):
            self.steps("../../page_object/sellhouse/publishmore.yaml", replace=True)
        self.tsleep(2)
        return self
