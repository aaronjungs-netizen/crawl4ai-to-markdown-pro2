# Crawl4AI Apify Actor

This Actor uses the [Crawl4AI](https://github.com) library to convert any website into clean, LLM-ready Markdown. Optimized for high-speed crawling and bypassing anti-bot protections.

## Features
- **Markdown Conversion**: Get clean content without HTML clutter.
- **Anti-Bot Bypass**: Built-in logic to handle protected sites.
- **LLM Ready**: Perfect for feeding data into OpenAI or Anthropic.

## How to use
1. Enter the list of **URLs** you want to scrape in the Input tab.
2. Select your preferred **Extraction Strategy** (Markdown is default).
3. Click **Start** and wait for the results in the **Dataset** tab.

## Output
The Actor provides a JSON dataset containing:
- `url`: The source link.
- `markdown`: The converted content.
- `success`: Status of the crawl.
