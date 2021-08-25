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

                 "./test_businesslist.py",
                 "./test_buyinghouse.py",
                 "./test_buyingtools.py",
                 "./test_checkhouseprice.py",
                 "./test_communitydetail.py",
                 "./test_communitylist.py",
                 "./test_housedoctor.py",
                 "./test_housetour.py",
                 "./test_main.py",
                 "./test_mapfindhouse.py",
                 "./test_minepage.py",
                 "./test_newhousedetail.py",
                 "./test_newhouselist.py",
                 "./test_newslist.py",
                 "./test_publishhouse.py",
                 "./test_publishrental.py",
                 "./test_rentbrandapartmentdetail.py",
                 "./test_rentbrandapartmentlist.py",
                 "./test_rentfindhouse.py",
                 "./test_renthouse.py",
                 "./test_renthousedetail.py",
                 "./test_renthouselist.py",
                 "./test_rentlookroommatelist.py",
                 "./test_rentlookroommaterelease.py",
                 "./test_rentofficebuildingdetail.py",
                 "./test_rentofficebuildinglist.py",
                 "./test_rentsingleapartmentdetail.py",
                 "./test_rentsingleapartmentlist.py",
                 "./test_search.py",
                 "./test_sellhousedetail.py",
                 "./test_sellhouselist.py",
                 # "-m search"
                 ])

    os.system(r"allure generate --clean ./../../TestResult -o ./../../Report")
    os.system(r"allure open ./../../Report")  # 打开测试报告
