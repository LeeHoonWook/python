# Python

## 1. 파이썬이란?
> Python은 웹 애플리케이션, 소프트웨어 개발, 데이터 과학, 기계 학습(ML)에 널리 사용되는 프로그래밍 언어입니다.   
> 참고 : https://aws.amazon.com/ko/what-is/python/

## 2. Git 설명

> Python을 공부하면서 정리한 자료입니다.   
> 강의 : 한 번에 끝내는 파이썬 웹 개발 초격차 패키지(패스트캠퍼스)

## 3. 환경설정

> 해당 개발 환경은 window의 wsl2를 기반으로 작성되었습니다.   
> 참고 : https://velog.io/@gggggeun1/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD

```sh
# pip 안될 시
User $ sudo apt-get install python3-pip

# 가상환경 생성 및 실행
User $ sudo pip3 install virtualenv virtualenvwrapper
User $ virtualenv --python=python3 가상환경명
User $ source 환경명/bin/activate
(venv) User $ 필요한 모듈 설치

# 패키지 관리
(venv) User $ pip freeze > requirements.txt

# 내려받기 
(venv) User $ pip install -r requirements.txt
```