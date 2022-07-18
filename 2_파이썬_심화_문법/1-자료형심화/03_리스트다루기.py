# 리스트 메서드
fruits = ['apple', 'orange', 'mango']

# 삭제
fruits.pop()

fruits.pop(0)

fruits.remove('orange')

fruits.clear()  # 모두 삭제

# 추가(리스트도 추가 가능)
fruits.append('grape')
fruits.append('apple')
fruits.append('orange')


fruits.index('orange')  # 인덱스

fruits.count('orange')  # 값 개수

fruits.sort()  # 정렬

# 인덱스와 같이 출력

for i, fruit in enumerate(fruits):
    print(i, fruit)
