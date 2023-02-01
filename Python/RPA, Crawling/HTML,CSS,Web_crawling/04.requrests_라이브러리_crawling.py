# requests 설치
# pip install requests

import requests

response = requests.get("https://www.naver.com")    # 서버에 요청을 보내는 것, ""에 url을 넣음
# print(response.status_code) # 응답 코드 : 요청에 대한 응답 상태를 나타냄 (200-정상, 404-페이지찾을수없음)
html = response.text    # text : html 코드를 가지고 있음
# print(html)

# --------------------------------------------------------------------------------------------------------
# 내가 필요한 태그들을 추출해야 함 => beautifulsoup (pip install beautifulsoup)
from bs4 import BeautifulSoup

response = requests.get("https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")    # 네이버 지식인에서 파이썬 검색 후, 글 10개에 대한 제목과 링크를 crawling
html = response.text
soup = BeautifulSoup(html, 'html.parser')  # parser는 html 번역, 분석

# soup.select_one("선택자")   # 선택되는 제일 첫번째 태그 가져옴, ()에 crawling할 태그 
# soup.select("선택자")   # 선택되는 모든 태그를 리스트로 가져옴, ()에 crawling할 태그 

