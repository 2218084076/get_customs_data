"""Cmdline"""
from get_data.main import browser_action, read_csv

import argparse
import sys


def init_args() -> argparse.Namespace:
    """Init argument and parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--csv file path', required=True, help='To query the target file (product ID CSV file)')
    parser.add_argument('-y', '--year', required=True, help='Year to query.')
    parser.add_argument('-s', '--start_month', required=True, help='start month')
    parser.add_argument('-e', '--end_month', required=True, help='End month')
    return parser.parse_args(sys.argv[1:])


def main():
    """Execute"""
    args = init_args()
    browser_action(args.product_id, args.year, args.start_month, args.end_month)


if __name__ == '__main__':
    main()
