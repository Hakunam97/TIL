import pyautogui

# 1. 카카오톡 위치 파악
pyautogui.mouseInfo()
# 857,1423

# 2. 마우스 이동
pyautogui.moveTo(857,1423, 2)

# 3. 마우스 클릭
pyautogui.click()

# 4. 비밀번호 입력
pyautogui.sleep(10)
pyautogui.write('akstk970216~', interval=0.25)

# 엔터키 입력
pyautogui.press('enter')