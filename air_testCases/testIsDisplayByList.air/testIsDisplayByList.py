# -*- encoding=utf8 -*-
# 本用例测试目标：验证店内搜索关键字能搜索到包含关键字的商品
# 验证商品展示可以切换到一行一列效果
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
touch(Template(r"tpl1616403358114.png", record_pos=(-0.229, -0.399), resolution=(750, 1334)))
touch(Template(r"tpl1616403369047.png", record_pos=(-0.331, -0.784), resolution=(750, 1334)))
text("Nature",enter=False)
touch(Template(r"tpl1616404801770.png", record_pos=(0.425, -0.779), resolution=(750, 1334)))

touch(Template(r"tpl1616405509349.png", record_pos=(0.255, -0.439), resolution=(750, 1334)))

assert_exists(Template(r"tpl1616405519868.png", record_pos=(0.252, -0.444), resolution=(750, 1334)), "验证切换到一行一列效果后，显示当前展示状态")









