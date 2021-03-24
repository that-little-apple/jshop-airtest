# -*- encoding=utf8 -*-
# 本用例测试目标：验证店招模块展示店铺名，logo,关注人数和关注按钮

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

touch(Template(r"tpl1616476793394.png", record_pos=(-0.397, -0.188), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616408080835.png", record_pos=(-0.384, -0.608), resolution=(750, 1334)), "验证店招显示店铺logo")
assert_exists(Template(r"tpl1616408087014.png", record_pos=(-0.128, -0.671), resolution=(750, 1334)), "验证店招显示店铺名")
assert_exists(Template(r"tpl1616408091651.png", record_pos=(0.169, -0.553), resolution=(750, 1334)), "验证店招显示关注人数")
assert_exists(Template(r"tpl1616408099818.png", record_pos=(0.368, -0.555), resolution=(750, 1334)), "验证店招显示关注按钮")















