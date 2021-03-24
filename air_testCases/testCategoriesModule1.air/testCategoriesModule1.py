# -*- encoding=utf8 -*-
# 本用例测试目标：验证分类模块功能：向左滑动分类商品模块，出现more标签，点击more跳转店内分类页,显示一级分类名
# 验证点击分类页返回按钮，回到店铺首页
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

touch(Template(r"tpl1616478605838.png", record_pos=(-0.399, -0.187), resolution=(750, 1334)))

wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)


swipe((600, 1200),(600, 400))

swipe(Template(r"tpl1616399991182.png", record_pos=(-0.017, 0.441), resolution=(750, 1334)), vector=[-0.99, 0.00])

wait(Template(r"tpl1616400343509.png", record_pos=(0.387, 0.411), resolution=(750, 1334)), timeout=30, interval=3, intervalfunc=notfound)

touch(Template(r"tpl1616400376076.png", record_pos=(0.385, 0.409), resolution=(750, 1334)))

sleep(1.0)

assert_exists(Template(r"tpl1616400413590.png", record_pos=(-0.347, -0.393), resolution=(750, 1334)), "验证存在一级分类名")
touch(Template(r"tpl1616400464331.png", record_pos=(-0.457, -0.745), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616400569202.png", record_pos=(0.384, 0.413), resolution=(750, 1334)), "验证点击分类页返回按钮，回到店铺首页")





