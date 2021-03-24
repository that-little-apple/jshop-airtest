# -*- encoding=utf8 -*-
__author__ = "xiaoyao62"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# 本用例测试目标： 验证滑动商品模块点击小号more标签跳转搜索结果页，搜索结果按畅销商品排序
# 验证从搜索结果页点击店铺导航，可回到店铺首页
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
touch(Template(r"tpl1616052761553.png", record_pos=(-0.391, -0.348), resolution=(1080, 1920)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
for i in range(2):
    swipe((600, 1500),(600, 400))

touch(Template(r"tpl1616070749895.png", record_pos=(0.375, -0.363), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616070760730.png", record_pos=(-0.281, -0.52), resolution=(1080, 1920)), "点击滑动商品，搜索结果页排序方式显示为Sort by Based on sales")
swipe(Template(r"tpl1616070789232.png", record_pos=(0.006, -0.636), resolution=(1080, 1920)), vector=[0.5, 0])
touch(Template(r"tpl1616070824206.png", record_pos=(-0.386, -0.643), resolution=(1080, 1920)))
wait(Template(r"tpl1616057658578.png", record_pos=(-0.234, -0.219), resolution=(1080, 1920)), timeout=30, interval=2, intervalfunc=notfound)
touch(Template(r"tpl1616070832218.png", record_pos=(-0.27, -0.271), resolution=(1080, 1920)))
assert_exists(Template(r"tpl1616070841124.png", record_pos=(0.318, 0.696), resolution=(1080, 1920)), "验证点击滑动商品跳转商详页")
touch(Template(r"tpl1616070872685.png", record_pos=(-0.423, -0.764), resolution=(1080, 1920)))
swipe(Template(r"tpl1616070889684.png", record_pos=(-0.059, -0.15), resolution=(1080, 1920)), vector=[-0.99, 0.00])
touch(Template(r"tpl1616070922402.png", record_pos=(0.358, -0.08), resolution=(1080, 1920)))

assert_exists(Template(r"tpl1616070760730.png", record_pos=(-0.281, -0.52), resolution=(1080, 1920)), "点击滑动商品，搜索结果页排序方式显示为Sort by Based on sales")

















