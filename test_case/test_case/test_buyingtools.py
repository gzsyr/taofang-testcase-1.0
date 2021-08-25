import allure
import pytest

from test_case.base_test.test_base import TestBase


@allure.feature("淘房APP（android）: 购房工具箱页面的测试")
class TestBuyingTools(TestBase):
    """
    购房工具箱页面测试用例
    """
    @allure.description("点击购房工具")
    @pytest.mark.parametrize("tool", ["买房流程", "购房资格测试", "购房能力评估",
                                      "地图找房", "学校地图", "周边房价",
                                      "房价评估", "看房报名", "楼盘订阅",
                                      "开盘抢先知", "摇号查询", "贷款计算器",
                                      "公积金贷款额度计算", "税费计算器", "提前还款计算器"])
    def test_click_tools(self, tool):
        self.shouye.goto_func_entrance_first("购房工具").goto_tools(tool)
