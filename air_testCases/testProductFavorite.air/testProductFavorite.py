# -*- encoding=utf8 -*-
# 本用例测试目标：验证商品关注和取消功能正常

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



touch(Template(r"tpl1616478730348.png", record_pos=(0.113, -0.78), resolution=(750, 1334)))

touch(Template(r"tpl1616476793394.png", record_pos=(-0.397, -0.188), resolution=(750, 1334)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616406536617.png", record_pos=(-0.06, 0.039), resolution=(750, 1334)))
sleep(1)
touch(Template(r"tpl1616406536617.png", record_pos=(-0.06, 0.039), resolution=(750, 1334)))
sleep(1)

assert_exists(Template(r"tpl1616406554640.png", record_pos=(-0.059, 0.035), resolution=(750, 1334)), "验证商品关注成功")

touch(Template(r"tpl1616406571821.png", record_pos=(-0.057, 0.036), resolution=(750, 1334)))
touch(Template(r"tpl1616406571821.png", record_pos=(-0.057, 0.036), resolution=(750, 1334)))

assert_exists(Template(r"tpl1616406584996.png", record_pos=(0.415, 0.036), resolution=(750, 1334)), "验证取消商品关注成功")



