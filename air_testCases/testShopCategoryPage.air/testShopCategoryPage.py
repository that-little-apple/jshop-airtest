# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
ST.FIND_TIMEOUT=10  #设置隐式等待时长

auto_setup(__file__)
def notfound():
    print("No target found")
# 本用例测试目标：验证店内分类页店铺logo,店铺名，商品数量，一级分类，二级分类名正确
# 验证二级分类跳转链接正确
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
touch(Template(r"tpl1616064684731.png", record_pos=(-0.337, 0.699), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616064709455.png", record_pos=(-0.315, -0.729), resolution=(1080, 1920)), "验证分类页显示店铺logo")
assert_exists(Template(r"tpl1616064714615.png", record_pos=(-0.085, -0.726), resolution=(1080, 1920)), "验证分类页显示店铺名")
assert_exists(Template(r"tpl1616064718366.png", record_pos=(-0.305, -0.534), resolution=(1080, 1920)), "验证分类页显示全部商品类目")
assert_exists(Template(r"tpl1616064722244.png", record_pos=(-0.342, -0.361), resolution=(1080, 1920)), "验证分类页显示一级类目")
assert_exists(Template(r"tpl1616064766767.png", record_pos=(-0.321, -0.219), resolution=(1080, 1920)), "验证分类页显示二级类目")












