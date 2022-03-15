import os
import threading
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.base.log import Log
from src.base.config import Config
from src.base.banner import get_banner
from src.test_driver.boce_driver import BoceDriver


def run(host, driver_addr, log, account, password, url):

    boce_driver = BoceDriver(host, driver_addr, log, account, password, url)

    boce_driver.log.info('>>>>> 开始测试 <<<<<')
    boce_driver.log.debug(f'执行登录操作，账号：{account}，密码：{password}')
    boce_driver.login()

    # boce_driver.log.debug(f'运行初始 - job thread_id-{threading.get_ident()}, process_id-{os.getpid()}')
    #
    # boce_driver.log.debug(f'寻找host输入框并输入host: {url}')
    # boce_driver.find_host_input()
    #
    # boce_driver.log.info('寻找按钮：检测一下，并执行点击操作')
    # boce_driver.find_subm_btn()
    #
    # boce_driver.log.info('等待文案 已检测结束 的出现，并收集整理数据')
    # boce_driver.find_flex_success()
    #
    # boce_driver.log.info('>>>>> 结束测试 <<<<<')
    time.sleep(2)

    boce_driver.tear_down()


if __name__ == '__main__':
    cfg = Config()
    account = cfg.read('boce', 'account')
    password = cfg.read('boce', 'password')
    host = cfg.read("boce", "host")
    driver_addr = cfg.read("boce", "driver_addr")
    host_list = ['www.baidu.com', 'www.google.com']
    max_workers = cfg.read("threading", "max_workers")
    banner_name = cfg.read("banner", "banner_name")

    log = Log().log4()

    setting = {
            'host': host,
            'driver_addr': driver_addr,
            'log': log,
            'account': account,
            'password': password,
            'url': 'www.baidu.com'
        }

    log.info('\n' + get_banner(banner_name))
    # try:
    #     with ThreadPoolExecutor(max_workers=int(max_workers)) as pool:
    #         obj_lst = []
    #         for lst in host_list:
    #             setting['url'] = lst
    #             obj_lst.append(pool.submit(run, **setting))
    #
    #         for result in as_completed(obj_lst):
    #             if result.result():
    #                 log.exception(result)
    #             else:
    #                 log.debug(f'运行结果 - job thread_id-{threading.get_ident()}, process_id-{os.getpid()}：{result}')
    # except BaseException as e:
    #     log.exception(e)
    run(**setting)