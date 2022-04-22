from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")

    # 0× click
    page.locator("html").click()
    page.wait_for_timeout(1000)
    # Select 3
    page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option("3")
    page.wait_for_timeout(1000)
    # Select CODE_TS
    page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")
    page.wait_for_timeout(1000)
    # Click input[name="outerValue1"]
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()

    # Fill input[name="outerValue1"]
    page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").fill("04063000")

    # Click text=查询
    page.frame_locator("iframe").nth(1).locator("text=查询").click()

    # Click text=确定
    page.frame_locator("iframe").nth(1).locator("text=确定").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
