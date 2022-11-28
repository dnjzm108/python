# 문자열

string = '나는 소년 입니다'
print(string)
string2 = '파이썬은 쉬워요'
print(string2)
string3 = """ 나는 소년 입니다
파이썬은 쉬워요"""
print(string3)


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


# 문자열 포멧
print('a' + 'b')
print('a' , 'b')

# 방법 1
print('나는 %d살 입니다.' % 20) # d 는 정수
print('나는 %s을 좋아해요' % '파이썬') # s 는 문자열
print('애플은 %c로 시작해요' % 'A') # c 는 문자

print('나는 %s색과 %s색을 좋아해요' % ('파란','빨간'))

# 방법 2
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란','빨간'))

# 방법 3
print('나는 {age}살이며,{color}색을 좋아해요'.format(age=20,color='파란'))

# 방법 4 (v3.6 이상~)
age = 20
color = '파란'
print(f'나는 {age}살 이며 {color}색을 좋아해요.')


# 탈출 문자

print('백문이 불여일견 \n 백견이 불여일타')   # \n : 줄바꿈

print("저는 \"ant\" 입니다.")  # \"  \' :문장내에서 따움표

# \\ : 문장내에서 \
print('\\Users\\Desktop\\python\\ch01')

# \r : 커서를 맨 앞으로 이동
print('Red Apple \rPine') #PineApple 

# \b : 백스페이스 (한 글자 삭제)
print('Redd\bApple')  #RedApple

# \t : 탭
print('Red\tApple') # Red     Apple


# Quiz ) 사이트별로 비밀번호를 만들어 주는  프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.compile
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 (nav)          (5)           (1)       (!) 
# 예) 생성된 비밀번호 : nav51! 

que = 'http://naver.com'   

result1 = que[7:]  # que[-9:] , que.replace('http://','') ,
result2 = result1[:5] #result1.reoplace('.com','')  result1[:result1.index(".")]
result3 =  result2[:3] + str(len(result2)) + str(result2.count('e')) + '!'

print('{0} 의 비밀번호는 {1} 입니다.'.format(que,result3))