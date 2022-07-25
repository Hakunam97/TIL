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

## 패키지
#
