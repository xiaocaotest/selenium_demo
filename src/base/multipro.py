import multiprocessing


class Multiprocess:
    """
    进程封装
    """
    def __init__(self):
        self.num = 2

    def processing(self, func, host, driver_addr, log, item_list):
        pool = multiprocessing.Pool(processes=self.num)

        for item in item_list:
            pool.apply(func, (host, driver_addr, log, item))

        pool.close()
        pool.join()