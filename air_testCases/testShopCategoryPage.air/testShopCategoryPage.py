# -*- encoding=utf8 -*-
# 本用例测试目标：验证店内分类页店铺logo,店铺名，商品数量，一级分类，二级分类名正确
# 验证二级分类跳转链接正确
# 验证二级分类跳转链接正确
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
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616407585874.png", record_pos=(0.404, 0.684), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616407702585.png", record_pos=(-0.312, -0.747), resolution=(750, 1334)), "验证分类页显示店铺logo")

assert_exists(Template(r"tpl1616407715490.png", record_pos=(-0.301, -0.557), resolution=(750, 1334)), "验证分类页显示全部商品类目")
assert_exists(Template(r"tpl1616407730815.png", record_pos=(-0.305, -0.263), resolution=(750, 1334)), "验证分类页显示二级类目")
assert_exists(Template(r"tpl1616407742151.png", record_pos=(-0.351, -0.392), resolution=(750, 1334)), "验证分类页显示一级类目")
touch(Template(r"tpl1616407914116.png", record_pos=(-0.312, -0.26), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616407921237.png", record_pos=(-0.24, -0.091), resolution=(750, 1334)), "请填写测试点")














