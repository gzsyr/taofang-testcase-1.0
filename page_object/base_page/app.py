import subprocess

from appium import webdriver

from page_object.base_page.base_page import BasePage
from page_object.indexpage.main import Main


class App(BasePage):

    _package = "com.house365.newhouse"
    _activity = "com.house365.newhouse.ui.SplashActivity"
    # _activity = "com.house365.newhouse.ui.MainActivity"

    def start(self):
        """
        执行appium连接设备
        :return:self
        """
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"

            devicename = subprocess.check_output("adb devices").split(str.encode("\r\n"))[1].split(str.encode("\t"))[0].decode("UTF-8")
            aa = "adb -P 5037 -s " + devicename + " shell getprop ro.build.version.release"
            version = subprocess.check_output(aa).split(str.encode("\r\n"))[0].decode("UTF-8")
            # adb devices   获取deviceName
            # adb -P 5037 -s 1cd2f6f5 shell getprop ro.build.version.release   获取platformVersion

            # yeshen 模拟器
            # caps["deviceName"] = "127.0.0.1:62001"
            # caps["automationName"] = "UiAutomator1"
            # caps["platformVersion"] = "7.1.2"

            # 小米8
            # caps["deviceName"] = "1682a454"
            # caps["platformVersion"] = "10"

            # # huawei mate 30
            # caps["deviceName"] = "JTK5T20318000225"
            # caps["platformVersion"] = "10.0.0"

            # xiaomi  4C
            # caps["deviceName"] = "2e72982d"
            # caps["platformVersion"] = "7"
            # caps["automationName"] = "UiAutomator1"

            # huaiwei mate9
            # caps["deviceName"] = "3HX0217302003038"
            # caps["platformVersion"] = "9.0"

            # 小米4 lte
            # caps["deviceName"] = "1cd2f6f5"
            # caps["platformVersion"] = "6.0.1"

            caps["deviceName"] = devicename #"1cd2f6f5"
            caps["platformVersion"] = version #"6.0.1"

            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            print("driver is none, 重新建立driver")
        else:
            # self._driver.start_activity(self._package, self._activity)
            self._driver.launch_app()
            print("driver is OK, 不需要重新建立driver")

        self.set_implicity(10)
        print("app -> start")
        return self

    def stop(self):
        """
        关闭连接
        :return:self
        """
        if self._driver is not None:
            self._driver.quit()

    def openapp(self):
        """
        打开执行的app
        :return:self
        """
        if self._driver is not None:
            self._driver.launch_app()
            print("openapp: 执行launch_app")
        else:
            self.start()

        return self

    def closeapp(self):
        """
        关闭执行的app
        :return:self
        """
        if self._driver is not None:
            self._driver.close_app()

    def main(self) -> Main:
        print("app -> main")
        return Main(self._driver)