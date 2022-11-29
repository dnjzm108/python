# 로또 번호 뽑기
from random import *

def random(num,min,max):

    for one in list(range(num)):
        total = list(range(min,max))
        shuffle(total)
        game = sample(total,6)
        game.sort()
        print(game)

if __name__ in '__main__':
    random(5,1,46)


# print(abs(-1))
# print(pow(2,4))
# print(max(4,5,7))
# print(min(2,1,2))
# print(round(4.12))

from math import *
from random import *

# print(floor(4.12))
# print(ceil(3.123))
# print(sqrt(304))

# print(random())
# print(randint(1,10))
# print(randrange(1,10))

# result = randint(4, 28)
# print(f'오프라인 스터디 모임 날짜는 매월 {result}일로 선정 되었습니다.')

# num = '950810-1027811'

# print(num[:6])

str = 'hey what are You doing'

# print(str.upper())
# print(str.lower())
# print(str.islower())

# print(len(str))
# print(str.replace('what','What'))


# arr = []

# for i in list(range(10)):
#     arr.append(randint(1,30))

# arr.sort()
# arr.pop()

# arr.reverse()

# arr2 =['a','b','c','d']
# arr.extend(arr2)
# print(arr)

