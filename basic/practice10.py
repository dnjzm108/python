# # 기본 모듈 가져오기
# import theater_module

# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 
# theater_module.price_soldier(3)  # 3명이서 군인 할인


# # 변수로 변경하기 
# import theater_module as mv

# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# # 모두 가져오기 
# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(3)

# # 원하는 것 만 가져오기
# from theater_module import price,price_morning,price_soldier
# price(3)
# price_morning(3)
# price_soldier(3)

# # 원하는 것을 변수에 담아서 가져오기
# from theater_module import price_soldier as price
# price(3)



# # 팩키지 
# import travel.thailand
# trip_to = travel.thailand.ThaileandPackage()
# trip_to.detail()

# from travel.thailand import ThaileandPackage
# trip_to = ThaileandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackge()
# trip_to.detail()



# # __all__ - __init__ 파일에 설정 하여 *  범위 정하기 

# from travel import *
# trip_to = vietnam.VietnamPackge()
# trip_to.detail()



# 모듈 직접 실행
# thailand 파일에서 if __name__ == '__main__' 으로 파일에서 직접 실행 확인 가능 


# # 팩키지 ,모듈 위치
# import inspect
# import random
# from travel import *
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# # pip install  - 팩키지 설치
# # pypi 검색하여 다양한 팩키지가 있음
# # pip install beautifulsoup4
# # pip install --upgrade beautifulsoup4
# # pip uninstall beautifulsoup4
 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# # 내장 함수 
# # input : 사용자 입력을 받는 함수 
# language = input('무슨 언어를 좋아하세요?')
# print(f'{language}은 아주 좋은 언어 입니다.')

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# print(dir())
# import random # 외장 함수
# print(dir())
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# # 구글에서  list of python builtins  라고 검색하면 다양한 내장 함수를 볼 수 있다.



# 외장 함수 
# 구글에서 list of python modules 검색 하면 다양한 외장 함수 볼수있다.

# # glob : 경로내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob('*.py'))

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리

# folder = 'sample_dir'

# if os.path.exists(folder):
#     print('이미 존재하는 폴더 입니다.')
#     os.rmdir(folder)
#     print(folder,'폴더를 삭제 하였습니다.')
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder,'폴더를 생성하였습니다.')

# print(os.listdir())

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# import datetime
# print('오늘 날짜는 ',datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()  # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print('우리가 만난지 100일은', today + td) #오늘 부터 100일 후 


# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제 )
# 이 프로그램은 나도코딩에 의해 만들어 졌습니다.
# 유튜브 : http://youtube.com