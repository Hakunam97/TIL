from selenium import webdriver

from selenium.webdriver.common.by import By

import pyautogui

import time

import pyperclip



# 크롬 드라이버 연결

browser = webdriver.Chrome("C:/chromedriver.exe")

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌

browser.get(url) # 페이지 열기

browser.maximize_window() # 화면 최대화



# 아이디 입력창

id = browser.find_element(By.CSS_SELECTOR,"#id")

id.click()

pyperclip.copy("haknam0216")

pyautogui.hotkey("ctrl", "v")

time.sleep(2)



# 비밀번호 입력창

pw = browser.find_element(By.CSS_SELECTOR,"#pw")

pw.click()

pyperclip.copy("akstk0216~")

pyautogui.hotkey("ctrl", "v")

time.sleep(2)



# 로그인 버튼

login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")

login_btn.click()



# 메일함 이동

browser.get("https://mail.naver.com/")

time.sleep(2)



# 메일 쓰기 버튼 클릭

browser.find_element(By.CSS_SELECTOR,"#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()

time.sleep(2)



# 받는사람

browser.find_element(By.CSS_SELECTOR,"#user_input_1").send_keys("haknam0216@naver.com")

time.sleep(2)



# 제목

browser.find_element(By.CSS_SELECTOR,"#subject_title").send_keys("자동화 프로그램 업그레이드!")

time.sleep(2)



# iframe 안으로 들어가기

browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR,"#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe"))



# 내용

browser.find_element(By.CSS_SELECTOR,"div.workseditor-content").send_keys("잘 될까용?")

time.sleep(2)



# iframe 밖으로 나오기

browser.switch_to.default_content()



# 보내기 버튼 클릭

browser.find_element(By.CSS_SELECTOR,"#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()