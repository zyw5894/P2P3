import logging
import os
from logging import handlers
import time
Base_url = "http://user-p2p-test.itheima.net"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = ""
DB_USERNAME = ""
DB_PASSWORD = ""
DB_NAME1 = ""
DB_NAME2 = ""
Base_dir = os.path.dirname(os.path.abspath(__file__))
#初始化日志配置
def init_log_cofig():
    #1、初始化日志对象
    logger = logging.getLogger()

    #2、设置日志级别
    logger.setLevel(logging.INFO)


    #3、创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()
    logfile = "{0}{1}log{2}{3}".format(Base_dir, os.sep, os.sep, "p2p{}.log".format(time.strftime("%Y%m&d-%H%M%S")))

    fh = logging.handlers.TimedRotatingFileHandler(logfile,when='M',interval=5,backupCount=5,encoding='utf-8')
    #4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    #5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)