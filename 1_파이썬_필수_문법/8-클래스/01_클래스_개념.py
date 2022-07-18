# 클래스를 사용하지 않는 경우
champion1_name = '이즈리얼'
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신 것을 환영합니다.")


def basic_attack(name, attack):
    print(f'{name} 기본공격 {attack}')


basic_attack(champion1_name, champion1_attack)


# 클래스를 사용하는 경우
class Champion:

    # 생성자 : 인스턴스를 만들 때 호출되는 메서드
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f'{name}님 소환사의 협곡에 오신 것을 환영합니다.')

    def basic_attack(self):
        print(f'{self.name} 기본공격 {self.attack}')


ezreal = Champion('이즈리얼', 700, 90)

ezreal.basic_attack()
