# 파일 입출력을 사용하는 이유
# : 파일로부터 데이터를 읽고 사용하기 위해
# : 데이터를 파일 형태로 저장하기 위해

'''
 w : 쓰기 모드
 a : 추가 모드
 r : 읽기 모드
 
 file = open('파일 이름', '모드')
 file.write(데이터)
 file.close()
'''

file = open('data.txt', 'w', encoding="utf8")
file.write("1. 파이썬 공부")
file.close()

file = open('data.txt', 'a', encoding="utf8")
file.write("2. 파이썬 공부2")
file.close()

file = open('data.txt', 'r')
file.read()
file.close()
