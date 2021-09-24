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
                 "./test_businesslist.py",  # 商铺办公列表页面
                 "./test_buyinghouse.py",
                 "./test_buyingtools.py",  # 购房工具页面
                 "./test_checkhouseprice.py",  # 查房价页面
                 "./test_communitydetail.py",  # 找小区详情页面
                 "./test_communitylist.py",  # 找小区列表页面
                 "./test_housedoctor.py",  # 房博士页面
                 "./test_housetour.py",  # 看房团页面
                 "./test_main.py",
                 "./test_mapfindhouse.py",  # 地图找房页面
                 "./test_minepage.py",  # 我的页面
                 "./test_newhousedetail.py",
                 "./test_newhouselist.py",
                 "./test_newslist.py",  # 资讯列表
                 "./test_publishhouse.py",
                 "./test_publishrental.py",  # 租房-发布出租页面
                 "./test_rentbrandapartmentdetail.py",  # 租房-品牌公寓详情页
                 "./test_rentbrandapartmentlist.py",  # 租房-品牌公寓列表
                 "./test_rentfindhouse.py",  # 租房-我要求租
                 "./test_renthouse.py",  # 租房-租房首页
                 "./test_renthousedetail.py",  # 租房-租房房源详情页
                 "./test_renthouselist.py",  # 租房-租房房源列表页
                 "./test_rentlookroommatelist.py",  # 租房-找室友列表
                 "./test_rentlookroommaterelease.py",  # 租房-找室友发布
                 "./test_rentofficebuildingdetail.py",  # 租房-写字楼详情页
                 "./test_rentofficebuildinglist.py",  # 租房-写字楼列表
                 "./test_rentsingleapartmentdetail.py",  # 租房-独栋公寓详情页
                 "./test_rentsingleapartmentlist.py",  # 租房-独栋公寓列表
                 "./test_search.py",
                 "./test_sellhousedetail.py",
                 "./test_sellhouselist.py",
                 # "-m search"
                 ])

    os.system(r"allure generate --clean ./../../TestResult -o ./../../Report")
    os.system(r"allure open ./../../Report")  # 打开测试报告
