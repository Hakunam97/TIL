# numpy : pandas 설치하면 같이 설치됨 (pip install pandas)
# PIL(pillow) : 이미지처리 라이브러리 (pip install pillow)

import numpy
from PIL import Image
# 만약 import PIL 로 불러오면 코드 작성시 PIL.image 로 작성해야하는 번거로움 발생 (가독성)
import os

# 만들 폴더 경로
target = "Python/RPA, Crawling/06_2.랜덤이미지"

# 폴더 만들기
if not os.path.exists(target):
    os.mkdir(target)

for i in range(1, 101):
    filename = f'{i}.jpg'

    # 3차원 rgb 랜덤 배열 생성
    rgb_array = numpy.random.rand(720, 1080, 3) * 255

    # 이미지 생성
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

    # 이미지 저장
    image.save(os.path.join(target, filename)) # 폴더와 파일 이름을 합친다


## 이미지 크기를  반으로 자동 줄이기

import os
from PIL import Image

# 정리할 확장자
extension_list = ['.jpg', '.png', '.jpeg', '.gif']

# 정리할 폴더
target1 = 'Python/RPA, Crawling/06_2.랜덤이미지'

# 만들 폴더
destination = os.path.join(target1, '크기변경')

# 폴더가 없다면 만들기
if not os.path.exists(destination):
    os.mkdir(destination)

# 현재 폴더 내 모든 파일 출력
file_list = os.listdir(target1)

# 반복문 통해 각 파일의 확장자를 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in extension_list:
        # 이미지 열기
        img_path = os.path.join(target1, file)
        img = Image.open(img_path)  # 이미지 객체를 변환하여 img 변수 저장

        # 이미지 크기 수정
        width = int(img.width * 0.5)
        height = int(img.height * 0.5)
        resize = img.resize((width, height))

        # 이미지 저장
        save_path = os.path.join(destination, file)
        resize.save(save_path)   # 크기 변경한 이미지를 저장