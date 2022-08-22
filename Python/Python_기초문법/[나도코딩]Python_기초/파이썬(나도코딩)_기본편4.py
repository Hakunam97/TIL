# 10-1 예외처리 부터

## 예외처리 : error처리

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
# 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 6
# 두 번째 숫자를 입력하세요 : 삼
# 에러! 잘못된 값을 입력하였습니다.
except ZeroDivisionError as err:    # 값에 0을 넣었을 때 생기는 오류
    print(err)
# division by zero

# try 내부에 있는 문장에 문제가 발생하면 밑에 except에 해당하는 오류가 있으면 그 내부 명령 실행

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:    
    print(err)

except Exception as err:                                             # try에서 오류 발생 했을 때 위의 ValueError, ZeroDivisionError를 제외한 나머지 모든 error에 대해 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)            # err을 추가하면 구체적인 error message를 받음.

#-----------------------------------------------------------

## 의도적 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError    # 오류 발생시 아래 print를 출력하지 않고 except로 넘어감.
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

#-----------------------------------------------------------

## 사용자 정의 예외처리 (직접 error 정의 가능, class ~ (Exception) 사용)

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {}, {}".format(num1, num2))   
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10
# 두 번째 숫자를 입력하세요 : 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5


#-----------------------------------------------------------

## finally : 예외처리 중 무조건 실행되는 구문, 보통 마지막

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {}, {}".format(num1, num2))   
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10
# 두 번째 숫자를 입력하세요 : 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5
# 계산기를 이용해 주셔서 감사합니다.

#-----------------------------------------------------------

## Quiz 동네에 항상 대기 손님이 있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:  # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break    # while문 탈출

#-----------------------------------------------------------

## 모듈 (theater_module.py 참고)

# 같은 폴더 경로에 있음

import theater_module
from travel import thailand
theater_module.price(3) # 3명이 영화 보러 갔을 때 가격
# 3명 가격은 30000원 입니다.
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# 4명 조조 할인 가격은 24000원 입니다.
theater_module.price_soldier(5) # 5명 군인이 영화 보러 갔을 때 가격
# 5명 군인 할인 가격은 20000원 입니다.

import theater_module as mv    # module에 별명을 붙여서 줄임
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
# 위와 같은 값

from theater_module import *    # module 바로 사용
# from random import *
price(3)
price_morning(4)
price_soldier(5)
# 위와 같은 값

from theater_module import price, price_morning   # 필요한 함수만 쓸 수 있음
price(5)
price_morning(6)
# price_soldier 는 오류

from theater_module import price_soldier as price    # price-soldier 를 price 로 별명 지정
price(5)
# 5명 군인 가격은 20000원 입니다.

#-----------------------------------------------------------

## 패키지 : module들을 모아놓은 집합

# travel 폴더와 하위파일 3개를 만듬
import travel.thailand     # 주의할 점 : 맨 뒤 thailand 처럼 모듈이나 패키지만 가능, class나 함수는 바로 import 불가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행
#  (야시장 투어) 50만원

from travel.thailand import ThailandPackage    # travel 패키지 안의 thailand 모듈에서 ThailandPackage라는 class를 import
trip_to = ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

#-----------------------------------------------------------

## __all__

from travel import *    # travel 패키지 안에 import가 되는 공개범위를 설정해줘야함. => __init__.py 에서 지정
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

trip_to = thailand.ThailandPackage()
trip_to.detail()                         # __init__.py 에서 __all__ = ["thailand"] 해야 import 가능
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

#-----------------------------------------------------------

## 모듈 직접 실행 (모듈 테스트를 위해)

# thailand.py로!
# 그 후

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()   
# Thailand 외부에서 모듈 호출
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

#-----------------------------------------------------------

## 패키지, 모듈 위치

import inspect
import random
print(inspect.getfile(random))    # random.py 파일을 찾는 것
# C:\Python310\lib\random.py

print(inspect.getfile(thailand))
# c:\Users\hakna\Desktop\Python_Workspace\파이썬연습_코드잇\TIL\travel\thailand.py

#-----------------------------------------------------------

## pip install : 패키지 설치

# 구글에 pypi 검색, 기존에 있는 여러 패키지를 이용 가능
# Terminal에 "pip install beautifulsoup4" 를 복붙
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# Terminal에 "pip list" 입력하면 설치되어있는 패키지 내용 확인 
# Terminal에 "pip show 패키지명" 입력하면 자세한 정보 확인
# 만약 쓰고 있는 패키지에 업데이트가 필요하면 => Terminal에 pip install --upgrade 패키지명 입력!
# 패키지 삭제 => Terminal에 pip uninstall 패키지명

#-----------------------------------------------------------

## 내장함수 : 따로 import 필요 없이 바로 사용 가능한 함수

# input : 사용자 입력을 받는 함수
 
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random # 외장 함수
print(dir(random)) # random 모듈내에서 쓸 수 있는 함수 표시

lst = [1, 2, 3]
print(dir(lst))  # lst 모듈에서 쓸 수 있는 함수들 표시

# 혹은 구글에 list of python builtins 라고 검색하면 내장 함수 정보 등 확인 가능

#-----------------------------------------------------------

## 외장함수 : 직접 import를 해서 사용해야 하는 함수

# 구글에 list of python modules 를 검색하면 외장함수 목록 확인 가능

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob(*.py))    # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 directory

#-----------------------------------------------------------

## Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 작성
# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com

# 