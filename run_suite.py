import unittest
import app, time
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from script.login import login
from script.realname import realname
from script.register import register
from script.tender import tender
from script.lctest import lctest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))
suite.addTest(unittest.makeSuite(realname))
suite.addTest(unittest.makeSuite(register))
suite.addTest(unittest.makeSuite(tender))
suite.addTest(unittest.makeSuite(lctest))


report_file = app.Base_dir + "/report/report{}.html".format(time.strftime("%Y%m%d %H%M%S"))
with open(report_file, "wb") as f:
    runner = HTMLTestRunner(f, title="p2ptestcaseReport", description="test")
    runner.run(suite)