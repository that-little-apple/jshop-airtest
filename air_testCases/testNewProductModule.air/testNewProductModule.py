# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标： 验证重点商品模块点击more标签跳转搜索结果页，搜索结果按新品排序
# 验证滑动导航条可回到店铺首页
# 验证点击重点商品模块内商品，跳转商详页
ST.FIND_TIMEOUT=10  #设置隐式等待时长

auto_setup(__file__)
def notfound():
    print("No target found")
# 本用例测试目标：验证轮播图图片正确
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
touch(Template(r"tpl1616069613720.png", record_pos=(-0.35, -0.584), resolution=(1080, 1920)))
wait(Template(r"tpl1616069138054.png", record_pos=(0.371, 0.419), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616070145324.png", record_pos=(0.384, -0.244), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616070237521.png", record_pos=(-0.311, -0.272), resolution=(1080, 1920)), "点击重点商品more显示Sort by New Arrival")
swipe(Template(r"tpl1616070353442.png", record_pos=(0.005, -0.393), resolution=(1080, 1920)), vector=[0.5, 0.0])
touch(Template(r"tpl1616070390616.png", record_pos=(-0.33, -0.387), resolution=(1080, 1920)))
touch(Template(r"tpl1616070426157.png", record_pos=(-0.43, 0.276), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616070440128.png", record_pos=(0.321, 0.702), resolution=(1080, 1920)), "验证点击重点商品模块商品，跳转商详页")


















