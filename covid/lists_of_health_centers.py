import requests
from bs4 import BeautifulSoup

url = "https://seocho.go.kr/site/seocho/CoronaNewsList.do"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

    response = requests.get(url, headers = headers)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, "lxml")