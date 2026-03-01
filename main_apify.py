import asyncio
from apify import Actor
from crawl4ai import AsyncWebCrawler

async def main():
    async with Actor:
        # 1. Get the input from the Apify console
        actor_input = await Actor.get_input() or {}
        urls = actor_input.get("urls", ["https://apify.com"])
        
        if not urls:
            await Actor.fail(reason="No URLs provided in the input.")
            return

        print(f"Starting crawl for {len(urls)} URLs...")

        # 2. Initialize the Crawl4AI crawler
        async with AsyncWebCrawler(verbose=True) as crawler:
            for url in urls:
                print(f"Crawling: {url}")
                
                # 3. Perform the crawl
                result = await crawler.arun(url=url)

                if result.success:
                    # 4. Save the Markdown result to the Apify Dataset
                    await Actor.push_data({
                        "url": url,
                        "markdown": result.markdown,
                        "success": True
                    })
                    print(f"Successfully crawled {url}")
                else:
                    await Actor.push_data({
                        "url": url,
                        "error": result.error_message,
                        "success": False
                    })
                    print(f"Failed to crawl {url}: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
