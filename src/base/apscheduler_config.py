from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor


executors = {
    'default': ThreadPoolExecutor(2)
}

job_defaults = {
    'max_instances': 2
}

scheduler = BlockingScheduler(
    executors=executors,
    job_defaults=job_defaults,
    timezone='Asia/Shanghai'
)

# if __name__ == '__main__':
#     scheduler.add_job(run, "interval", args=[host, driver_addr, log], seconds=2)
#     scheduler.start()