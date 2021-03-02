import pytest

from page_object.indexpage.login import Login


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

# # @fixture(scope="session", autouse=True)
# def setup_module():
#     TestBase().setup()
#     print("*******setup*******")

