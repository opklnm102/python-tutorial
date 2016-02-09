# -*- coding: utf-8 -*-
#한글을 코드 내 사용시 맨상단에 현재 코드의 인코딩방식을 표기 -> 대부분 utf-8사용
# -> 주석

#스크립트 언어
#라인 단위로 해석하여 수행

#장점
#개발 시간이 단축
#소스코드의 수정이 빠르고 간단하게 이루어진다.

#단점
#중간 코드를 만드는 것은 간단하지만 그것을 실제로 실행시키는 것은 많은 작업을 필요
#실행 시간이 오래걸린다.

#Python의 특징
#대화 기능의 인터프리터 언어
#동적인 데이터 타입 결정 지원
#플랫폼 독립적 언어
#개발 기간 단축에 촛점을 둔 언어
#간단하고 쉬운 문법
#고수준의 내장 객체 자료형 제공
#메모리 자동관리
#쉬운 유지보수
#많은 수의 라이브러리 제공
#짧아지는 코드
#높은 확장성

#활용처
#시스템 유틸리티, 게임, 웹 등

#장점
#들여쓰기를 강제화하여 코드의 가독성을 높였고, 코드의 재사용이 쉬움


print 4 + 5
print 12 -32
print (4 + 5) * 6
print 4 + 5 * 6
print 9 / 5  #정수/정수 연산결과는 정수
print 9.0 / 5.0
print 9 / 5.0

#화씨 변환기
#섭씨 온도: 32.2
#화씨 온도: 89.96
print "섭씨를 화씨로 변환"
celcius = float(raw_input("섭씨 입력>>"))
fah = ((9.0/5.0) * celcius) + 32
print "섭씨온도: ", celcius
print "화씨온도: ", fah

#웹에서 입력 받기
import urllib	#웹관련 라이브러리 호출
conn = urllib.urlopen('http://www.naver.com')	#홈페이지 호출
htmlcontents = conn.read()	#해당페이지 열기
print htmlcontents	#해당페이지 내용출력

#코딩 컨벤션

#Code layout
#들여쓰기는 공백 4칸을 권장
#한 줄은 최대 79자까지
#최상위(top-level)메소드와 클래스 정의는 2줄씩 띄어쓰기
#클래스 내의 메소드 정의는 1줄씩 띄어쓰기

#Whitespace in Expressions and Statements
#불필요한 공백은 피함 -> '[]', '()'안. ',', ':', ';' 앞
#=연산자는 붙여씀

#Comments
#주석은 항상 갱신, 불필요한 주석제거
#한줄 주석은 신중히 달기

#Naming Conventions
#변수명에서 '_'은 위치에 따라 의미가 있다.
#	_single_leading_underscore -> 내부적으로 사용되는 변수
#	single_trailing_underscore -> 파이썬 기본키워드와 충돌을 피하려고 사용
#	__double_leading_underscore -> 클래스 속성으로 사용되면 그 이름을 변경
#	(ex. FooBar에 정의된 __boo는 _FooBar__boo로 바뀐다.)
#	__double_leading_and_trailing_underscore__ -> magic을 부리는 용도로 사용되거나
#	사용자가 조정할 수 있는 네임스페이스 안의 속성을 뜻한다. 이름을 만들지 말고 문서대로 사용하세요
#소문자 L, 대문자 O, 대문자 I는 변수명으로 사용하지 말것(가독성 문제)
#Module명은 짧은 소문자로 구성되면 필요시 '_'사용
#	모듈은 파이썬 파일(.py)에 대응하기 때문에 파일 시스템의 영향을 받으니 주의
#	C/C++ 확장 모듈은 밑줄로 시작
#클래스명은 카멜케이스(CamelCase)로 작성
#	내부적으로 쓰이면 밑줄을 앞에 붙인다.
#	예외(Exception)는 실제로 에러인 경우엔 "Error"를 뒤에 붙인다.
#함수명은 소문자로 구성, 필요하면 '_'로 나눔
#인스턴스 메소드의 첫번쨰 인자는 언제나 self
#클래스 메소드의 첫번째 인자는 언제나 cls
#메소드명은 함수명과 같은나 비공개(non-public)메소드, 변수면 '_'을 앞에 붙인다.
#sub-class의 이름충돌을 막기 위해서는 '__'를 앞에 붙인다.
#상수(Constant)는 모듈 단위에서만 정의, 모두 대문자가 필요하면 '_'을 붙인다.

#Programming Recommendations
#코드는 될 수 있으면 어떤 구현(PyPy, Jython, IronPython등)에서도 불이익이 없게끔 작성
#None을 비교할 때는 is나 is not만 사용
#클래스 기반의 예외를 사용
#try: 블록의 코드는 필요한 것만 최소한으로 작성
#string모듈보다는 string메소드 사용. 메소드는 모듈보다 더 빠르고, 유니코드 문자열에 같은 API를 공유
#접두사나 접미사를 검사할 때는 startwith()와 endwith()를 사용
#객체의 타입을 비교할 때는 isinstance()를 사용
#빈 시퀀스(문자열, list, tuple)는 조거문에서 Flase다.
#boolean의 값을 조건문에서 ==을 통해 비교하지 마라.
#참고자료: https://spoqa.github.io/2012/08/03/about-python-coding-convention.html



















