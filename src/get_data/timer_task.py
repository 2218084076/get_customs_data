import datetime
import time
from threading import Timer

from apscheduler.schedulers.blocking import BlockingScheduler


def timer_task_1():
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("job1: %s" % ts)


def timer_task_2():
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("job2: %s" % ts)


def loopMonitor():
    while True:
        # timer_task()
        # 3s检查一次
        time.sleep(3)


def timerMonitor():
    # timer_task()
    t = Timer(3, timerMonitor)
    t.start()


def APschedulerMonitor():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(timer_task_1, 'interval', minutes=1, id='test_job1')
    # 添加任务,时间间隔5S
    scheduler.add_job(timer_task_2, 'interval', seconds=5, id='test_job2')
    scheduler.start()


APschedulerMonitor()
