from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")

    # 0× click
    page.locator("header:has-text(\"海关统计数据在线查询平台 ENGLISH\")").click()

    # Click text=数据查询
    page.locator("text=数据查询").click()

    # Click text=数据查询
    page.locator("text=数据查询").click()

    # Select 2021
    page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").select_option("2021")

    # Select 6
    page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option("6")

    # Click text=--未选择-- 商品 贸易伙伴 贸易方式 收发货人注册地 选择编码 >> nth=0
    page.frame_locator("iframe").nth(1).locator("text=--未选择-- 商品 贸易伙伴 贸易方式 收发货人注册地 选择编码").first.click()

    # Select CODE_TS
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")

    # Select ORIGIN_COUNTRY
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").select_option("ORIGIN_COUNTRY")

    # Select TRADE_MODE
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").select_option("TRADE_MODE")

    # Click text=--未选择-- 商品 贸易伙伴 贸易方式 收发货人注册地 选择编码 >> nth=3
    page.frame_locator("iframe").nth(1).locator("text=--未选择-- 商品 贸易伙伴 贸易方式 收发货人注册地 选择编码").nth(3).click()

    # Select TRADE_CO_PORT
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").select_option("TRADE_CO_PORT")

    # Click input[name="outerValue1"]
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()

    # Fill input[name="outerValue1"]
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").fill("01012100")

    # Click text=查询
    page.frame_locator("iframe").nth(1).locator("text=查询").click()

    # Click text=确定
    page.frame_locator("iframe").nth(1).locator("text=确定").click()

    # Click text=向右滑动模块填充拼图
    page.frame_locator("iframe").nth(1).frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator("text=向右滑动模块填充拼图").click()

    # Click text=向右滑动模块填充拼图
    page.frame_locator("iframe").nth(1).frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator("text=向右滑动模块填充拼图").click()

    # Click a:has-text("导出数据")
    page.frame_locator("iframe").nth(1).locator("a:has-text(\"导出数据\")").click()

    # Click text=确定
    with page.expect_download() as download_info:
        page.frame_locator("iframe").nth(1).locator("text=确定").click()
    download = download_info.value

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=贸易方式名称
    page.frame_locator("iframe").nth(1).locator("text=贸易方式名称").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=返回设置 导出数据
    page.frame_locator("iframe").nth(1).locator("text=返回设置 导出数据").click()

    # Click text=导出数据
    page.frame_locator("iframe").nth(1).locator("text=导出数据").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
