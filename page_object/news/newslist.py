import allure

from page_object.base_page.base_page import BasePage


class NewsList(BasePage):
    """
    资讯列表页
    """

    def switch_newstab(self, tab_name='导购'):
        """
        切换tab
        :return:
        """
        self._params["newstab"] = tab_name
        with allure.step("切换TAB"):
            self.steps("../../page_object/news/newslist.yaml", replace=True)
        self.tsleep(2)
        return self

    def select_search_result(self, title_text='6.16早知道：'):
        """
        选择搜索结果
        :return:
        """
        self._params["title_name"] = title_text
        with allure.step("选择搜索结果"):
            self.steps("../../page_object/news/newslist.yaml", replace=True)
        self.tsleep(2)
        return self

    def send_search_text(self, send_text='6.16早知道'):
        """
        输入搜索内容
        """
        self._params["send_text"] = send_text
        with allure.step("输入搜索内容"):
            self.steps("../../page_object/news/newslist.yaml", replace=True)
        self.tsleep(2)
        return self

    def click_ad_pic(self):
        """
        点击联版图片
        :return:
        """
        with allure.step("点击联版图片"):
            self.steps("../../page_object/news/newslist.yaml")
        self.tsleep(2)
        return self

    def click_func_entry(self, func_entry="365楼市"):
        """
        点击精选栏目
        :return:
        """
        self._params["func_entry"] = func_entry
        with allure.step("点击精选栏目"):
            self.steps("../../page_object/news/newslist.yaml", replace=True)
        self.tsleep(2)
        return self

    def func_entrance_swipe_left(self, pos_text="燕子矶新城"):
        """
        作为功能入口的左滑，滑到下一屏
        :pos_text: 起点位置的文字
        :return:
        """
        self._params["pos_text"] = pos_text
        with allure.step("点住" + self._params["pos_text"] + "向左滑动到下一屏"):
            self.steps("../../page_object/news/newslist.yaml", replace=True)
        self.tsleep(2)
        return self
