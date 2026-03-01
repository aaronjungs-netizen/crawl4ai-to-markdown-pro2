# Use the official Apify Python image which has basic tools pre-installed
FROM apify/actor-python:3.11

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies
# Including crawl4ai and playwright
RUN pip install --no-cache-dir -r requirements.txt

# --- CRITICAL STEPS FOR CRAWL4AI ---
# 1. Install Playwright browsers and their system dependencies (Chromium)
RUN playwright install --with-deps chromium

# 2. Run the crawl4ai-setup to configure the internal environment
RUN crawl4ai-setup

# 3. Optional: Run doctor to verify everything is correct during build
RUN crawl4ai-doctor
# -----------------------------------

# Copy the rest of the Actor source code
COPY . ./

# Start the Actor
CMD ["python3", "-m", "main_apify"]


