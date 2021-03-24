# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *

auto_setup(__file__)

def notfound():
    print("No target found")
# 本用例测试目标：验证分类模块功能：
# 验证点击分类模块某分类，跳转对应的搜索结果页,页面包含商品价格信息
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


for i in range(3):    
    swipe((600, 1500),(600, 400))
    sleep(2)

touch(Template(r"tpl1616053385713.png", record_pos=(-0.358, -0.051), resolution=(1080, 1920)))

wait(Template(r"tpl1616053411800.png", record_pos=(-0.243, 0.024), resolution=(1080, 1920)), timeout=30, interval=3, intervalfunc=notfound)
assert_exists(Template(r"tpl1616053452835.png", record_pos=(-0.232, 0.019), resolution=(1080, 1920)))



