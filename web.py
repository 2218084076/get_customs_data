from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser_type = playwright.webkit
    browser = browser_type.launch(headless=False, slow_mo=100)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")
    page.wait_for_timeout(1000)
    # Click font:has-text("数据查询")
    page.locator("font:has-text(\"数据查询\")").click()
    page.wait_for_timeout(1000)
    # Select CODE_TS
    page.frame_locator("iframe").first.locator("select[name=\"outerField1\"]").select_option("CODE_TS")

    # Select ORIGIN_COUNTRY
    page.frame_locator("iframe").first.locator("select[name=\"outerField2\"]").select_option("ORIGIN_COUNTRY")

    # Select TRADE_MODE
    page.frame_locator("iframe").first.locator("select[name=\"outerField3\"]").select_option("TRADE_MODE")

    # Click #button1
    page.frame_locator("iframe").first.locator("#button1").click()

    # Click text=确认
    page.frame_locator("iframe").first.frame_locator("iframe[name=\"layui-layer-iframe1\"]").locator("text=确认").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
