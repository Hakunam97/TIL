import pyautogui
import pyperclip

# 1. 키보드 입력(문자)
pyautogui.write('startcoding', interval=0.25)   # 0.25초마다 한 글자씩 작성

# 2. 키보드 입력(키)
pyautogui.press('enter')
pyautogui.press('up')

# 3. 키보드 입력 (여러개 동시에)
pyautogui.hotkey('ctrl', 'c')

# 4. 한글 입력 방법 (pyperclip 모듈 불러오기)
pyperclip.copy('스타트코딩')
pyautogui.hotkey('ctrl', 'v')   # 복사, 붙여넣기 방식