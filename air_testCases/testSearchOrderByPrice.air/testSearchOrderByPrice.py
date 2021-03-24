# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标：验证店内搜索关键字能搜索到包含关键字的商品

# 唤醒并解锁目标设备,不支持ios
#wake()
# 关闭指定app
stop_app("jd.cdyjy.overseas.market.indonesia")
# 回到手机首页
home()

# app上启动目标应用
start_app("jd.cdyjy.overseas.market.indonesia")

wait(Template(r"tpl1616054670703.png", record_pos=(-0.231, -0.11), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616065492468.png", record_pos=(-0.415, -0.654), resolution=(1080, 1920)))

touch(Template(r"tpl1616064206345.png", record_pos=(0.389, 0.679), resolution=(1080, 1920)))
touch(Template(r"tpl1616064223853.png", record_pos=(0.324, 0.244), resolution=(1080, 1920)))
wait(Template(r"tpl1616064239107.png", record_pos=(0.43, -0.456), resolution=(1080, 1920)), timeout=20, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616064264317.png", record_pos=(0.096, -0.756), resolution=(1080, 1920))) 
touch(Template(r"tpl1616065406477.png", record_pos=(-0.141, -0.581), resolution=(1080, 1920)))

touch(Template(r"tpl1616038120829.png", record_pos=(-0.291, -0.768), resolution=(1080, 1920)))
touch(Template(r"tpl1616038120829.png", record_pos=(-0.291, -0.768), resolution=(1080, 1920)))


text("Nature",search=True)
wait(Template(r"tpl1616038580366.png", record_pos=(-0.143, -0.276), resolution=(1080, 1920)))
touch(Template(r"tpl1616040633439.png", record_pos=(-0.184, -0.387), resolution=(1080, 1920)))
touch(Template(r"tpl1616040647253.png", record_pos=(-0.278, 0.1), resolution=(1080, 1920)))
exists(Template(r"tpl1616040663623.png", record_pos=(-0.199, -0.388), resolution=(1080, 1920)))










