FROM apify/actor-python:3.11

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install apify crawl4ai

CMD ["python3", "main_apify.py"]

