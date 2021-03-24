# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标：查看导航模块默认展示首页，全部商品，滑动商品标签
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
touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
assert_exists(Template(r"tpl1616068678158.png", record_pos=(-0.326, -0.394), resolution=(1080, 1920)), "验证导航栏显示首页")
assert_exists(Template(r"tpl1616068702732.png", record_pos=(0.01, -0.393), resolution=(1080, 1920)), "验证导航栏显示全部商品")
assert_exists(Template(r"tpl1616068716157.png", record_pos=(0.35, -0.394), resolution=(1080, 1920)), "验证导航栏显示滑动商品")
touch(Template(r"tpl1616068810205.png", record_pos=(0.006, -0.391), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616068826904.png", record_pos=(-0.346, -0.268), resolution=(1080, 1920)), "点击全部商品，搜索结果页排序方式显示为Sort by Popular")
touch(Template(r"tpl1616068832525.png", record_pos=(0.338, -0.391), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616068841615.png", record_pos=(-0.275, -0.268), resolution=(1080, 1920)), "点击滑动商品，搜索结果页排序方式显示为Sort by Based on sales")
touch(Template(r"tpl1616068854295.png", record_pos=(0.344, -0.388), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616068866313.png", record_pos=(-0.308, -0.269), resolution=(1080, 1920)), "点击重点商品，搜索结果页排序方式显示为Sort by New Arrival")


















