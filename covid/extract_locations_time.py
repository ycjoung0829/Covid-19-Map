
import requests
from bs4 import BeautifulSoup

url = "https://seocho.go.kr/site/seocho/CoronaNewsList.do"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

response = requests.get(url, headers = headers)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, "lxml")


##contents > div > div:nth-child(3) > div.sectionContent > p:nth-child(1)

locations = dict()

for page in range(3, 10):
    ann = soup.select('div:nth-child(%d) > div.sectionContent > p:nth-child(1)' %page)
    
    result = ""


    for txt in ann:
        result += txt.text
    start_index = result.find("확진자 경유지 역학조사 결과 미확인 접촉자 발생으로 인하여 확진자의 경유지를 공개합니다")
    end_index = result.find("은 가까운 선별진료소에서 코로나19검사 받으시길 바랍니다.")

    #location paragraph
    loc = result[start_index+48:end_index].strip()
    split_loc = loc.split("\n")

    for locate in split_loc:
        location = locate[2:locate.find(")")+1]
        print(page, location, "\n")
        date = locate[locate.find(")")+3:locate.find("까지")]
        if location not in locations: 
            locations[location] = date


