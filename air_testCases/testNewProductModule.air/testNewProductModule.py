# -*- encoding=utf8 -*-
# 本用例测试目标： 验证重点商品模块点击more标签跳转搜索结果页，搜索结果按新品排序
# 验证滑动导航条可回到店铺首页
# 验证点击重点商品模块内商品，跳转商详页
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
touch(Template(r"tpl1616477008149.png", record_pos=(-0.395, -0.616), resolution=(750, 1334)))

wait(Template(r"tpl1616406318826.png", record_pos=(0.371, -0.303), resolution=(750, 1334)), timeout=30, interval=2, intervalfunc=notfound)
# 默认点击第一个more
touch(Template(r"tpl1616406332080.png", record_pos=(0.373, -0.301), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616406357063.png", record_pos=(-0.285, -0.325), resolution=(750, 1334)), "验证点击重点商品more，搜索结果页按照Sort by New Arrival排序")
swipe(Template(r"tpl1616406400186.png", record_pos=(0.123, -0.445), resolution=(750, 1334)), vector=[0.5, 0.0])

touch(Template(r"tpl1616406425779.png", record_pos=(-0.327, -0.449), resolution=(750, 1334)))
touch(Template(r"tpl1616406436394.png", record_pos=(-0.428, 0.457), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616406448749.png", record_pos=(0.309, 0.819), resolution=(750, 1334)), "验证点击重点商品模块商品，跳转商详页")



















