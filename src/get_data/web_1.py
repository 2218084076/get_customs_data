from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")

    # 0× click
    page.locator("html").click()

    # Click body
    page.frame_locator("iframe").locator("body").click()

    # Click a:has-text("导出数据")
    page.frame_locator("iframe").nth(1).locator("a:has-text(\"导出数据\")").click()

    # Click text=确定
    with page.expect_download() as download_info:
        page.frame_locator("iframe").nth(1).locator("text=确定").click()
    download = download_info.value

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
