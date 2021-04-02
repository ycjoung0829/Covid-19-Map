#reference to https://velog.io/@swhybein/python-BeautifulSoup%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0

import requests
from bs4 import BeautifulSoup

url = "https://seocho.go.kr/site/seocho/CoronaNewsList.do"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

#contents > div > div:nth-child(3) > div.sectionContent > p:nth-child(1)

announcement = soup.select('div:nth-child(3) > div.sectionContent > p:nth-child(1)')

print(announcement[0].text)