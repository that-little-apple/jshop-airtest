# -*- encoding=utf8 -*-
# 本用例测试目标：验证点击店招->更多->home可以回到app首页
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

touch(Template(r"tpl1616472439198.png", record_pos=(-0.396, -0.189), resolution=(750, 1334)))


wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616398156334.png", record_pos=(0.441, -0.787), resolution=(750, 1334)))

touch(Template(r"tpl1616398173801.png", record_pos=(0.187, -0.632), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616398364800.png", record_pos=(-0.403, 0.864), resolution=(750, 1334)), "点击home回到app首页")










