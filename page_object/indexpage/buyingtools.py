import allure

from page_object.base_page.base_page import BasePage


class BuyingTools(BasePage):
    """
    购房工具箱页面
    """
    def goto_tools(self, tool="买房流程"):
        """
        购房工具箱页面内容
        :param: tool 工具名称
        :return:
        """
        self._params["tool"] = tool
        with allure.step("购房工具箱点击：" + self._params["tool"]):
            self.steps("../../page_object/indexpage/buyingtools.yaml", replace=True)

        return self
