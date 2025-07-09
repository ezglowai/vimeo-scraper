from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)")
        page = context.new_page()

        page.goto("https://vimeo.com/therealbrokerage")

        # TODO: Auto-click 'Load More' until all videos load
        # TODO: Click each video and download transcript if available

        page.wait_for_timeout(5000)
        browser.close()

run()
