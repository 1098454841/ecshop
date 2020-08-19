#执行所有脚本
import unittest
from HTMLTestRunner import HTMLTestRunner
#批量匹配用例
discover = unittest.defaultTestLoader.discover(start_dir = './',
                                               pattern = "test*.py",
                                               top_level_dir = None
                                               )
#批量执行生成报告
rpt = "report/"+"report.html"
with open(rpt,"wb")as file:
    runner = HTMLTestRunner(
    stream=file, #测试结果报告文件对象
    description="自动化测试报告详情",
    title="ECshop自动化测试报告")
    runner.run(discover)