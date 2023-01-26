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

# 강의 실습 풀이
import os

# 절대 경로 이용
os.mkdir('C:/Users/hakna/Downloads/이미지파일')

# 폴더가 없을 때만 만들기
if not os.path.exists('C:/Users/hakna/Downloads/이미지파일'):
    os.mkdir('C:/Users/hakna/Downloads/이미지파일')

# 현재 폴더 내 모든 파일 출력 (리스트 형태로 출력)
file_list = os.listdir('C:/Users/hakna/Downloads')
print(file_list)

# 반복문 통해 각 파일의 확장자 확인
for file in file_list:
    name, ext = os.path.splitext(file)  # unpacking : 각 원소들을 변수에 하나씩 담는 것

    # tuple_a = os.path.splitext(file)
    # name = tuple_a[0]
    # ext = tuple_a[1]


## 한번에 정리 ##

# 정리할 확장자 리스트
extension_list = ['.jpg', '.png', '.gif', '.jpeg']

# 정리할 폴더
target = "C:/Users/hakna/Downloads"

# 만들 폴더
destination = target + "/이미지파일"

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir(target)

# 반복문을 통해 각 파일의 확장자를 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in extension_list:
        # 파일 이동
        source = os.path.join(target, file)
        os.rename(source, os.path.join(destination, file))