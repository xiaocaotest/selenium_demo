from gevent import monkey

monkey.patch_all()
import gevent
from gevent.pool import Pool


class Coroutine:
    """
    协程封装
    """
    def __init__(self):
        self.pool_num = 2

    def concurrency(self, func, range_list):
        p = Pool(self.pool_num)

        threads = [p.spawn(func, i) for i in range_list]
        gevent.joinall(threads)