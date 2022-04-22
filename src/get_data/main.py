# coding=utf-8
import logging
import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
import pyautogui
import cv2
import numpy as np


# 578 688 717 683

def read_csv(file_path: str):
    """ read csv file return list """
    data_list = []
    data = pd.read_csv(file_path, usecols=[0], encoding='gbk')
    print(data.values.tolist())
    for i in data.values.tolist():
        # 删除非数字部分
        data_list.append(i)
    return data_list


def browser_action(driver: Playwright, key: str) -> None:
    browser = driver.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")
    time.sleep(1)
    pyautogui.hotkey('win', 'up')
    # Select 3
    page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").select_option("2021")
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").click()
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").select_option("1")
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").click()
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option("3")
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").click()
    page.wait_for_timeout(200)
    # Select CODE_TS
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")
    page.wait_for_timeout(200)
    # Click input[name="outerValue1"]
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").select_option("ORIGIN_COUNTRY")
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").click()
    # Select TRADE_MODE
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").select_option("TRADE_MODE")
    page.wait_for_timeout(200)
    # Select TRADE_CO_PORT
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").click()
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").select_option("TRADE_CO_PORT")
    # Fill input[name="outerValue1"]
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").click()
    page.wait_for_timeout(200)
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").fill(f"{key}")
    page.wait_for_timeout(300)
    # Click text=查询
    page.frame_locator("iframe").nth(1).locator("text=查询").click()
    page.wait_for_timeout(300)
    # Click text=确定
    page.frame_locator("iframe").nth(1).locator("text=确定").click()
    page.wait_for_timeout(2000)
    page.screenshot(path='page.png', full_page=True)
    print('=== screenshot page ==')
    image_action('page.png')
    time.sleep(1)
    mouse_action(mark_edge('1.jpg'))
    # Close page
    page.wait_for_timeout(300)

    page.wait_for_timeout(500)
    page.close()

    # ---------------------
    context.close()
    browser.close()


def mouse_action(x: int):
    pyautogui.moveTo(919, 675)
    pyautogui.click(919, 675)
    time.sleep(random.uniform(1, 2))
    pyautogui.dragTo(950 + x, 675, duration=random.uniform(1, 2))
    time.sleep(random.uniform(1, 2))


def mark_edge(image_path: str):
    p = cv2.imread(image_path)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 255])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
    ret, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    cv2.drawContours(p, contours, -1, (0, 0, 255), 3)
    x = contours[len(contours) - 2][0][0]
    x = x.tolist()
    print(len(x))
    x = x[0]
    print(x, type(x))
    return x


def image_action(image_path: str):
    img = cv2.imread(image_path)
    cv2.imshow('original', img)
    roi = (727, 268, 310, 154)
    x, y, w, h = (727, 268, 310, 154)
    print(roi)
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]
        cv2.imshow('crop', crop)
        cv2.imwrite('1.jpg', crop)
        print('Saved!')


# 830 712 1010712
# mark_edge('1.jpg')
id_list = read_csv(r"商品参数导出.csv")
# print(id_list)
# with sync_playwright() as playwright:
#     browser_action(playwright, '04063000')
