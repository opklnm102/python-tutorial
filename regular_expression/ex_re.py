# -*- coding: utf-8 -*-

import re
url = '<a href="etc/python3/koala.jpg"> picture </a> <font size="10">'
print(re.search('href="(.*?)">', url).group(1))  #정규식

# 주요 정규식 기호
# . 임의의 한 문자가 존재
# ? 바로 앞의 문자가 존재하거나 존재하지 않음 (1 or 0)
# * 바로 앞의 문자가 존재하지 않거나 무한대로 존재 (0 or infinite)
# + 바로 앞의 문자가 한번 이상 존재
# ^ 바로 뒤의 문자로 문자열이 시작
# $ 바로 앞의 문자로 문자열이 끝남
# {숫자} 숫자만큼 반복
# {숫자,} 숫자 이상만큼 반복
# {숫자1, 숫자2} 숫자 1이상, 숫자 2이하 만큼 반복
# (문자열) 문자나 문자열을 묶음
# [문자1, 문자2...] 대괄호 안에 있는 문자들이 존재하는지 검색
# [^ ] ^ 바로뒤에 문자가 존재하지 않음
# [:alpha:] 알파벳만 검색
# [:alnum:] 알파벳, 숫자만 검색
# [:digit:] 숫자만 검색
# [:upper:] 대문자만 검색
# \\ \(역슬래쉬) 자체를 검색
# \d 모든 숫자를 검색. [0-9]와 동일
# \D 숫자를 제외한 모든 문자를 검색
# \s 공백 검색
# \S 공백이 아닌 문자 검색
# \w 숫자 또는 문자 검색 [a-zA-Z0-9]
# \W 숫자 또는 문자가 아닌것을 검색

# 찾을 pattern을 미리 지정. 편하고 빠르다.
r = re.compile("[ab]")  #찾고 싶은 pattern 지정. a or b를 찾는다.
print(r.search("pizza"))  #해당 글자가 포함된 부분을 찾음. 정규식에 해당하는 부분이 있을 경우 Match object츌력
print(r.match("pizza"))  #동일한 단어를 찾음. 정규식에 해당하는 부분이 없기 때문에 None 출력

print("")
r = re.compile("[pP]")
print(r.search("apple"))
print(r.match("apple"))
print(r.match("apPle"))
print(r.match("pP"))
print("")

# 미리 지정안하고 사용
print(re.search("[pP]", "apPle"))
print(re.match("[pP]", "pP"))
print("")

# . -> 임의의 한문자를 의미
r = re.compile("a.c")
print(r.search("abc"))
print(r.search("afc"))
print(r.search("ac"))
print("")

# ? -> 바로 앞의 문자가 존재하거나 존재하지 않음. ?뒤의 글자는 반드시 있어야할 경우 요긴하게 사용
r = re.compile("ck?w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("ckk"))
print(r.search("kkkw"))
print("")

# * -> 바로 앞의 문자가 존재하지 않거나 개수와 상관없이 존재
r = re.compile("ck*w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("ckk"))
print(r.search("kkkw"))
print("")

# + -> 바로 앞의 문자가 1번이상 존재
r = re.compile("ck+w")
print(r.search("ckw"))
print(r.search("ckkkkkkw"))
print(r.search("ckkkkkk"))
print(r.search("cw"))
print("")

# ^ -> 시작되는 문자를 지정
r = re.compile("^c")  # c로 시작되는 것을 찾는다.
print(r.search("ckw"))
print(r.search("sjs"))
print("")

# $ -> 끝나는 문자를 지정
r = re.compile("e$")
print(r.search("apple"))
print(r.search("banana"))
print("")

# [문자1, 문자2, ...] -> 대괄호 안에 있는 문자들이 존재하는지 검색
r = re.compile("[abcd]")  # a 나 b 나 c 나 d를 찾는다.
print(r.search("pizza"))
print(r.search("bread"))
print(r.search("mashroom"))
print("")

# [^문자1, 문자2...] -> ^뒤에 문자들을 제외한 모든 문자를 검색
print(re.search("[^ap]", "apple"))  # 1번쨰로 나오는 pattern을 찾는다.
print(re.search("[^ab]", "bread"))
print(re.search("[^ab]", "orange"))
print("")

# 찾고 싶은 패턴이 여러가지가 있을 경우 범위를 줄 수 있다.
print(re.search("[a-g]", "apple"))
print(re.search("[0-5]", "123678"))
print(re.search("[가-사]", "강원도에서"))
print("")

# Match object 활용
# span: 정규식 조건에 부합하는 문자열의 시작과 끝을 알수 있다.
# match: 정규식에 부합한 문자열을 보여준다.
result = re.search("\d+", "햄버거가 무려 700원이나 하다니!!!")
print(result.start())  # 시작 index
print(result.end())  # 끝 index
print(result.span())  # index 범위
print(result.group())  # 정규식으로 찾은 결과 출력
print("")

# 정규식에서 사용하는 다양한 함수들
# search() - 문자열 전체에서 정규식에 부합하는 문자열이 있는지 검색
print(re.search("\d+", "가나다라마바사아400 102이러러러러러러럴러"))
print("")

# match() - 문자열의 처음이 정규식과 부합하는지 검색
print(re.match("\d+", "가나다라마바사아400 102이러러러러러러럴러"))
print("")

# findall() - 정규식에 부합하는 모든 문자열을 리스트로 리턴
print(re.findall("\d+", "가나다라마바사아400 102이러러러러러러럴러"))
print("")

# split() - 주어진 문자열을 특정 패턴을 기준으로 분리
print(re.split("[:]+", "Apple Orange : Grape Cherry"))
print(re.split("[: ]+", "Apple Orange : Grape Cherry"))
print("")

# sub() - 주어진 패턴과 일치하는 문자를 변경
print(re.sub("-", "**", "751023-1901813"))

# example
url = "http://www.naver.com"
print(re.split("[/]", url))

r = re.compile("[^\w\s]+")  # \w(모든 숫자, 알파벳), \s(공백, 이스케이프문자)를 ^(제외한 문자)가 +(1번이상 존재)
print(r.search("my name is .....?"))

str = "빵 5개, 우유 5팩, 사과 2개 주세요"
print(re.findall("\d+", str))


