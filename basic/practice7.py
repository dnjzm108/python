# #  표준 입출력

# print('Python' , 'Java',sep=' vs ',end="?")
# # end 마지막 문장 sep 는 , 마다 넣고 싶은 단어
# print('무엇이 더 재미있을까요?')
# import sys
# print('Python' , 'Java',file=sys.stdout) # 표준 출력
# print('Python' , 'Java',file=sys.stderr) # 표준 에러 

# # 시험 성적
# scores = {'수학':0,'영어':50,'코딩':100}
# for subject,score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":")
#     #             왼쪽 정렬 8칸 확보      오른쪽 정렬 4칸 확보


# # 은행 대기순서표
# # 001 002 003 ...
# for num in range(1,21):
#     print('대기번호 : ' + str(num).zfill(3))

# # input 의 값은 str로 들어온다 숫자를 적어도 스트링
# answer = input('아무 값이나 입력하세요 : ')
# print(f'입력 하신 값은 {answer} 입니다.')



# # 다양한 출력 포멧

# # 빈자리는 빈공간으로 두고 , 오른쪽 정렬을 하되, 총 10자리 공강을 확보
# print('{0: >10}'.format(500))

# # 양수 일때는 + 로 표시 , 음수 일때는 -로 표시
# print('{0: >+10}'.format(500))
# print('{0: >+10}'.format(-500))

# # 왼쪽 정렬하고 , 빈칸으로 _로 채움
# print('{0:_<+10}'.format(500))

# # 3자리 마다 콤마를 찍어주기
# print('{0:,}'.format(10000000000))

# # 3자리 마다 콤마 찍어주고 , + ,- 부호 붙이기
# print('{0:+,}'.format(10000000000))

# # 3자리마다 콤마,부호붙이고 ,자릿수 확보 빈자리는 ^ 채워주기
# print('{0:^<+30,}'.format(1000000000000000))

# # 소수점 출력
# print('{0:f}'.format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print('{0:.2f}'.format(5/3))


# # 파일 입출력
# #                             w 쓰기 기존에 데이터가 있으면 덮어쓰기가됨
# score_file = open('score.txt','w',encoding='utf8')
# print('수학 : 0',file=score_file) 
# print('영어 : 0',file=score_file) 
# score_file.close()

# #                             a 는 append 기존 데이터에 추가
# score_file = open('score.txt','a',encoding='utf8')
# score_file.write('과학:80')
# score_file.write('\n코딩:10')
# score_file.close()

# #                             r은 읽기
# score_file = open('score.txt','r',encoding='utf8')
# # print(score_file.read())  # 통째로 읽기

# print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동 
# print(score_file.readline(),end=" ")  # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동 
# print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동 

# score_file.close()

# 반복문으로 출력
# score_file = open('score.txt','r',encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end='')
# score_file.close()

# score_file = open('score.txt','r',encoding='utf8')
# lines = score_file.readlines()  # list 형태로 저장
# for line in lines:
#     print(line,end='')

# score_file.close()


# pickle   프로그램 상에 데이터를 파일 형태로 저장 다른사람에게 주면 pickle 통해 코드 사용 가능
# import pickle

# profile_file = open('profile.pickle','wb') # w 쓰기 목적 b 바이너리 
# profile = {'이름':'박명수','나이':30,'취미':['축구','골프','코딩']}
# print(profile)
# pickle.dump(profile,profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open('profile.pickle','rb')
# profile = pickle.load(profile_file)  # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()


# with

# import pickle
# with open('profile.pickle','rb') as profile_file: # 따로 닫지 않아도 된다.
#     print(pickle.load(profile_file))

# with open('study.txt','w',encoding='utf8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있어요')

# with open('study.txt','r',encoding='utf8') as study_file:
#     print(study_file.read())


# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 : 
# 업무요약 :
# 1주차 부터 50주착 까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt','2주차.txt', ... 와 같이 만듭니다. 

for day in list(range(1,11)):
    with open(f'{day}주차.txt','w',encoding='utf8') as bogo:
        bogo.write(f'- {day} 주차 주간보고 - \n부서 : \n이름 : \n업무요약 :')