# 클래스 변수
# : 인스턴스들이 모두 공유하는 변수

# 부모 클래스
import random


class Monster:
    max_num = 10000

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


class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ('불뿜기', '날개치기')

    def move(self):  # 메서드 오버라이딩
        print(f'[{self.name}] 날기')

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0, 2)]}")


dragon = Dragon('드래곤', 1500, 200)
dragon.move()
dragon.skill()
