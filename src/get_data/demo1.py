import time
import numpy as np
import cv2
from playwright.sync_api import Playwright, sync_playwright, expect

import pyautogui


def mark_edge(image_path: str):
    p = cv2.imread(image_path)
    cv2.imshow('p', p)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 0, 245])  # 提取颜色的低值
    high_hsv = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
    cv2.imshow('mask', mask)

    ret, binary = cv2.threshold(mask, 253, 255, cv2.THRESH_BINARY)
    print(ret)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(p, contours, -1, (0, 0, 255), 3)
    cv2.imshow("img", p)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run(playwright: Playwright, key: str) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")
    time.sleep(1)
    pyautogui.hotkey('win', 'up')
    # 0× click
    page.locator("html").click()
    page.wait_for_timeout(1000)
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
    # image_action('page.png')
    time.sleep(1)
    # mouse_action(mark_edge('1.jpg'))
    # Close page
    page.wait_for_timeout(300)
    page.frame_locator("iframe").first.frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator(
        "text=确定").click()

    page.wait_for_timeout(500)
    page.close()

    # ---------------------
    context.close()
    browser.close()




# with sync_playwright() as playwright:
#     run(playwright, '04063000')
mark_edge('1.jpg')
