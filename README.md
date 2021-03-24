###1、框架脚本文件说明
- run-ios.py   #自动连接ios设备，执行airtest脚本运行和报告生成命令,可完成批量执行脚本，生成汇总和详细测试报告
- run-android.py   #自动连接android设备，执行airtest脚本运行和报告生成命令,可完成批量执行脚本，生成汇总和详细测试报告
- report_tpl.html  #测试报告模板文件
- report.html   #自动生成的测试报告文件，会将汇总的执行结果的json数据与report_tpl.html结合，生成汇总测试报告
- result   #文件夹，用于存放每个测试用例的执行结果，格式为json文件
- devices_name.json #暂未用到，未来可扩展
- xxx.air  #测试用例，所有以.air文件名称结尾的文件夹都是测试用例
- xxx.air/log  #运行用例后自动生成，每次运行会清理上一次留下的文件夹，每个测试用例的日志文件和测试过程截图，以设备号区分，每个设备号下存放一份测试结果日志文件
    - log.html  #运行airtest report命令后自动生成，每个测试用例在每个设备中运行的详细测试报告，即汇总测试报告中点击"点击可查看详情"弹出的页面详情效果
    - log.txt   #运行airtest run命令后自动生成，每个测试用例在每个设备中运行的结果数据，记录下每一步操作，格式为json;使用此数据生成log.html
  
###2、框架运行编写建议
- 执行命令时可以用python3 run-ios/android.py运行整个框架
但是写脚本或者调试脚本时，用airtestIDE来操作，即从airtestIDE中新建编辑.air脚本保存到该框架的根目录下，调试通过后再用run.py进行批量脚本、批量设备去执行。
- 建议ios脚本和安卓脚本以不同分支来维护，因为包名不一样、activityId、poco定位不一样，截图也有可能不一致，脚本无法通用

###3、执行run.py文件前，请参考以下文档，使用电脑连接好手机
Airtest App自动化探索与实践:https://cf.jd.com/pages/viewpage.action?pageId=460223609