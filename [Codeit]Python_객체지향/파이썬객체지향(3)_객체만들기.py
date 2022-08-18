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


# 인스턴스 변수와 클래스 변수 둘 다 쓴다면?
# > 인스턴스 메소드! : 인스턴스 변수, 클래스 변수 모두 사용 가능!
# > 하지만 클래스 메소드는 인스턴스 변수 사용 불가