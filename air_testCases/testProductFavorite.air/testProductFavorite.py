# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标：验证商品关注和取消功能正常

# 唤醒并解锁目标设备,不支持ios
#wake()
# 关闭指定app
stop_app("jd.cdyjy.overseas.market.indonesia")
# 回到手机首页
home()

# app上启动目标应用
start_app("jd.cdyjy.overseas.market.indonesia")


wait(Template(r"tpl1616054670703.png", record_pos=(-0.231, -0.11), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616054736845.png", record_pos=(-0.416, -0.653), resolution=(1080, 1920)))
touch(Template(r"tpl1616054736845.png", record_pos=(-0.416, -0.653), resolution=(1080, 1920)))


text("Toko Sebelah",search=True)
sleep(3)
touch(Template(r"tpl1616061008524.png", record_pos=(-0.127, -0.758), resolution=(1080, 1920)))

touch(Template(r"tpl1616037742658.png", record_pos=(0.073, -0.625), resolution=(1080, 1920)))

    
touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616042762109.png", record_pos=(-0.062, 0.094), resolution=(1080, 1920)))
sleep(2.0)
exists(Template(r"tpl1616042770219.png", record_pos=(-0.056, 0.091), resolution=(1080, 1920)))
sleep(2.0)
touch(Template(r"tpl1616046238387.png", record_pos=(-0.061, 0.089), resolution=(1080, 1920)))
exists(Template(r"tpl1616046250777.png", record_pos=(-0.056, 0.091), resolution=(1080, 1920)))


