async def main():
    async with Actor:
        # 1. Fetch the input provided by the user
        actor_input = await Actor.get_input() or {}

        # 2. MATCH THE KEY: Use "urls" because that's what is in your input_schema.json
        # We use .get("urls", []) to handle cases where the list might be empty
        urls_input = actor_input.get("urls", [])

        # 3. Handle the 'requestListSources' format (it's a list of dicts)
        # We extract the actual 'url' string from each object
        urls = [item.get("url") for item in urls_input if item.get("url")]

        if not urls:
            Actor.log.error("No URLs provided in the input!")
            await Actor.fail()
            return

        # 4. Now loop through your extracted URLs
        for url in urls:
            Actor.log.info(f"Processing: {url}")
            # ... your Crawl4AI logic goes here ...
