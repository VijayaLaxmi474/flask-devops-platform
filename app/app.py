from flask import Flask
import logging
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

REQUEST_COUNT = Counter('request_count', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    logging.info("Home endpoint hit")
    return "Hello Vijaya DevOps Project!"

@app.route('/health')
def health():
    return "OK"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
