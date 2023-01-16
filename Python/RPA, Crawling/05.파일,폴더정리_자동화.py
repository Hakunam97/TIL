# 난잡한 파일들을 카테고리에 맞게 폴더에 정리

# 먼저 스스로 만들어보기 ----------------------------------------------------
import os, glob, shutil

# 1. 폴더 만들기
os.mkdir("C:/Users/hakna/Downloads/이미지파일")

# 2. 폴더 내 모든 파일 읽기
dir_path = "C:/Users/hakna/Downloads"

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)

# 3. 파일 확장자 추출
# 우선 파일명 가져오기
os.chdir('C:/Users/hakna/Downloads')

file_names = os.listdir()   # 폴더 내 모든 파일들

for filename in file_names:
    print(os.path.splitext(filename))   # 파일명, 확장자명 분리

# 4. 이미지 파일만 이동
files = glob.iglob(os.path.join('C:/Users/hakna/Downloads', "*.jpg"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, 'C:/Users/hakna/Downloads/이미지파일')

# -----------------------------------------------------------------------

