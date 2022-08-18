## 클래스 메소드 : 클래스 변수의 값을 읽거나 설정하는 메소드

class User:
    count = 0   # 클래스 변수

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod    # 마치 데코레이터, 첫 번째 파라미터로 클래스가 자동 전달(cls) (self가 아님) <- python규칙!
    def number_of_users(cls):   # cls는 User클래스, cls.count = User.count
        print("총 유저 수는: {}입니다".format(cls.count))


# 인스턴스 생성
user1 = User("강영훈", "younghoon@gmail.com", "122345")
user2 = User("이윤수", "yoonsoo@codeit.kr", "341535")
user3 = User("서혜린", "lisa@naver.com", "123qas")

# 클래스로 클래스 메소드 호출
User.number_of_users()  # 총 유저 수는: 3입니다

# 인스턴스로 클래스 메소드 호출
user1.number_of_users() # 총 유저 수는: 3입니다


## 클래스 메소드 number_of_users는 인스턴스 메소드로 작성 가능
# 이 부분만 수정
#     def number_of_users(self):   # cls는 User클래스, cls.count = User.count
#         print("총 유저 수는: {}입니다".format(User.count))
# User.number_of_users(user1) # 총 유저 수는: 3입니다


# !!! 인스턴스 변수와 클래스 변수 둘 다 쓴다면?
# > 인스턴스 메소드! : 인스턴스 변수, 클래스 변수 모두 사용 가능!
# > 하지만 클래스 메소드는 인스턴스 변수 사용 불가

#------------------------------------------------------------------------------------------

# * 요약 *
# class이름으로 접근하는 경우는 instance이름.변수를 사용하는 것이 당연하지만,
print(User.is_valid_email(user1.email))
# 아래 코드처럼 instance이름으로 접근하는 경우
# 해당 인스턴스의 변수이름만 사용하면  될 것으로 생각되었지만,
# not defined 에러가 나네요.
print(user1.is_valid_email(email))

# 정확히 class이름으로 접근할 떄와 같은 방식으로 사용해야 함.
print(user1.is_valid_email(user1.email)) 


## 정적 메소드
# 정적메소드는 class이름이나 인스턴스 이름을 사용해서 접근할 수 있다
# 인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드라면 정적 메소드로 만들면 됩니다
@staticmethod
def is_valid_email(email_address):
    return "@" in email_address
#------------------------------------------------------------------------------------------

## 문제(예시) ##
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 각 변수에 분리된 문자열 저장
        params_list = string_params.split(",")  # 리스트로 만들기

        name = params_list[0]
        email = params_list[1]
        password = params_list[2]

        # 인스턴스 생성 후 리턴
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):    # 아래보면 이미 리스트 형태
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]

        # 인스턴스 생성 후 리턴
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)  # 강영훈 younghoon@codeit.kr 123456
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)    # 이윤수 yoonsoo@codeit.kr abcdef