import pyautogui

pyautogui.alert("시작하시겠습니까?")    # 팝업창이 뜸

page = pyautogui.prompt("몇 페이지까지 검색?") # 입력창이 뜸
print(page)