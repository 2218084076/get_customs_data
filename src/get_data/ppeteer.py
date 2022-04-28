import asyncio
import time

from pyppeteer import launch


# 测试检测webdriver
async def main():
    browser = await launch(headless=False,contentType='application')
    page = await browser.newPage()
    
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 '
        'Safari/537.36')
    cookies = {
        'name': 'WvY7XhIMu0fGS',
        'value': '5OzjQN7Je6EPZOYyYcENEezhqJs7MMKumk_Z8DK47Q4qY2j.Se_XKhL4N5pv1IiIHLS_EX.c_7o_0nLq64LfYJG',
        'domain': '43.248.49.97'
    }
    await page.setCookie(cookies)
    resp = await page.goto('http://43.248.49.97/', timeout=1000)
    resp_staters = resp.status
    print(resp_staters)
    time.sleep(2)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
