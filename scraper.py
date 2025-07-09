import feedparser
import requests
from bs4 import BeautifulSoup

def scrape_vimeo():
    print("Scraping Vimeo feed...")

    feed_url = 'https://vimeo.com/therealbrokerage/videos/rss'
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        video_url = entry.link
        print(f"Processing: {video_url}")

        try:
            response = requests.get(video_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            transcript_links = soup.find_all('a', href=True)
            for link in transcript_links:
                if 'transcript.vtt' in link['href']:
                    print(f"Transcript link found: {link['href']}")
                    # Optionally download the file:
                    # transcript = requests.get(link['href']).text
                    # save it somewhere or send to n8n
        except Exception as e:
            print(f"Failed to process {video_url}: {e}")
