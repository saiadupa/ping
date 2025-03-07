import time
import requests

URL = "https://bgv-project-status.onrender.com/"

def ping_website():
    while True:
        try:
            response = requests.get(URL)
            print(f"Pinged {URL} | Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to ping {URL}: {e}")
        time.sleep(10)  # Wait for 10 seconds

if __name__ == "__main__":
    ping_website()
