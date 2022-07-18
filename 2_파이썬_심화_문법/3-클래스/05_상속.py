from abc import *


class Item:
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f'{self.name}을 주웠습니다.')

    def discard(self):
        print(f'{self.name}을 버렸습니다.')


# ()안에 상속할 클래스를 쓴다.
class Weapon(Item):
    pass


# 추상클래스

class Items(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    # 상속받은 클래스에서 반드시 구현해야함
    @abstractmethod
    def use(self):
        pass
