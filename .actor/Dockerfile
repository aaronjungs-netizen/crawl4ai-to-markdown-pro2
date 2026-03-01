FROM apify/actor-python:3.11

# Copy everything from your fork into the container
COPY . ./

# Install crawl4ai and apify SDK
RUN pip install -r requirements.txt
RUN pip install apify crawl4ai

# Run the integration script
CMD ["python3", "main_apify.py"]
