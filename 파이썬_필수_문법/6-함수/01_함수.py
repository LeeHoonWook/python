# 함수를 사용하는 이유
'''
1. 재사용성이 좋다.
2. 유지보수가 편리하다.
3. 가독성이 좋아진다.
'''

# 함수를 사용하지 않는 경우
print('안녕하세요, Lee님')
print('현재 사용 기간이 15일 남았습니다.')


# 함수를 사용한 경우
def printMessage(name, date):
    print(f'안녕하세요, {name}님')
    print(f'현재 사용 기간이 {date}일 남았습니다.')


printMessage('Lee', 15)
