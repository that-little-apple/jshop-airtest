# -*- encoding=utf-8 -*-
# Run Airtest in parallel on multi-device
import json
import os
import shutil
import subprocess
import time
import traceback
import webbrowser

from jinja2 import Environment, FileSystemLoader


def run(devices, airs):
    """"
        run_all     """
    try:
        data_r = []
        global time_s
        time_s = time.time()
        for air in airs:
            results = load_jdon_data(air)
            tasks = run_on_multi_device(devices, air, results)
            for task in tasks:
                status = task['process'].wait()
                results['tests'][task['dev']] = run_one_report(task['air'], task['dev'])
                results['tests'][task['dev']]['status'] = status
                name = air.split(".")[0]
                json.dump(results, open(get_path("result") + os.sep + name + '_data.json', "w"), indent=4)
            data_r.append(results)
        run_summary(data_r)
    except Exception as e:
        traceback.print_exc()


def run_on_multi_device(devices, air, results):
    """
        在多台设备上运行airtest脚本
        Run airtest on multi-device
    """
    tasks = []
    for dev in devices:
        log_dir = get_path("log", dev, air)
        # 命令行执行：airtest run openOrder.air --device ios:///http+usbmux://ed1ecc95f11ef2e24d51eb0ebb587896606e373b --log F:\airtest_code\good_store_project\log\openOrder

        cmd = [
            "airtest",
            "run",
            "air_testCases/" + air,
            "--device",
            dev,
            "--log",
            log_dir
        ]
        try:
            tasks.append({
                'process': subprocess.Popen(cmd, cwd=os.getcwd()),
                'dev': dev,
                'air': air
            })
        except Exception as e:
            traceback.print_exc()
    return tasks


# 点击每个用例的详情页面
def run_one_report(air, dev):
    """"
        生成一个脚本的测试报告
        Build one test report for one air script
    """
    try:
        log_dir = get_path("log", dev, air)
        log = os.path.join(log_dir, 'log.txt')
        if os.path.isfile(log):
            # 命令行执行：airtest report air_testcases/testAddCart.air --log_root /Users/xiaoyao62/airtest/airtest_jdid_ios/air_testCases/testAddCart.air/log/ios_///http+usbmux_//ed1ecc95f11ef2e24d51eb0ebb587896606e373b --lang zh --outfile /Users/xiaoyao62/airtest/airtest_jdid_ios/air_testCases/testAddCart.air/log/ios_///http+usbmux_//ed1ecc95f11ef2e24d51eb0ebb587896606e373b/log.html
            cmd = [
                "airtest",
                "report",
                "air_testCases/" + air,
                "--log_root",
                log_dir,
                "--outfile",
                os.path.join(log_dir, 'log.html'),
                "--lang",
                "zh"
            ]
            # 坑：无法生成报告文件 换用Popen类 ret = subprocess.call(cmd, shell=True, cwd=os.getcwd())
            ret = subprocess.Popen(cmd, cwd=os.getcwd())
            return {
                'status': ret,
                'path': os.path.join(get_path("report", dev, air), 'log.html')
            }
        else:
            print("Report build Failed. File not found in dir %s" % log)
    except Exception as e:
        traceback.print_exc()

    return {'status': -1, 'device': dev, 'path': ''}


def run_summary(data):
    """"
        生成汇总的测试报告
        Build sumary test report
    """
    try:
        for i in data:
            c = get_json_value_by_key(i, "status")

        summary = {
            'time': "%.3f" % (time.time() - time_s),
            'success': c.count(0),
            'count': len(c)
        }
        summary['start_all'] = time.strftime("%Y-%m-%d %H:%M:%S",
                                             time.localtime(time_s))
        summary["result"] = data
        print("summary++++++++++", summary)

        env = Environment(loader=FileSystemLoader(os.getcwd()),
                          trim_blocks=True)
        html = env.get_template('report_tpl.html').render(data=summary)
        with open("report.html", "w", encoding="utf-8") as f:
            f.write(html)
        webbrowser.open("report.html")
    except Exception as e:
        traceback.print_exc()


def load_jdon_data(air):
    """"
        加载进度
            返回一个空的进度数据
    """
    clear_log_dir(air)
    return {
        'start': time.time(),
        'script': air,
        'tests': {}

    }


def clear_log_dir(air):
    """"
        清理log文件夹 airtest_cases/testAddCart.air/log
    """
    log = os.path.join(os.getcwd(), "air_testCases", air, 'log')
    if os.path.exists(log):
        shutil.rmtree(log)

    # 获取key为status的值


def get_json_value_by_key(in_json, target_key, results=[]):
    for key, value in in_json.items():  # 循环获取key,value
        if key == target_key:
            results.append(value)
        if isinstance(value, dict):
            get_json_value_by_key(value, target_key)
    return results

    # 获取路径


def get_path(content, device=None, air="testAddCart.air"):
    root_path = os.getcwd()
    if content == "result":
        # 返回测试报告路径
        path = os.path.join(root_path, "result", "air_testCases")
    elif content == "report":
        # 返回查看详情相对路径
        path = os.path.join("air_testCases", air, 'log', device.replace(".", "_").replace(':', '_'))
    elif content == "log":
        log_dir = os.path.join(root_path, "air_testCases", air, 'log', device.replace(".", "_").replace(':', '_'))
        # 如果没有日志路径则创建一个
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # 返回日志路径
        path = log_dir
    elif content == "air_testCases":
        # 返回测试用例路径
        path = os.path.join(root_path, "air_testCases")
    else:
        # 返回根目录
        path = root_path
    return path

    # 获取路径下所有air的测试用例文件


def get_cases(path):
    cases = []
    root_path = os.getcwd()
    for name in os.listdir(get_path(path)):  # 遍历当前路径下的文件夹和文件名称
        if name.endswith(".air"):
            cases.append(name)
    return cases


def sort_cases(cases, loginAir, outAir):
    # 清除列表中的登录、退出登录，然后将其分别添加到列表的第一位和最后一位
    cases.remove(loginAir)
    cases.remove(outAir)
    cases.insert(0, loginAir)
    cases.insert(len(airs), outAir)
    return cases


if __name__ == '__main__':
    """
        初始化数据
        Init variables here
    """
    # 设置指定设备执行测试用例
    devices = ["ios:///http+usbmux://ed1ecc95f11ef2e24d51eb0ebb587896606e373b"]
    # 获取所有测试用例
    airs = get_cases("air_testCases")
    # 获取指定用例,按顺序执行
    # sort_airs = ["testAddCart.air", "testAllProductModule.air", "testCategoriesModule1.air",
    #              "testCategoriesModule2.air", "testClickRecommendModule.air", "testCustomService.air",
    #              "testDefaultShop.air", "testFavoritShop.air", "testFilterProduct.air",
    #              "testHotSpotPic.air", "testIsDisplayByList.air",
    #              "testLunboPic.air", "testMoreHome.air",
    #              "testMoreShare.air", "testNavModule.air", "testNewProductModule.air",
    #              "testProductFavorite.air", "testSearchByKeyWords.air", "testSearchOrderByPrice.air",
    #              "testShopCategoryPage.air", "testShopCategoryPageLink.air", "testShopHeader.air",
    #              "testSlideProductModule.air"]
    # 获取指定用例,按顺序执行
    sort_airs = ["testAddCart.air"]
    """
        执行脚本
        excute scripts
    """
    # 运行所有脚本
    # run(devices, airs)
    #
    # 运行指定脚本
    run(devices, sort_airs)
