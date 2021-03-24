# -*- encoding=utf8 -*-
# 本用例测试目标：查看导航模块默认展示首页，全部商品，滑动商品标签
# 点击每个tab，查看跳转至对应的搜索结果页
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
assert_exists(Template(r"tpl1616405963318.png", record_pos=(-0.331, -0.441), resolution=(750, 1334)), "验证导航栏显示首页")

assert_exists(Template(r"tpl1616405973322.png", record_pos=(0.023, -0.444), resolution=(750, 1334)), "验证导航栏显示全部商品")
assert_exists(Template(r"tpl1616405987082.png", record_pos=(0.359, -0.439), resolution=(750, 1334)), "验证导航栏显示滑动商品")

touch(Template(r"tpl1616405999322.png", record_pos=(0.016, -0.445), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616406013085.png", record_pos=(-0.315, -0.324), resolution=(750, 1334)), "验证点击导航上全部商品项，搜索结果页排序方式显示为Sort by Popular")
touch(Template(r"tpl1616406032984.png", record_pos=(0.356, -0.44), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616406045659.png", record_pos=(-0.251, -0.323), resolution=(750, 1334)), "验证点击导航上滑动商品项，搜索结果页排序方式显示为Sort by Based on sales")

swipe(Template(r"tpl1616406103775.png", record_pos=(-0.127, -0.445), resolution=(750, 1334)), vector=[-0.99, 0.00])
touch(Template(r"tpl1616406127912.png", record_pos=(0.327, -0.445), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616406141308.png", record_pos=(-0.28, -0.327), resolution=(750, 1334)), "点击导航上重点商品项，搜索结果页排序方式显示为Sort by New Arrival")


















