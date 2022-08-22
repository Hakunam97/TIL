# 변수
burger_price = 4750
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price * 2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price * 5) ;


# 함수
def hello():                         # def는 함수정의
    print("""
    Hello!
    Welcome to Codeit!
    """)                        # print 2개를 실행하는 함수 = hello()
    
hello()                         # 지정된 함수 실행

# 파라미터
def hello(name):                # name이 파라미터
    print("Hello!")
    print(name)
    print("Welcome to Codeit!")

hello("Chris")
hello("Michael")

# 여러 개의 파라미터
def print_sum(a, b, c):             # a와 b가 파라미터
    print(a + b + c)      

print_sum(7, 3, 2)       

# return (반환)
def get_square(x):
    return x * x

print(get_square(3)) #1

y = get_square(3) #2
print(y)

print(get_square(3) + get_square(4)) #3

def sum(x, y):
    return(x + y)

print(sum(1, 2) + sum(3, 4))
