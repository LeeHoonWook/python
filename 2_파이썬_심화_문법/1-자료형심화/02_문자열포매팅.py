# 문자열 포매팅이 없다면?
# Lee님 마감까지 5일 남았습니다.

name = 'Lee'
duration = 5

message = name + '님 마감까지 ' + str(duration) + '일 남았습니다.'
print(message)

# f-string 사용
print(f'{name}님 마감까지 {duration}일 남았습니다.')

# format 메서드 사용
format_message = '{0}님 마감까지 {1}일 남았습니다.'.format(name, duration)
print(format_message)
