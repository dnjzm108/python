# 리스트 []

#  지하철 칸별로 10명,20명,30명

subway1 = 10
subway2 = 20
subway3 = 30

subway=[10,20,30]

print(subway)

subway = ['유재석','조세호','박명수']
# 조세호는 몇번째 칸에 타고 있나?
print(subway.index('조세호'))

# 다음정거장에서 하하가 다음칸에 탐
subway.append('하하')
print(subway)

# 정형돈을 유재석 / 조세호 사이에 탐
subway.insert(1,'정형돈')  # 첫번째 인자 자리를 뒤로 미루고 넣음
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()
print(subway)

# 자리 위치로 삭제
del subway[0]
print(subway)

# 지정하여 삭제
subway.remove('박명수')  # 주의 찾는 값이 없을 경우 에러남
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append('유재석')
print(subway.count('유재석'))


# 정렬도 가능
num_list = [8,2,1,3,5]
num_list.sort()
print(num_list)

# 순서 뒤집기 기능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
num_list = [8,2,1,3,5]
list = ['조세호',20,True]

#리스트 확장
num_list.extend(list)
print(num_list)


# 사전
cabinet = {3: '유재석', 100: '조세호'}
print(cabinet[3])  # 주의 찾는 값이 없으면 에러가 남
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5,'사용 가능')) #찾는 값이 없을 경우 두번째 인자값 또는 None return

print( 3 in cabinet) # bool 값 return

# 새로운 손님
cabinet[50] = '박명수'  # 만약 이미 값이 있을 경우 값이 '박명수' 로 업데이트 된다.
print(cabinet)

#  간 손님
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 
print(cabinet.values())

# key.value 쌍으로 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)


# 튜플   - 리스트랑 다르게 내용 변경이나 추가가 안됨 . 하지만 속도가 빠름
menu = ('돈까스','치즈까스')
print(menu[0])
print(menu[1])

name = '김종국'
age = 20
hobby = '코딩'
print(name,age,hobby)

(name , age,hobby) = ('ant',25,'코딩')
print(name,age,hobby)


# 집합 (set)
# 중복 안됨 , 순서없음
my_set ={1,2,3,4,4,4}
print(my_set)

java  = {'유재석','김태호','양세형'}
python  = {'유재석','박명수','김종국'}

# 교집합(java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 pytho 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(java 할 수 있지만 python 할 줄 모르는 개발자 
print( java - python)
print( java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# java 를 까먹음 
java.remove('김태호')
print(java)


# 자료 구조의 변경
menu = {'커피','우유','쥬스'}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))


# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨,3명은 커피 쿠포을 받게 됩니다.
# 추첨 프로그램을 작성 하시오.
 
# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2: 댓글내용과 상관없이 무작위로 추첨 하되 중복 불가
# 조건 3: random 모듈의 suffle 과 sample 을 활용

# 출력 예제 ) 
# -- 당첨자 발표 --
# 치킨 당첨자 :1
# 커피 당첨자 :[2,3,4]
# -- 축하합니다.--

# 활용예제
from random import *
# list = [1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list,3))
# print(sample(list,1))

person = list(range(1,21))
shuffle(person)
winners = sample(person,4)
chicken = winners[0]
coffee = winners[1:]
print(f'-- 당첨자 발표 -- \n 치킨 당첨자 : {chicken} \n 커피 당첨자 : {coffee} \n -- 축하합니다.--')
