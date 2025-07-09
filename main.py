import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://vimeo.com/therealbrokerage")
        await page.screenshot(path="example.png")
        await browser.close()

asyncio.run(run())

