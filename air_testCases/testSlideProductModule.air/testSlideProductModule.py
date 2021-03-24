# -*- encoding=utf8 -*-
# 本用例测试目标： 验证滑动商品模块点击小号more标签跳转搜索结果页，搜索结果按畅销商品排序
# 验证从搜索结果页点击店铺导航，可回到店铺首页
# 验证点击重点商品模块内商品，跳转商详页
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
swipe((600, 1200),(600, 600))
sleep(1.0)
touch(Template(r"tpl1616408820097.png", record_pos=(-0.28, -0.347), resolution=(750, 1334)))


assert_exists(Template(r"tpl1616408449536.png", record_pos=(0.316, 0.817), resolution=(750, 1334)), "验证点击滑动商品模块商品跳转商详页")
touch(Template(r"tpl1616408476169.png", record_pos=(-0.432, -0.78), resolution=(750, 1334)))

touch(Template(r"tpl1616408258202.png", record_pos=(0.371, -0.456), resolution=(750, 1334)))

assert_exists(Template(r"tpl1616408268784.png", record_pos=(-0.237, -0.557), resolution=(750, 1334)), "点击滑动商品小more标签，搜索结果页排序方式显示为Sort by Based on sales")
swipe(Template(r"tpl1616408294627.png", record_pos=(0.127, -0.672), resolution=(750, 1334)), vector=[0.5, 0.0])
touch(Template(r"tpl1616408325843.png", record_pos=(-0.321, -0.669), resolution=(750, 1334)))
swipe((600, 1200),(600, 700))
sleep(2.0)
swipe(Template(r"tpl1616409242377.png", record_pos=(-0.109, -0.22), resolution=(750, 1334)), vector=[-0.99, -0.00])



touch(Template(r"tpl1616408659013.png", record_pos=(0.236, 0.24), resolution=(750, 1334)))

assert_exists(Template(r"tpl1616408670197.png", record_pos=(-0.231, -0.556), resolution=(750, 1334)), "验证点击滑动商品，搜索结果页排序方式显示为Sort by Based on sales")


















