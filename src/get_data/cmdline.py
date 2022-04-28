"""Cmdline"""
import argparse
import logging
import sys
import threading
import time
from get_data.get_data import main_action

curTime = time.strftime("%Y-%M-%D", time.localtime())  # 记录当前时间
execF = False
ncount = 0


def init_args() -> argparse.Namespace:
    """Init argument and parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--csv_file_path', required=True, help='To query the target file (product ID CSV file)')
    parser.add_argument('-y', '--year', required=True, help='Year to query.')
    parser.add_argument('-s', '--start_month', required=True, help='start month')
    parser.add_argument('-e', '--end_month', required=True, help='End month')
    parser.add_argument('-d', '--dest_file', required=True, help='destination file path')
    return parser.parse_args(sys.argv[1:])


def main():
    """Execute"""
    args = init_args()
    main_action(args.csv_file_path, args.year, args.start_month, args.end_month, args.dest_file)


def timer_task():
    global execF
    global curTime
    global ncount
    logging.debug('timer task %s ' % curTime)
    if execF is False:
        main()
        execF = True
    else:
        destime = time.strftime("%Y-%M-%D", time.localtime())
        if destime > curTime:
            execF = False
            curTime = destime
    ncount += 1
    timer = threading.Timer(5, timer_task)
    timer.start()
    logging.debug('number of executions: %s' % ncount)


if __name__ == '__main__':
    timer = threading.Timer(5, timer_task)
    timer.start()
