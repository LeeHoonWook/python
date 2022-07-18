# 람다 함수란?
# : 이름을 지을 필요도 없을 간단한 형태의 함수

# 기존 함수
def minus_one(a):
    return a-1


# 람다 함수
lambda a: a-1

lambda a: True if a > 0 else False

# 호출
# 1. 함수 자체를 호출

print((lambda a: a-1)(10))


# 2. 변수에 담아서 호출

def minus_one_2(a): return a-1


print(minus_one_2(100))
