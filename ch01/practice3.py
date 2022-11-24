# 문자열

str = '나는 소년 입니다'
print(str)
str2 = '파이썬은 쉬워요'
print(str2)
str3 = """ 나는 소년 입니다
파이썬은 쉬워요"""
print(str3)


# 슬라이싱

num = '950909-1234567'
# 컴퓨터는 자리수를 0 부터 시작한다.
print('성별 : ' + num[7])  # 문자열 7번째 자리를 가져오겠다
print('연도 : ' + num[0:2])  # 문자열 0번째 자리 이상 2미만
print('월 : ' + num[2:4])  # 문자열 0번째 자리 이상 2미만
print('일 : ' + num[4:6])  # 문자열 0번째 자리 이상 2미만

print('생년 월일 : ' + num[:6])  # 문자열 처음부터 6미만
print('뒤 7자리 : ' + num[7:])  # 문자열 7미만 부터 끝까지

print('마지막 자리 : ' + num[-1])  # 문자열 마지막 자리
print('뒤 7자리(뒤에서부터) : ' + num[-7:])  # 문자열 맨뒤에서 7번째 자리부터 끝까지
print('뒤집어서 출력 : ' + num[::-1])  # 문자열 거꾸로


# 문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())  # 문자열 소문자로 변환
print(python.upper())  # 문자열 대문자로 변환
print(python[0].isupper())  # 문자열 0번째가 대문자가 맞는지?

print(len(python))  # 문자열 길이 세주는 함수 17자
print(python.replace('Python', 'Java'))  # 첫번째 인자를 두번째 인자값을로 바꿔주는 함수

index = python.index("n")
print(index) # 인자의 위치를 알려주는 함수  5
index = python.index('n',index + 1) # 두번째 인자 다음부터 찾음
print(index) # 15 

#index 는 찾는 문자열이 없을 경우 에러가 남

test = python.find('Java')
print(test) # Java 문자열을 찾아줌  원하는 값이 없을 경우 -1

test2 = python.count('n')
print(test2) # 찾는 문자열이 총 몇번 나오는 지 세주는 함수