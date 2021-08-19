import allure

from test_case.base_test.test_base import TestBase


class TestNewsList(TestBase):
    """
    资讯列表页测试用例
    """
    @allure.description("切换TAB：导购")
    def test_switch_tab(self):
        self.shouye.goto_news_more().switch_newstab().screenshot()

    @allure.description("输入搜索内容：江北核心区")
    def test_search_keywords(self):
        self.shouye.goto_news_more().send_search_text("江北核心区").screenshot()

    @allure.description("点击资讯联版图片")
    def test_click_ad_pic(self):
        self.shouye.goto_news_more().click_ad_pic().screenshot()

    @allure.description("365楼市")
    def test_click_func_entry(self):
        self.shouye.goto_news_more().click_func_entry().screenshot()

    @allure.description("查看全部精选栏目")
    def test_click_func_entry_all(self):
        self.shouye.goto_news_more().func_entrance_swipe_left().click_func_entry("全部").screenshot()

    @allure.description("进入普通资讯详情")
    def test_goto_newsdetail_common(self):
        self.shouye.goto_news_more().send_search_text("重塑楼市").select_search_result("江北核心区").screenshot()

    @allure.description("进入365专题")
    def test_goto_newsdetail_special(self):
        self.shouye.goto_news_more().send_search_text("6.16早知道").select_search_result("江北核心区").screenshot()

    @allure.description("进入直击资讯")
    def test_goto_newsdetail_zhibo(self):
        self.shouye.goto_news_more().send_search_text("直击：2021上半年").select_search_result("龙虎榜").screenshot()

    @allure.description("进入互动话题")
    def test_goto_newsdetail_huati(self):
        self.shouye.goto_news_more().send_search_text("话题热议").select_search_result("三孩").screenshot()

    @allure.description("进入视频说房")
    def test_goto_newsdetail_video(self):
        self.shouye.goto_news_more().send_search_text("什么楼").select_search_result("不能买").screenshot()

    @allure.description("进入淘房点点通")
    def test_goto_newsdetail_audio(self):
        self.shouye.goto_news_more().send_search_text("淘房点点通：开盘潮").select_search_result("领销许").screenshot()

    @allure.description("进入图集资讯")
    def test_goto_newsdetail_pics(self):
        self.shouye.goto_news_more().send_search_text("图集").select_search_result("博鳌").screenshot()

    @allure.description("进入开盘直击")
    def test_goto_newsdetail_kaipan(self):
        self.shouye.goto_news_more().send_search_text("青奥村开盘").select_search_result("普通人").screenshot()
