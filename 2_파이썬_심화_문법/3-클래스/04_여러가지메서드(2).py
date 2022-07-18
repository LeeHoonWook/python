class Math:

    # 정적 메서드 : 인스턴스를 만들 필요가 없는 메서드
    @staticmethod
    def add(x, y):
        return x + y

    # 매직 메서드 : 클래스 안에 정의할 수 있는 스페셜 메서드
    # : __이름__의 형태로 되어있다.


print(Math.add(3, 4))
