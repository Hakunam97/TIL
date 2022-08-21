# 01. 메뉴 만들기

# 올해 코드잇 대학교를 졸업한 영훈이는 배달 어플 회사 “여기오”에 취직했습니다. “여기오”는 고객들이 배달 음식을 주문할 수 있는 어플을 만들려고 합니다. 영훈이가 맡게 된 업무는 어플에서 각 배달 음식 메뉴를 나타낼 클래스를 작성하는 건데요.

# MenuItem 클래스가 가져야할 다음 조건들을 보고 배달 음식 메뉴를 나타내는 MenuItem 클래스를 정의해보세요.

# 인스턴스 변수(타입):
# name(문자열): 메뉴 이름
# price(숫자): 메뉴 가격

# 인스턴스 메소드:
# __init__: MenuItem 클래스의 모든 인스턴스 변수를 초기화한다.
# __str__: MenuItem 인스턴스의 정보를 문자열로 리턴한다. 단, 리턴 형식은 아래의 출력 예시와 같은 형식이어야 한다.

# 출력예시 #
# 햄버거 가격: 4000
# 콜라 가격: 1500
# 후렌치 후라이 가격: 1500


class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{} 가격: {}".format(self.name, self.price)

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)

#------------------------------------------------------------------------------------------


# 02. 속성이 없는 계산기

# 이번 과제에서는 계산기 클래스를 만들어 볼게요. 이때까지 객체는 속성과 행동을 갖는 존재라고 했습니다. 
# 하지만 속성없이 행동만 있는 객체도 있습니다. 이 말은 변수는 없고 메소드만 있는 클래스도 만들 수 있다는 뜻입니다. 
# 우리가 배웠던 메소드의 종류 3가지는

# 인스턴스 메소드
# 클래스 메소드
# 정적 메소드
# 입니다. 변수가 없는 클래스에서는 무슨 메소드를 써야할까요? 이전에 우리는 인스턴스 변수나 클래스 변수를 쓰지 않을 거라면 정적 메소드(static method)를 사용해야 한다고 배웠죠? 변수가 없는 클래스에서는 정적 메소드를 정의하면 됩니다.

# 다음 조건들을 보고 계산기 클래스인 SimpleCalculator 클래스의 정적 메소드들을 완성해보세요.

# 정적 메소드
# add: 파라미터로 받은 두 숫자의 합을 리턴한다
# subtract: 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
# multiply: 파라미터로 받은 두 숫자의 곱을 리턴한다
# divide: 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다


class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        return first_number + second_number
    
    @staticmethod
    def subtract(first_number, second_number):
        return first_number - second_number
    
    @staticmethod
    def multiply(first_number, second_number):
        return first_number * second_number
    
    @staticmethod
    def divide(first_number, second_number):
        return first_number / second_number
    
    
# 계산기 인스턴스 생성
calculator = SimpleCalculator()
    
# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
