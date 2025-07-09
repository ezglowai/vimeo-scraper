import asyncio
from scraper import scrape_vimeo  # This assumes you already have a scraper.py file with this function defined

async def main():
    await scrape_vimeo()

if __name__ == "__main__":
    asyncio.run(main())
