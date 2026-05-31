import requests
import time
# from fake_useragent import UserAgent
url="https://www.hotfrog.co.uk/search/austin/food-delivery-services"
session=requests.session()
headers = {
    "Referer": "https://www.hotfrog.co.uk/search/austin/food-delivery-services",
    "sec-ch-ua": '"Chromium";v="144", "Google Chrome";v="144"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}
time.sleep(2)
r=session.get(url,headers=headers)
with open("File.html","w", encoding="utf-8") as f:
    f.write(r.text)