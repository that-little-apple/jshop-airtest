# -*- encoding=utf8 -*-
# 本用例测试目标：店招—关注和取消关注店铺

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
touch(Template(r"tpl1616476902018.png", record_pos=(-0.397, -0.615), resolution=(750, 1334)))


wait(Template(r"tpl1616402671253.png", record_pos=(0.373, -0.304), resolution=(750, 1334)), timeout=30, interval=2, intervalfunc=notfound)
assert_exists(Template(r"tpl1616403143037.png", record_pos=(0.315, -0.555), resolution=(750, 1334)), "验证店铺初始状态为已关注")
touch(Template(r"tpl1616403156262.png", record_pos=(0.313, -0.552), resolution=(750, 1334)))

touch(Template(r"tpl1616403169692.png", record_pos=(0.211, 0.121), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616403189584.png", record_pos=(0.239, -0.553), resolution=(750, 1334)), "验证取消关注成功")

touch(Template(r"tpl1616403203996.png", record_pos=(0.24, -0.556), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616403216033.png", record_pos=(0.315, -0.553), resolution=(750, 1334)), "验证关注店铺成功")















