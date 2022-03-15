import os
import datetime

from loguru import logger

from src.base.config import Config


class Log:

    def __init__(self):
        cfg = Config()
        self.addr = cfg.read("log", "addr")
        self.date = cfg.read("log", "date")
        self.format = cfg.read("log", "format")
        self.encoding = cfg.read("log", "encoding")
        self.retention = cfg.read("log", "retention")

    def log4(self):
        date = datetime.datetime.now().strftime(self.date)

        # 获取日志保存的路径
        log_path = os.path.join(os.path.dirname(os.getcwd()), self.addr)

        # 判断目录是否存在，不存在则创建新的目录
        if not os.path.isdir(log_path):
            os.makedirs(log_path)

        self.log = logger

        self.log.add(f'{log_path}/{date}.log',  # 指定文件
                     format=self.format,
                     encoding=self.encoding,
                     retention=self.retention,  # 设置历史保留时长
                     backtrace=True,  # 回溯
                     diagnose=True,  # 诊断
                     enqueue=True,  # 异步写入
                     # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1 week"
                     # filter="my_module"  # 过滤模块
                     # compression="zip"   # 文件压缩
                     )

        return self.log