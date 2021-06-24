import inspect
import json
import os
import time

import allure
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page_object.base_page.handle_wapper import handle_black


class BasePage:
    _driver: WebDriver

    # 数据驱动的设置。类型为字典
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicity(self, sec):
        """
        设置隐式等待
        :param sec: 秒
        :return:
        """
        self._driver.implicitly_wait(sec)

    def screenshot(self, name="tmp.png"):
        """
        等待两秒页面加载完成后，截屏保存
        :param name: 默认为“tmp.png"
        :return:
        """
        self.tsleep(2)  # 等待两秒，让页面加载完成后截图
        self._driver.save_screenshot(name)
        with open(name, "rb") as f:
            content = f.read()
        allure.attach(content, attachment_type=allure.attachment_type.PNG)

    @handle_black
    def find(self, locator, value):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    @handle_black
    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def click(self, locator, value):
        self.find(locator, value).click()
        return self

    def find_elements(self, locator, value, position):
        elements = self._driver.find_elements(locator, value)
        return elements[position]

    def click_element(self, locator, value, position):
        element = self.find_elements(locator, value, position)
        element.click()
        return self

    def swipe_to_buttom(self, text=None):
        """
        text=None:	直接滑动到页面底部
        text!=None:	滑动到text的地方
        """
        device_size = self._driver.get_window_size()
        p_e = self._driver.page_source
        while (1):
            p_s = p_e
            if text != None and (text in p_s):
                break
            s_x = device_size['width'] * 0.5
            s_y = device_size['height'] * 0.80
            e_y = device_size['height'] * 0.6
            self._driver.swipe(s_x, s_y, s_x, e_y, 500)
            p_e = self._driver.page_source
            self.tsleep(1)
            if p_s == p_e:
                print("找到所需要的地方！退出")
                break

        return self

    def swipe_to_left(self, o_x, o_y, text=None):
        """
        根据传入的x、y坐标，向左滑动3/4的屏幕
        :param o_x:
        :param o_y:
        :param text: 滑动到text的时候停止
        :return:
        """
        device_size = self._driver.get_window_size()
        p_e = self._driver.page_source

        if text is not None:
            if text in p_e:
                return self
            else:
                while text not in p_e:
                    d_x = o_x - device_size['width'] * 0.75
                    self._driver.swipe(o_x, o_y, d_x, o_y)
                    p_e = self._driver.page_source
                return self
        else:
            # 直接滑动一屏就停止
            d_x = o_x - device_size['width'] * 0.75
            self._driver.swipe(o_x, o_y, d_x, o_y)
            return self

    def steps(self, path, name=None, replace=False):
        """
        测试步骤 驱动
        :param path: 测试步骤文件的路径
        :param name: 测试步骤文件中的步骤名称，
                    1、默认为None当前方法名称；2、传递参数则使用参数数据
        :param replace: 数据驱动参数，1默认为False，表示没有数据要替换；
                        2传递True，表示需要替换步骤中的数据，使用self._params来设置
                        self._param["key"] = value，对应的yaml文件中使用${key}的形式
        :return:
        """
        with open(path, encoding="utf-8") as f:
            if name is None:
                name = inspect.stack()[1].function  # 可以不通过name来传参，而使用调用的函数名称
            steps = yaml.safe_load(f)[name]
            print(steps)

        if replace:
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            steps = json.loads(raw)
            print(steps)

        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    # 点击事件
                    self.find(step["by"], step["locator"]).click()
                    self.tsleep(1)
                if "send" == action:
                    # 发送文本
                    value = step["value"]
                    self.find(step["by"], step["locator"]).send_keys(value)
                    print(f"send({value})")
                if "press" == action:
                    # 按键操作
                    value = step["value"]
                    self._driver.press_keycode(value)
                if "swipe" == action:
                    # 向下滑动操作
                    value = step["value"]
                    if "buttom" != value:
                        self.swipe_to_buttom(value)
                    else:
                        self.swipe_to_buttom()
                if "len>0" == action:
                    # 查找元素是否存在
                    ele = self.finds(step["by"], step["locator"])
                    return len(ele) > 0
                if "click_pos" == action:
                    # 点击多个元素的第value个
                    pos = int(step["value"])
                    print(pos)
                    eles = self.finds(step["by"], step["locator"])
                    if len(eles) > 0:
                        eles[pos].click()
                if "swipe_left" == action:
                    # 作为功能入口的左滑操作，传入为点击哪个元素开始左滑
                    # pos_value 是存在多个元素时，取第pos_value个元素的位置，从0开始计
                    # value 是滑动到页面有value的时候，停止
                    if 'pos_value' in step.keys():
                        pos = int(step["pos_value"])
                        eles = self.finds(step["by"], step["locator"])
                        print(eles)
                        print(steps)
                        ele_loc = eles[pos].location
                    else:
                        ele_loc = self.find(step["by"], step["locator"]).location
                    x = ele_loc['x']
                    y = ele_loc['y']
                    if 'value' in step.keys():
                        self.swipe_to_left(x, y, step["value"])
                    else:
                        self.swipe_to_left(x, y)
                if "seekbar" == action:
                    # seekbar控件的测试，实例：我要买房页面的价格
                    per = int(step["value"])
                    ele = self.find(step["by"], step["locator"])
                    x = ele.location.get('x')
                    y = ele.location.get('y')
                    w = ele.size.get('width')
                    self._driver.swipe(x, y, w * 0.3, y, 1000)
                    # self._driver
                if "delay" == action:
                    # 延迟时间，单位秒
                    t = int(step["value"])
                    self.tsleep(t)
                if "check_click" == action:
                    # 先判断元素在不在，在的话点击，不在直接返回
                    ele = self.find(step["by"], step["locator"])
                    if len(ele) == 0:
                        print("no element")
                    else:
                        ele.click()

    def back(self, c_name=None):
        """
        点击返回
        :param c_name: 类的实例：1、默认为None，返回为self；2、不为None，则返回c_name
        :return:
        """
        self._driver.back()
        if c_name is None:
            return self
        else:
            return c_name

    def tsleep(self, sec):
        time.sleep(sec)

    def adbshell(self, command):
        os.system(command)

    def getCurrentActivity(self):
        return self._driver.current_activity

    def inPageSource(self, text=None):
        p_e = self._driver.page_source
        if text in p_e:
            return True
        else:
            return False