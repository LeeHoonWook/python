# 1. 위치 매개변수
# 가장 기본적인 매개변수

def my_func(a, b):
    print(a, b)


my_func(2, 3)


# 2. 기본 매개변수
# 매개변수의 기본값을 지정할 수 있다.

def post_info(title, content='내용없음'):
    print(f'제목은 {title}, 내용은 {content}')


post_info('안녕')

# 3. 키워드 매개변수
# 함수 호출 시 키워드를 붙여서 호출
# 순서를 지키지 않아도 된다.

post_info(content="슬퍼요", title="안녕")


# 1. 위치 가변 매개변수

def print_fruits(*args):
    print(args)


print_fruits('apple', 'orange', 'mango')


# 2. 키워드 가변 매개변수

def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


comment_info(main='안녕', sub='하세요')
