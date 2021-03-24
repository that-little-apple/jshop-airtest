# -*- encoding=utf8 -*-
# 本用例测试目标：
# 验证轮播图图片正确
# 验证轮播图链接跳转正常
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

touch(Template(r"tpl1616478525912.png", record_pos=(-0.397, -0.188), resolution=(750, 1334)))

wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
swipe((600, 1200),(600, 700))
assert_exists(Template(r"tpl1616405673990.png", record_pos=(0.013, 0.313), resolution=(750, 1334)), "验证轮播图显示图1")
assert_exists(Template(r"tpl1616405700620.png", record_pos=(0.011, 0.299), resolution=(750, 1334)), "验证轮播图显示图2")


touch(Template(r"tpl1616061629441.png", record_pos=(-0.001, 0.268), resolution=(1080, 1920)))

assert_exists(Template(r"tpl1616405722523.png", record_pos=(-0.229, -0.223), resolution=(750, 1334)), "验证点击轮播图链接跳转至搜索结果页")










