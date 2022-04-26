# coding=utf-8
import asyncio
import logging
import random
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
import cv2
import numpy as np
import pandas as pd
import pyautogui

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def read_csv(file_path: Path) -> list:
    """
    read csv file return list
    :param: csv file path
    :return: id list
    """
    logging.debug('read csv file%s:' % file_path)
    data = pd.read_csv(file_path, usecols=[0], encoding='gbk')
    id_list = []
    for n in data.values.tolist():
        if len(str(n[0])) == 8:
            id_list.append(n[0])
    logging.debug('return id list ')
    return id_list


def main(file_path: str, year: str, start_month: str, end_month: str) -> None:
    """
    browser action
    :param file_path:
    :param year:
    :param start_month:
    :param end_month:
    """
    playwright = sync_playwright().start()
    browser = playwright.webkit.launch(headless=False)
    page = browser.new_page()
    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")
    title = page.title()
    pyautogui.hotkey('win', 'up')
    logging.debug('page title: %s' % title)
    page.wait_for_timeout(1000)
    for key in read_csv(Path(file_path)):
        logging.debug('find %s' % key)
        page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").select_option(year)
        page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").click()
        page.wait_for_timeout(100)
        # Select start month
        page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").select_option(start_month)
        page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").click()
        page.wait_for_timeout(100)
        # Select end month
        page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option(end_month)
        page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").click()
        page.wait_for_timeout(100)
        # Select CODE_TS
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")
        page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()
        page.wait_for_timeout(100)
        # Select ORIGIN_COUNTRY
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").select_option(
            "ORIGIN_COUNTRY")
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").click()
        page.wait_for_timeout(100)
        # Select TRADE_MODE
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").select_option(
            "TRADE_MODE")
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").click()
        # Select TRADE_CO_PORT
        page.wait_for_timeout(100)
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").select_option(
            "TRADE_CO_PORT")
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
        msg_element = page.locator('#msg')
        logging.debug('msg_element: %s' % msg_element)
        # page.evaluate('document.getElementById("msg").value = "1"')
        text = page.evaluate('document.getElementById("msg").innerText')
        logging.debug('text_msg: %s' % text)
        # Close page
        page.wait_for_timeout(300)
        # Click text=确定
        page.frame_locator("iframe").nth(1).frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator(
            "text=确定").click()
        page.wait_for_timeout(200)
        page.frame_locator("iframe").nth(1).locator("text=返回设置").click()
        page.wait_for_timeout(500)
        page.close()
    logging.debug('playwright stop')
    browser.close()


def mouse_action(x: int):
    """
    mouse movement
    :param x:
    """
    pyautogui.moveTo(919, 675)
    pyautogui.click(919, 675)
    time.sleep(random.uniform(1, 2))
    pyautogui.dragTo(970 + x, 675, duration=random.uniform(0, 1))
    time.sleep(random.uniform(1, 2))


def mark_edge(image_path: str) -> int:
    """
    Mark image edges
    :param image_path:
    """
    e_max = 0
    max_contours = []
    p = cv2.imread(image_path)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 255])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
    ret, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(p, contours, -1, (0, 0, 255), 3)
    for i in contours:
        if len(i) > e_max:
            e_max = len(i)
            max_contours = i.tolist()
    # print(e_max, max_list)
    return max_contours[len(max_contours) - 1][0][0]


def crop_image(image_path: str):
    """
    crop_image and save
    :param page image_path:
    """
    logging.debug('-crop_image-')
    img = cv2.imread(image_path)
    roi = (727, 268, 310, 154)
    x, y, w, h = (727, 268, 310, 154)
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]
        cv2.imwrite('1.jpg', crop)
        logging.debug('Saved!')


def download(page):
    """
    click to download
    """
    page.frame_locator("iframe").nth(1).locator("a:has-text(\"导出数据\")").click()
    # Click text=确定
    with page.expect_download() as download_info:
        page.frame_locator("iframe").nth(1).locator("text=确定").click()
    download_ = download_info.value
    print(download_)


# 830 712 1010712
# mark_edge('1.jpg')

# id_list = read_csv('商品参数导出.csv')
# print(id_list)
# for d in id_list:
main('商品参数导出.csv', '2021', '1', '3')
