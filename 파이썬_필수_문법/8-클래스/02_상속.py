# 상속의 개념
'''
 : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기
   위해서 사용
   
 부모클래스 <- 자식클래스
'''


# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f'[{self.name}] 지상에서 이동하기')


# 자식 클래스
class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f'[{self.name}] 헤엄치기')
