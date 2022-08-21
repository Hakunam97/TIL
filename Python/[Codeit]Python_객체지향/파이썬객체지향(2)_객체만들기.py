## __str__메소드 : 
# 어떤 인스턴스를 print함수로 호출할 때 자동으로 실행
# 인스턴스를 출력할 때 원하는 정보를 나오게 할 수 있음

class User:
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드 
        self.name = name
        self.email = email
        self.pw = pw

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4r")

print(user1)    # 사용자: 강영훈, 이메일: younghoon@codeit.kr, 비밀번호: ******
print(user2)    # 사용자: 이윤수, 이메일: yoonsoo@codeit.kr, 비밀번호: ******

#------------------------------------------------------------------------------------------

## 클래스 변수
# count (같은 클래스의 인스턴스들이 서로 공유), 접근시 'class명.변수'로!

class User:
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드 
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1 # 인스턴스를 생성할 때마다 count가 1씩 증가

user1 = User("강영훈", "younghoon@gmail.com", "122345")
user2 = User("이윤수", "yoonsoo@codeit.kr", "341535")
user3 = User("서혜린", "lisa@naver.com", "123qas")

user1.count = 5 # 같은 이름의 인스턴스 변수(count)로 설정 (클래스 변수(User.count)보다 우선적으로)

print(User.count)   # 3

print(user1.count)  # 5
print(user2.count)  # 3
print(user3.count)  # 3

#------------------------------------------------------------------------------------------

## 데코레이터 (decorator) @

def print_hello():
    print("안녕하세요!")

# 새로운 함수 만들기
def add_print_to(original): # 파라미터로 또 다른 함수(original)을 받음, 이 함수는 다른 함수(print_hello)를 꾸며주는 역할 (decorator 함수)
    def wrapper():  
        print("함수 시작")
        original()  # = print_hello()
        print("함수 끝")
    return wrapper  # 또 다른 함수(wrapper)를 return, 실행이 아니라 return만!(출력X)

add_print_to(print_hello)()   # original = print_hello가 들어감, () -> return된 함수를 호출하기 위해!
# 함수 시작
# 안녕하세요!
# 함수 끝

# 또다른 return 함수 출력 형식
print_hello = add_print_to(print_hello) # add_print_to 함수가 새로운 함수를 return. 그 return된 함수(wrapper)를 print_hello 에 넣고
print_hello()   # return된 함수를 호출


## 다른 방식의 데코레이터 함수 작성 (더 간단)

def add_print_to(original):
    def wrapper():  
        print("함수 시작")
        original()  
        print("함수 끝")
    return wrapper

@add_print_to   # print_hello 함수를 add_print_to로 꾸며준다는 뜻 @
def print_hello():
    print("안녕하세요!")

# print_hello = add_print_to(print_hello) 없어도 됌
print_hello()
# 함수 시작
# 안녕하세요!
# 함수 끝

# decorator 함수는 각각의 정의된 함수에 같은 기능을 추가할 때! 유용