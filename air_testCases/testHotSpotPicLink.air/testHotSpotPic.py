# -*- encoding=utf8 -*-
# 本用例测试目标：验证图片热区链接（本用例选择商品详情链接）跳转正确
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

touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
assert_exists(Template(r"tpl1616057724422.png", record_pos=(-0.343, -0.216), resolution=(1080, 1920)))
touch(Template(r"tpl1616061290038.png", record_pos=(-0.344, -0.223), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616061306463.png", record_pos=(0.021, -0.738), resolution=(1080, 1920)))







