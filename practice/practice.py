"""reference to https://velog.io/@swhybein/python-BeautifulSoup%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0
"""

import requests
from bs4 import BeautifulSoup

url = "https://seocho.go.kr/site/seocho/CoronaNewsList.do"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')



for i in range(3,10):
    announcement = soup.select('div:nth-child(%d) > div.sectionContent > p:nth-child(1)' %i)
    txt = announcement[0].text
    para = txt.split("\n")
    for sentence in para:
        print(sentence, "\n")
    #para = announcement.split("\n")
    #print(para.find("확진자 경유지 역학조사 결과 미확인 접촉자 발생으로 인하여 확진자의 경유지를 공개합니다"))
