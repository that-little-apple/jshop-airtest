# -*- encoding=utf8 -*-
# 本用例测试目标：验证默认店铺组包含重点推荐商品、滑动商品展示、分类图片展示、无限下拉商品模块
# 点击每个tab，查看跳转至对应的搜索结果页
__author__ = "xiaoyao62"
auto_setup(__file__)

from airtest.core.api import *
ST.FIND_TIMEOUT=20  #设置隐式等待时长
def notfound():
    print("No target found")
    
# 关闭指定app
stop_app("com.jdid.iosapp")
# 回到手机首页
home()

# app上启动目标应用
start_app("com.jdid.iosapp")

touch(Template(r"tpl1616398034596.png", record_pos=(0.421, 0.865), resolution=(750, 1334)))

touch(Template(r"tpl1616398235360.png", record_pos=(0.351, 0.124), resolution=(750, 1334)))

wait(Template(r"tpl1616398279074.png", record_pos=(0.435, -0.493), resolution=(750, 1334)), timeout=30, interval=2, intervalfunc=notfound)



touch(Template(r"tpl1616397973918.png", record_pos=(0.111, -0.783), resolution=(750, 1334)))
touch(Template(r"tpl1616478682807.png", record_pos=(-0.393, -0.615), resolution=(750, 1334)))

wait(Template(r"tpl1616402671253.png", record_pos=(0.373, -0.304), resolution=(750, 1334)), timeout=30, interval=2, intervalfunc=notfound)
assert_exists(Template(r"tpl1616402786840.png", record_pos=(-0.312, -0.307), resolution=(750, 1334)), "验证默认店铺显示重点商品模块")

assert_exists(Template(r"tpl1616402805182.png", record_pos=(-0.285, 0.363), resolution=(750, 1334)), "验证默认店铺显示滑动商品模块")

swipe((600, 1200),(600,500))
assert_exists(Template(r"tpl1616402878731.png", record_pos=(-0.349, -0.445), resolution=(750, 1334)), "验证默认店铺显示分类模块")

assert_exists(Template(r"tpl1616479803939.png", record_pos=(-0.293, 0.019), resolution=(750, 1334)), "验证默认店铺显示全部商品模块")













