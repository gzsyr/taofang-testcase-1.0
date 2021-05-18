import pytest

from page_object.indexpage.login import Login
from page_object.indexpage.main import Main


@pytest.fixture()
def loginf():
    print("~~~~~loginf~~~~~")
    # setup_module()

    def _login(driver):
        return Login(driver).login()

    return _login

@pytest.fixture()
def logoutf():
    def _logout(driver):
        return Login(driver).logout()

    return _logout


@pytest.fixture()
def cancel_adv():
    """
    关闭首页大屏广告的弹框
    :return:
    """
    def _cancel_adv(driver):
        return Main(driver).cancel_index_adv()

    return _cancel_adv


# # @fixture(scope="session", autouse=True)
# def setup_module():
#     TestBase().setup()
#     print("*******setup*******")

