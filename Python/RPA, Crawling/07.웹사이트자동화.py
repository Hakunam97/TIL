# 셀레니움 4 사용 (pip install selenium)
# chrome드라이버 자동 업데이트 : webdriver_manager  (pip install webdriver_manager)
#--------------------------------------------------------------------------------------------------------------


## 셀레니움 기본설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기 (터미널)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

# 셀레니움으로 웹브라우저 자동 띄우기
service = Service(executable_path=ChromeDriverManager().install())  # 크롬드라이버 설치
driver = webdriver.Chrome(service=service, options=chrome_options)  # options= 로 브라우저 바로 꺼짐을 방지

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)   # 웹페이지가 로딩 될때까지 5초 기다림
driver.maximize_window()    # 화면 최대화

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")    # 네이버 로그인 주소

#--------------------------------------------------------------------------------------------------------------
## 네이버 자동 로그인

# 네이버 로그인 창에서 F12 -> 구글 개발자 도구 -> Ctri+Shift+C 돋보기 버튼 
# -> '아이디' 부분 클릭 -> 해당하는 Tag를 찾음 (HTML) -> copy selector (비밀번호 과정도 같음)

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id") # #id -> 복사했던 Tag를 붙여넣은 것, # 해당 CSS selector에 맞는 Tag를 자동으로 찾아줌
id.click()  # 클릭
id.send_keys("haknam0216")  # 키보드 입력

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw") 
pw.click()  
pw.send_keys("akstk0216~")  

# 15:58부터 시청!!!