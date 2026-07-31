import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_app(url):
    try:
        response = requests.get(url, timeout=5, verify=False)

        if response.status_code == 200:
            print(f"✅ Application is UP: {url}")
        else:
            print(f"⚠️ Application returned status code {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"❌ Application is DOWN: {url}")

if __name__ == "__main__":
    url = input("Enter application URL: ")
    check_app(url)