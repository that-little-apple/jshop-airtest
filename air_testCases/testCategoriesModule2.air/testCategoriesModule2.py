# -*- encoding=utf8 -*-
# 验证点击分类模块某分类，跳转对应的搜索结果页,页面包含商品价格信息

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

touch(Template(r"tpl1616476779650.png", record_pos=(-0.392, -0.193), resolution=(750, 1334)))

wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
swipe((600, 1200),(600, 400))

touch(Template(r"tpl1616400788762.png", record_pos=(-0.363, 0.425), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616053452835.png", record_pos=(-0.232, 0.019), resolution=(1080, 1920)))



