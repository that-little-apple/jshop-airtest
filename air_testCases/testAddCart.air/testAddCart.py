# -*- encoding=utf8 -*-

__author__ = "xiaoyao62"

from airtest.core.api import *

ST.FIND_TIMEOUT=20  #设置隐式等待时长
auto_setup(__file__)
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

touch(Template(r"tpl1616476748951.png", record_pos=(-0.397, -0.191), resolution=(750, 1334)))


wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
assert_exists(Template(r"tpl1616398645727.png", record_pos=(-0.075, 0.291), resolution=(750, 1334)), "验证商品推荐模块有购物车按钮")














