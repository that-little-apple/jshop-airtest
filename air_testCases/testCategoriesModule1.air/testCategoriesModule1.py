# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *

auto_setup(__file__)

def notfound():
    print("No target found")
# 本用例测试目标：验证分类模块功能：
# 向左滑动分类商品模块，出现more标签，点击more跳转店内分类页,显示一级分类名
# 关闭指定app
stop_app("jd.cdyjy.overseas.market.indonesia")
# 回到手机首页
home()

# app上启动目标应用
start_app("jd.cdyjy.overseas.market.indonesia")


touch(Template(r"tpl1616054736845.png", record_pos=(-0.416, -0.653), resolution=(1080, 1920)))
touch(Template(r"tpl1616064206345.png", record_pos=(0.389, 0.679), resolution=(1080, 1920)))
touch(Template(r"tpl1616064223853.png", record_pos=(0.324, 0.244), resolution=(1080, 1920)))
wait(Template(r"tpl1616064239107.png", record_pos=(0.43, -0.456), resolution=(1080, 1920)), timeout=20, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616064264317.png", record_pos=(0.096, -0.756), resolution=(1080, 1920))) 
touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))

wait(Template(r"tpl1616052554321.png", record_pos=(-0.245, -0.069), resolution=(1080, 1920)), timeout=30, interval=3, intervalfunc=notfound)


for i in range(3):    
    swipe((600, 1500),(600, 400))
    sleep(2)

swipe(Template(r"tpl1616052678294.png", record_pos=(-0.02, -0.08), resolution=(1080, 1920)), vector=[-0.99, 0.00])


wait(Template(r"tpl1616047285577.png", record_pos=(0.387, -0.139), resolution=(1080, 1920)), timeout=30, interval=3, intervalfunc=notfound)
touch(Template(r"tpl1616047831518.png", record_pos=(0.382, -0.056), resolution=(1080, 1920)))
sleep(3.0)

assert_exists(Template(r"tpl1616052911458.png", record_pos=(-0.344, -0.361), resolution=(1080, 1920)))
touch(Template(r"tpl1616047988678.png", record_pos=(-0.456, -0.723), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616048000005.png", record_pos=(0.401, -0.058), resolution=(1080, 1920)))



