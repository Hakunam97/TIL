# pyautogul
# 파이썬 마우스 키보드 조작 라이브러리
# 터미널에 pip install pyautogui 입력

import pyautogui
import time

# 1. 화면 크기 출력
print(pyautogui.size())

# 2. 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 3. 마우스 이동

# 한번에 이동
pyautogui.moveTo(300, 200)

# a초 만큼 이동
pyautogui.moveTo(468, 16, 2)    # 2초 동안 이동

# 4. 마우스 클릭
pyautogui.click()
pyautogui.doubleClick()
pyautogui.click('right')
pyautogui.click(clicks=3, interval=1)   # 1초마다 3번 클릭

# 5. 마우스 드래그 
# 786,61 -> 473,65  (01_1.마우스정보보기.py 에서 마우스 위치 정보)
pyautogui.moveTo(786,61, 2) # 2초 동안 이동
pyautogui.dragTo(473,65, 2) # 2초 동안 이동