# map 함수
# : map(함수, 순서가 있는 자료형)

items = ['  pen', 'eraser  ']

items = list(map(lambda x: x.strip(), items))

print(items)

# filter 함수
# : filter(함수, 순서가 있는 자료형)

result = list(filter(lambda x: len(x) <= 3, items))

print(result)
