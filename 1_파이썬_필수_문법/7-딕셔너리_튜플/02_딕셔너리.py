# 딕셔너리의 특징
'''
1. 시퀀스 자료형
2. Key와 Value를 가지고 있는 사전형 자료형

딕셔너리 = {key:value, key2:value2}
'''

# 딕셔너리 만들기
stock = {'삼성전자': 82000, 'LG전자': 150000}

stocks = {'삼성전자': [81000, 82000, 83000, 84000]}

# 접근하기, 할당하기, 삭제하기
print(stock['삼성전자'])

stock['삼성전자'] = 83000

del stock['삼성전자']

# 딕셔너리 함수
print(stock.items())
print(stock.keys())
print(stock.values())

print('LG전자' in stock)
