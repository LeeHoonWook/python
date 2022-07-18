txt = '   오늘 날씨는 흐림입니다.   '

# 1. 문자열 교체 : replace
txt.replace('흐림', '맑음')

print(txt)

# 2. 문자열 찾기 : find
f = txt.find('날씨')

print(f)

# 3. 문자열 분리 : split
# split('나누고 싶은 예') ex) :, , , 공백, /
s = txt.split()

print(s)

# 4. 문자열 공백 제거 : strip
ls = txt.lstrip()  # 왼쪽
rs = txt.rstrip()  # 오른쪽
st = txt.strip()  # 모두

print(f'{ls}, {rs}, {st}')
