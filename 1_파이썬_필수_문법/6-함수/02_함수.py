# 기본형

# 1. 정의하기
import random


def printHello():
    print("Hello")


printHello()  # 호출


# 2. 매개변수가 있는 함수
def sum(a, b):
    print(a + b)


sum(3, 4)  # 호출


# 3. 반환값이 있는 함수
def getRandom():
    number = random.randint(1, 10)

    return number


print(getRandom())


# 4. 매개변수와 반환값이 있는 함수
def add(a, b):
    result = a + b

    return result


print(add(5, 6))
