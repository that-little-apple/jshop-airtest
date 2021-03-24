# -*- encoding=utf8 -*-
# 本用例测试目标：
# 验证店内搜索关键字能搜索到包含关键字的商品
# 验证可以根据条件筛选搜索结果页商品

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
assert_exists(Template(r"tpl1616406865893.png", record_pos=(-0.385, 0.223), resolution=(750, 1334)), "验证搜索结果页商品中包含搜索关键字")

touch(Template(r"tpl1616403421890.png", record_pos=(0.421, -0.439), resolution=(750, 1334)))

wait(Template(r"tpl1616403527248.png", record_pos=(-0.273, -0.629), resolution=(750, 1334)))

swipe((525, 1100),(511, 200))
touch(Template(r"tpl1616405007543.png", record_pos=(-0.001, 0.68), resolution=(750, 1334)))

touch(Template(r"tpl1616404972628.png", record_pos=(0.283, 0.815), resolution=(750, 1334)))
assert_exists(Template(r"tpl1616405025141.png", record_pos=(-0.083, 0.263), resolution=(750, 1334)), "商品容量小于200ml")










