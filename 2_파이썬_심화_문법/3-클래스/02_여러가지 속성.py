class Unit:

    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체마다 다른 값을 가지는 속성

    클래스 속성 : 전체 유닛 개수
    -> 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성 (__)
    """
    count = 0

    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.__hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f'{self.name}(이)가 생성되었습니다.')

    def __str__(self):
        return f'{self.name}의 체력은 {self.__hp}, 방어막은 {self.shield}, 공격력은 {self.demage}입니다.'


probe = Unit('프로브', 20, 20, 5)

zealot = Unit('질럿', 100, 60, 16)

dragoon = Unit('드라군', 100, 80, 20)
