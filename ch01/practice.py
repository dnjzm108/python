# 자료형
# int(숫자)
print(5)
print(-10)
print(3.14)

# 사칙연산
print(5+3)  # 더하기
print(5-3)  # 빼기
print(5*3)  # 곱하기
print(5/3)  # 나누기
print(5+(3*3))  # 우선 순위 먼저 계산


# string (문자열)
print('ㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ' * 7)


# bool (참 / 거짓)

print(5 < 10)  # True
print(5 > 10)  # False
print(True)  # 첫 알파벳을 대문자로 해주어야 한다
print(False)
print(not True)  # False   not은 반대를 말한다.
print(not (5 > 10))  # True


# 변수
동물 = '강아지'
이름 = '초코'
나이 = 10
결과 = 나이 >= 3

print(f'우리집 {동물}의 이름은 {이름}입니다.')
print(이름, '의 나이는', 나이, '살 입니다.')
print(이름 + '는 어른 일까요? ' + str(결과))  # 불리언을 문자열로 바꾸어 준다. 안바꾸면 애러가 남


# 주석
# 프로그램 실행시 무시하는 부분
# 시작을 # 으로 시작하면 주석 처리되며 contol + /  를 같이 눌러도 주석 처리됨

''' 여러문장을 주석 처리 하고 싶을 경우  ' 를 3개씩 쓰면 된다. '''


# Quiz ) 변수를 이용하여 다음 문장을 출력 하시오

# 변수명 : station
# 변수값 : '사당','신도림','인천공항' 순서대로 입력
# 출력 문장 : xx헹 열차가 들어오고 있습니다.

station = '사당'
print(f'{station} 행 열차가 들어오고 있습니다.')
station = '신도림'
print(f'{station} 행 열차가 들어오고 있습니다.')
station = '인천공항'
print(f'{station} 행 열차가 들어오고 있습니다.')


# 연산자
print(1+1)  # 더하기 2
print(3-2)  # 빼기 1
print(3*2)  # 곱하기 6
print(3/3)  # 나누기 1

print(3**2)  # 제곱  9
print(5 % 3)  # 나머지 구하기 2
print(10//3)  # 몫 구하기 3

print(10 > 3)  # 비교 연산자  True
print(4 >= 7)  # 크거나 같다 False
print(5 >= 5)  # True

print(3 == 3)  # 동등연산자 True
print(1 != 3)  # 같지 않다 True
print(not (1 != 3))  # False
# = 를 한번만 쓸 경우 변수 선언

print((3 > 0) and (3 < 5))  # 둘 조건 다 성립해야한다 True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5))  # 둘중 하나라도 성립하면 된다. True
print((3 > 0) | (3 > 5))  # True

print(3 < 5 < 7)  # True
print(3 < 5 > 7)  # False


# 우선 순위 연산
print(2 + 3 * 4)  # 14
print(2 * (3 + 4))  # 14

number = 2 + 3 + 4
print(number)  # 9

number = number + 3
print(number)  # 12

number += +3    # number = number + 3  과 number += 3 은 같다
print(number)  # 15

number *= 2
print(number)  # 30

number /= 2
print(number)  # 15
