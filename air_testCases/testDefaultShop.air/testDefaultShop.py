# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标：验证默认店铺组包含重点推荐商品、滑动商品展示、分类图片展示、无限下拉商品模块
# 点击每个tab，查看跳转至对应的搜索结果页
ST.FIND_TIMEOUT=10  #设置隐式等待时长

auto_setup(__file__)
def notfound():
    print("No target found")
# 本用例测试目标：验证轮播图图片正确
# 关闭指定app
stop_app("jd.cdyjy.overseas.market.indonesia")
# 回到手机首页
home()

# app上启动目标应用
start_app("jd.cdyjy.overseas.market.indonesia")
wait(Template(r"tpl1616054670703.png", record_pos=(-0.231, -0.11), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616054736845.png", record_pos=(-0.416, -0.653), resolution=(1080, 1920)))

touch(Template(r"tpl1616064206345.png", record_pos=(0.389, 0.679), resolution=(1080, 1920)))
touch(Template(r"tpl1616064223853.png", record_pos=(0.324, 0.244), resolution=(1080, 1920)))
wait(Template(r"tpl1616064239107.png", record_pos=(0.43, -0.456), resolution=(1080, 1920)), timeout=20, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616064264317.png", record_pos=(0.096, -0.756), resolution=(1080, 1920))) 
touch(Template(r"tpl1616069104474.png", record_pos=(-0.376, -0.577), resolution=(1080, 1920)))
wait(Template(r"tpl1616069138054.png", record_pos=(0.371, 0.419), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)

assert_exists(Template(r"tpl1616069162929.png", record_pos=(-0.325, -0.249), resolution=(1080, 1920)), "验证默认店铺显示重点商品模块")
assert_exists(Template(r"tpl1616069191889.png", record_pos=(-0.295, 0.419), resolution=(1080, 1920)), "验证默认店铺显示滑动商品模块")
swipe((600, 1500),(600, 400))
assert_exists(Template(r"tpl1616069242398.png", record_pos=(-0.355, 0.326), resolution=(1080, 1920)), "验证默认店铺显示分类模块")
swipe((600, 1500),(600, 400))
assert_exists(Template(r"tpl1616069285393.png", record_pos=(-0.305, -0.064), resolution=(1080, 1920)), "验证默认店铺显示全部商品模块")












