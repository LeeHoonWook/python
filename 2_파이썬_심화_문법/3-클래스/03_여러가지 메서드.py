# Unit 클래스

class Unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    """
    count = 0

    # 생성자 : 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, shield, demage):
        self.name = name  # self는 객체 자기 자신을 의미
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f'{self.name}(이)가 생성되었습니다.')

    # 객체를 출력할 때 호출되는 메서드
    def __str__(self):
        return f'{self.name}의 체력은 {self.hp}, 방어막은 {self.shield}, 공격력은 {self.demage}입니다.'

    # 인스턴스 메서드 : 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self, demage):
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0

    # 클래스 메서드 : 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f'생성된 유닛 개수 : {cls.count}개')


# 객체를 생성
probe = Unit('프로브', 20, 20, 5)

zealot = Unit('질럿', 100, 60, 16)

dragoon = Unit('드라군', 100, 80, 20)


probe.hit(16)
print(probe)

Unit.print_count()
