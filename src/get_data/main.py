# coding=utf-8

import logging
import re
import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
import pyautogui
import cv2
import numpy as np


# 578 688 717 683

def read_csv(file_path: str):
    """
    read csv file return list
    :param: csv file path
    :return: id list
    """
    data = pd.read_csv(file_path, usecols=[0], encoding='gbk')
    id_list = []
    for n in data.values.tolist():
        if len(str(n[0])) == 8:
            id_list.append(n[0])
    logging.warning('--- return id list ---')
    return id_list


def browser_action(file_path: str, year: str, start_month: str, end_month: str) -> None:
    """
    browser action
    :param key:
    """
    for key in read_csv(file_path):
        with sync_playwright() as playwright:
            browser = playwright.webkit.launch(headless=False)
            context = browser.new_context()

            # Open new page
            page = context.new_page()

            # Go to http://43.248.49.97/
            page.goto("http://43.248.49.97/")
            time.sleep(1)
            pyautogui.hotkey('win', 'up')
            # Select year
            page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").select_option(f"{year}")
            page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").click()
            page.wait_for_timeout(100)
            # Select start month
            page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").select_option(f"{start_month}")
            page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").click()
            page.wait_for_timeout(100)
            # Select end month
            page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option(f"{end_month}")
            page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").click()
            page.wait_for_timeout(100)
            # Select CODE_TS
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")
            page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()
            page.wait_for_timeout(100)
            # Select ORIGIN_COUNTRY
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").select_option("ORIGIN_COUNTRY")
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").click()
            page.wait_for_timeout(100)
            # Select TRADE_MODE
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").select_option("TRADE_MODE")
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").click()
            # Select TRADE_CO_PORT
            page.wait_for_timeout(100)
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").select_option("TRADE_CO_PORT")
            page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").click()
            page.wait_for_timeout(100)
            # input keywords
            page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").fill(f"{key}")
            page.wait_for_timeout(100)
            # Click text=查询
            page.frame_locator("iframe").nth(1).locator("text=查询").click()
            page.wait_for_timeout(300)
            # Click text=确定
            page.frame_locator("iframe").nth(1).locator("text=确定").click()
            page.wait_for_timeout(2000)
            page.screenshot(path='page.png', full_page=True)
            logging.warning('-- screenshot page --')
            crop_image('page.png')
            time.sleep(1)
            mouse_action(mark_edge('1.jpg'))
            # Close page
            page.wait_for_timeout(300)
            # Click text=确定
            page.frame_locator("iframe").nth(1).frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator(
                "text=确定").click()
            page.wait_for_timeout(200)
            # Click text=返回设置
            page.frame_locator("iframe").nth(1).locator("text=返回设置").click()
            page.wait_for_timeout(500)
            page.close()

            # ---------------------
            # context.close()
            # browser.close()


def mouse_action(x: int):
    """
    mouse movement
    :param x:
    """
    pyautogui.moveTo(919, 675)
    pyautogui.click(919, 675)
    time.sleep(random.uniform(1, 2))
    pyautogui.dragTo(919 + x, 675, duration=random.uniform(1, 2))
    time.sleep(random.uniform(1, 2))


def mark_edge(image_path: str):
    """
    Mark image edges
    :param image_path:
    """
    p = cv2.imread(image_path)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 255])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
    ret, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(p, contours, -1, (0, 0, 255), 3)
    c = list(contours)
    c_max = max(c, key=len)
    print(type(c_max))
    x = c_max[len(c_max) - 1][0][1]
    print(x, type(x))
    return x


def crop_image(image_path: str):
    """
    crop_image and save
    :param page image_path:
    """
    logging.warning('-- crop_image --')
    img = cv2.imread(image_path)
    roi = (727, 268, 310, 154)
    x, y, w, h = (727, 268, 310, 154)
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]
        cv2.imwrite('1.jpg', crop)
        logging.warning('Saved!')


def download():
    page.frame_locator("iframe").nth(1).locator("a:has-text(\"导出数据\")").click()
    # Click text=确定
    with page.expect_download() as download_info:
        page.frame_locator("iframe").nth(1).locator("text=确定").click()
    download = download_info.value

# 830 712 1010712
# mark_edge('1.jpg')
id_list = read_csv('商品参数导出.csv')
print(id_list)
# for d in id_list:
#     browser_action(f'{d}', '2021', '1', '3')
