# # 조건문 if

# weather = input('오늘 날씨는 어때요?')  # 입력값을 받는 함수 터미널에 질문을 던지고 입력받은 값은 변수에 할당

# if weather == '비':
#     print('우산을 챙기세요')
# elif weather == '미세먼지':
#     print('마스크를 챙기세요')
# else:
#     print('준비물이 없어요')


# # 파이썬은 들여쓰기가 매우 중요하다. 칸의 위치로 조건문에 들어가는지 안들어 가는 지 결정됨

# temp = int(input('기온은 어때요?'))
# if 30 <= temp:
#     print('너무 더워요. 나가지 마세요')
# elif 10 <= temp <30:
#     print('괜찮은 날씨에요')
# elif 0<= temp <10:
#     print('외투를 챙기세요')
# else:
#     print('너무 추워요 나가지 마세요')


# 반복문 for
# print('대기번호:1')
# print('대기번호:2')
# print('대기번호:3')

# for waiting_no in list(range(5)):
#     print(f'대기번호 : {waiting_no}')

# starbucks = ['아이언맨','토르','헐크']

# for customer in starbucks:
#     print(f'{customer}, 커피가 준비 되었습니다.')


# # 반복문 while

# customer = '토르'
# index = 5

# while index >= 1:
#     print(f'{customer},커피가 준비 되었습니다. {index} 번 남았습니다.')
#     index -= 1
#     if index == 0:
#         print('커피는 폐기처분 되었습니다.')

# person = 'Unknwon'

# # while 문은 조건에 만족 할때 까지 반복
# while person != customer:
#     print(f'{customer}, 커피가 준비 되었습니다.')
#     person = input('이름이 어떻게 되세요?')


# continue 와 break  반복문에서 사용 가능
absent = [2, 5]  # 결석
no_book = [7]  # 책을 깜빡했음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f'오늘 수업 여기까지. {student}는 교무실로 따라와')
        break
    print(f'{student}, 책을 읽어봐')


# 한줄 for문 
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

students = ['Iron man','Thor','I am groot']

students = [i.upper() for i in students]
print(students)

students = [len(i) for i in students]
print(students)


# Quiz) 당신은 cocoa 서비스를 이용하는 택시기사님 입니다.
# 50명의 승객과 매칭 기회가 있을때 , 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O]1번째손님 (소요시간 : 15분)
# [ ]2번째손님 (소요시간 : 50분)
# [O]3번째손님 (소요시간 : 5분)
# ...
# [ ] 50번째손님 (소요시간:16분)
# 총 탑승 승객 : 2분

from random import *
customer = 0  # 총 탑승 승객
for count in list(range(1,51)):  # 1~50 (승객)
    time = randint(5,50) # 5분~50분 소요시간
    if 5 <= time <=15:  # 5~15분 사이 매칭 성공
        print(f'[O]{count}번째손님 (소요시간:{time}분)')
        customer +=1 # 탑승 승객 수 추가
    else:  # 매칭 실패
        print(f'[ ]{count}번째손님 (소요시간:{time}분)')
print(f'총 탑승 승객 : {customer} 분')