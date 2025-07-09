from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set to True to run in background
        page = browser.new_page()
        page.goto("https://vimeo.com/therealbrokerage", timeout=60000)

        # Keep clicking "Load more" until it disappears
        while True:
            try:
                load_more = page.locator('button:has-text("Load more")')
                if load_more.is_visible():
                    load_more.click()
                    time.sleep(2)
                else:
                    break
            except:
                break

        # Extract all video URLs
        video_links = page.locator('a[href*="/"] >> visible=true').all()
        urls = set()
        for link in video_links:
            href = link.get_attribute("href")
            if href and href.startswith("/"):
                full_url = "https://vimeo.com" + href
                if "/therealbrokerage/" not in full_url:  # skip links to the channel itself
                    urls.add(full_url)

        # Filter to unique video links
        video_ids = [url for url in urls if url.split("/")[-1].isdigit()]
        with open("video_urls.txt", "w") as f:
            for url in video_ids:
                f.write(url + "\n")

        print(f"✅ Extracted {len(video_ids)} video URLs.")
        browser.close()

if __name__ == "__main__":
    run()
