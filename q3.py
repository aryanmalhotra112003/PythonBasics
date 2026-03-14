import requests
import time
import logging
from http import HTTPStatus

logging.basicConfig(
    filename="uptime_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",               
    "http://httpstat.us/500",                  
    "https://www.google.com/"                  
]

def check_urls():

    for url in urls:
        try:
            print(f"\nChecking URL: {url}")

            response = requests.get(url, timeout=5)
            status_code = response.status_code

            try:
                status_message = HTTPStatus(status_code).phrase
            except:
                status_message = "Unknown Status"

            print(f"Status Code: {status_code} {status_message}")

            if 400 <= status_code < 500:
                alert = f"ALERT: 4xx error encountered for URL: {url}"
                print(alert)
                logging.warning(alert)

            elif 500 <= status_code < 600:
                alert = f"ALERT: 5xx error encountered for URL: {url}"
                print(alert)
                logging.error(alert)

            else:
                print("The website is UP and running")

        except requests.exceptions.RequestException as e:
            error_msg = f"ERROR: Could not reach {url} | {e}"
            print(error_msg)
            logging.error(error_msg)

while True:
    check_urls()
    print("\nWaiting 10 seconds before next check...\n")
    time.sleep(10)