import random

### randint 함수
# : 두 수 사이의 어떤 랜덤한 정수를 리턴

print(random.randint(1,20)) # 1 ~ 20 사이 랜덤 정수


### uniform 함수
# : 두 수 사이의 랜덤한 소수를 리턴

print(random.uniform(0, 1)) # 0 ~ 1 사이 랜덤 소수

#------------------------------------------------------------------------------------------

import datetime
# 날짜와 시간

### 값 생성
pi_day = datetime.datetime(2022, 8, 10)
print(pi_day)   # 2022-08-10 00:00:00
print(type(pi_day)) # <class 'datetime.datetime'>

# 시간 정할 수 있음
pi_day = datetime.datetime(2022, 8, 10, 13, 6, 15)
print(pi_day)   # 2022-08-10 13:06:15


### 오늘 날짜
today = datetime.datetime.now()
print(today)    # 2022-08-10 01:12:20.707202
print(type(today))  # <class 'datetime.datetime'>


### timedelta
# : 두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됨
today = datetime.datetime.now()
pi_day = datetime.datetime(2022, 8, 7, 13, 6, 15)
print(today - pi_day)   # 2 days, 12:08:13.735491
print(type(today - pi_day)) # <class 'datetime.timedelta'>

## timedelta를 생성해서 datetime 값에 더해 줄 수도 있음
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)    # 2022-08-10 01:16:09.581860
print(today + my_timedelta) # 2022-08-15 04:26:59.581860


### datetime 값에서 '연도' or '월' 값 추출
today = datetime.datetime.now()

print(today)    
print(today.year)   # 연도
print(today.month)  # 월
print(today.day)    # 일
print(today.hour)   # 시
print(today.minute)     # 분
print(today.second) # 초
print(today.microsecond)    #마이크로초


### datetime 포맷팅 (포맷코드)
# : strftime을 사용하여 바꿀 수 있음
today = datetime.datetime.now()
print(today)    # 2022-08-10 01:20:07.840249
print(today.strftime("%A, %B %dth %Y")) # Wednesday, August 10th 2022

#------------------------------------------------------------------------------------------

### 파일 읽기
with open('chicken.txt', 'r') as f: # 'r'은 read
    print(type(f))  # <class '_io.TextIOWrapper'>
    
    # for line in f:  # 모든 내용 줄 읽기
    #     print(line)


### strip : 문자열의 화이트스페이스(공백) 없애줌
# \n 은 빈 줄 하나 나옴

print("     abc   def     ".strip())    # abc   def
print("    \t   \n   abc   def\n\n\n".strip())  # abc   def

# for line in f:  # 모든 내용 줄 읽기
#     print(line.strip())   # 빈 줄이 사라짐


### split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(".")) # ['1', ' 2', ' 3', ' 4', ' 5', ' 6'], (".") 을 기준으로 파라미터를 나눔
print(my_string.split(". "))    # ['1', '2', '3', '4', '5', '6'], 보다 깔끔하게 나옴

full_name = "Kim, Yuna"
print(full_name.split(",")) # ['Kim', ' Yuna']
print(full_name.split(", "))    # ['Kim', 'Yuna']
name_date = full_name.split(", ")
last_name = name_date[0]
first_name = name_date[1] 
print(first_name, last_name)
