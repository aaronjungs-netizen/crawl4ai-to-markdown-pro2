import asyncio
from apify import Actor
from crawl4ai import AsyncWebCrawler, BrowserConfig

async def main():
    async with Actor:
        # 1. Get the input
        actor_input = await Actor.get_input() or {}
        
        # 2. Get the list of URL objects
        urls_list = actor_input.get("urls", [])
        
        # 3. Extract the actual string URLs
        urls = [item.get("url") for item in urls_list if item.get("url")]

        if not urls:
            Actor.log.error("No URLs found in input! Check your Input tab.")
            await Actor.fail()
            return

        # 4. Configure Browser for Apify
        browser_cfg = BrowserConfig(
            headless=True,
            extra_args=["--no-sandbox", "--disable-setuid-sandbox"]
        )

        async with AsyncWebCrawler(config=browser_cfg) as crawler:
            for url in urls:
                Actor.log.info(f"Scraping: {url}")
                result = await crawler.arun(url=url)
                
                if result.success:
                    # 5. Push data (Keys must match your output_schema.json)
                    await Actor.push_data({
                        "url": url,
                        "title": result.metadata.get("title", "No Title"),
                        "markdown": result.markdown
                    })
                    Actor.log.info(f"Done: {url}")
        
        Actor.log.info("Actor finished successfully!")

if __name__ == "__main__":
    asyncio.run(main())
