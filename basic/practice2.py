# 내장 함수

from random import *
from math import *

print(abs(-5))  # 절대값 5
print(pow(4, 2))  # 4^2 = 4*4 = 16
print(max(4, 2))  # 최대값 4
print(min(4, 2))  # 최소값 2
print(round(3.15))  # 반올림 3


# 라이브러리 불러오기
# math
print(floor(4.99))  # 내림  4
print(ceil(4.99))  # 올림  5
print(sqrt(16))  # 제곱근  4.0


print(random())  # 0.0 ~ 1.0 미만의  임의의 값을 생성한다.
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 값


print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 수
print(randint(1, 45))  # 1 ~45 이하의 임의의 수


#  Quiz) 다신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성 하시오.

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

date = randint(4,28)
print(f'오프라인 스터디 모임 날짜는 매월 {date} 일로 선정되었습니다.')