import asyncio
from apify import Actor
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def main():
    async with Actor:
        # Get user input
        actor_input = await Actor.get_input() or {}
        url = actor_input.get("url", "https://apify.com")

        # Config for Apify's Docker environment
        browser_cfg = BrowserConfig(
            headless=True,
            extra_args=["--no-sandbox", "--disable-setuid-sandbox"]
        )

        try:
            async with AsyncWebCrawler(config=browser_cfg) as crawler:
                # Perform the crawl
                result = await crawler.arun(url=url)

                if result.success:
                    # Save results - KEYS MUST MATCH output_schema.json
                    await Actor.push_data({
                        "url": url,
                        "title": result.metadata.get("title", "No Title"),
                        "markdown": result.markdown
                    })
                    Actor.log.info(f"Successfully scraped: {url}")
                else:
                    Actor.log.error(f"Crawl failed: {result.error_message}")
                    await Actor.fail()

        except Exception as e:
            Actor.log.error(f"Runtime error: {e}")
            await Actor.fail()

if __name__ == "__main__":
    asyncio.run(main())
