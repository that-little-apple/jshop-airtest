# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
ST.FIND_TIMEOUT=10  #设置隐式等待时长

auto_setup(__file__)
def notfound():
    print("No target found")
# 本用例测试目标：验证图片热区模块图片显示正常
# 关闭指定app
stop_app("jd.cdyjy.overseas.market.indonesia")
# 回到手机首页
home()

# app上启动目标应用
start_app("jd.cdyjy.overseas.market.indonesia")
wait(Template(r"tpl1616054670703.png", record_pos=(-0.231, -0.11), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616054736845.png", record_pos=(-0.416, -0.653), resolution=(1080, 1920)))
touch(Template(r"tpl1616064206345.png", record_pos=(0.389, 0.679), resolution=(1080, 1920)))
touch(Template(r"tpl1616064223853.png", record_pos=(0.324, 0.244), resolution=(1080, 1920)))
wait(Template(r"tpl1616064239107.png", record_pos=(0.43, -0.456), resolution=(1080, 1920)), timeout=20, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616064264317.png", record_pos=(0.096, -0.756), resolution=(1080, 1920))) 
touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))

wait(Template(r"tpl1616052554321.png", record_pos=(-0.245, -0.069), resolution=(1080, 1920)), timeout=30, interval=3, intervalfunc=notfound)
swipe((600, 1500),(600, 400))
assert_exists(Template(r"tpl1616057724422.png", record_pos=(-0.343, -0.216), resolution=(1080, 1920)))




