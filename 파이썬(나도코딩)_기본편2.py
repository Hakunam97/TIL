# 7-1 함수) 부터

## 전달값과 반환값

def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):    # 출금
    if balance >= money:    # 잔액이 출금보다 많으면 (출금 가능)
        print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):    # 저녁에 출금, 수수료가 붙음
    commission = 100    # 수수료 100원
    return commission, balance - money - commission    # 두 개의 값을 ,로 구분하여 반환

balance = 0    # 원래 잔액
balance = deposit(balance, 1000)    # 입금 후 잔액
balance = withdraw(balance, 2000)    # 출금 불가
balance = withdraw(balance, 500)    # 출금 완료
commission, balance = withdraw_night(balance, 500)
print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))

#-----------------------------------------------------------

## 함수 기본값

def profile(name, age, main_lang):
    print("이름: {}\t나이 : {}\t주 사용 언어: {}".format(name, age, main_lang))    # \t 는 간격 띄우기
profile("유재석", 20, "파이썬")
profile("김태우", 25, "자바")
# 이름: 유재석    나이 : 20       주 사용 언어: 파이썬
# 이름: 김태우    나이 : 25       주 사용 언어: 자바

# 같은 학교, 같은 학년, 같은 반, 같은 수업. (이름만 다름)
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {}\t나이 : {}\t주 사용 언어: {}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
# 이름: 유재석    나이 : 17       주 사용 언어: 파이썬
# 이름: 김태호    나이 : 17       주 사용 언어: 파이썬

#-----------------------------------------------------------

## 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)          # '키워드 =' 로 함수 호출도 가능 
profile(main_lang="자바", age = 25, name = "김태호")
# 유재석 20 파이썬
# 김태호 25 자바

#-----------------------------------------------------------

## 가변인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")    # end=" " 는 print문이 끝날 때 줄바꿈을 하지 않음. 이어서 밑 문장을 계속 출력
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# 이름 : 유재석   나이 : 20        Python Java C C++ C#     (한줄에 나옴)
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 위 코드 보다는
def profile(name, age, *language):    # 다변인자 * 사용
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
# 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript 
# 이름 : 김태호   나이 : 25        Kotlin Swift 

#-----------------------------------------------------------

## 지역변수와 전역변수

gun = 10    # 전역변수

def checkpoint(soldier):    # 경계근무 군인수
    gun = 20    # 지역변수
    gun = gun - soldier
    print("[함수 내] 남은 총 : {}".format(gun))

print("전체 총 : {}".format(gun))    # 전체 총 : 10
checkpoint(2)                        # (2명이 경계근무 나감) 남은 총 : 18
print("남은 총 : {}".format(gun))    # 남은 총 : 10


def checkpoint(soldier):    
    global gun     # 전역 공간에 있는 gun 사용
    gun = gun - soldier
    print("[함수 내] 남은 총 : {}".format(gun))

print("전체 총 : {}".format(gun))   
checkpoint(2)                       
print("남은 총 : {}".format(gun))
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

# 일반적인 방법
def checkpoint_ret(gun, soldeirs):
    gun = gun - soldeirs
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun    # 위에 새로 변경된 지역변수 gun을 return

print("전체 총 : {}".format(gun)) 
gun = checkpoint_ret(gun, 2)     # (gun, 2) 에서 gun은 88번줄의 gun
print("남은 총 : {}".format(gun))

# 예시

def std_weight(height, gender):    # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175    # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)    # m 단위로 변환, 소수점 둘째자리까지 표시
print("키 {}cm {}의 표준체중은 {}kg입니다.".format(height, gender, weight))