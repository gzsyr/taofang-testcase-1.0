# 执行用例的主入口
import os

import pytest

if __name__ == "__main__":
    # delfolder(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots')
    # delfolder(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\result')

    pytest.main(["-v",
                 "-s",
                 # "-rs",
                 # "--show-capture=all",
                 "--alluredir", "./../../TestResult",
                 # "--html=./../testreport.html", "--self-contained-html",
                 # "./test_case/test_house_detail.py",
                 "./test_case/test_main.py::TestMain::test_open_file",
                 # "-m search"
                 ])

    os.system(r"allure generate --clean ./../../TestResult -o ./../../Report")
    os.system(r"allure open ./../Report")  # 打开测试报告
