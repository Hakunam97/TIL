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

## 클래스 변수 1
