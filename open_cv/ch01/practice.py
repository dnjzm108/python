# 환경 설정 
# pip install opencv-python

import cv2
# print(cv2.__version__)

# # 1. 이미지 출력

# img = cv2.imread('../img/img.jpg')  # 해당경로 파일 읽어오기
# cv2.imshow('img',img) # img 라는 이름의 창에 img 표시
# key = cv2.waitKey(0) # 지정된 시간동안 사용자 키 입력 대기  0은 무한정 대기
# print(key) # 아스키코드 
# cv2.destroyAllWindows() # 모든 창 닫기

# # 읽기 옵션 
# # 1. cv2.IMREAD_COLOR : 컬러 이미지 . 투명 영역은 무시 (기본값)
# # 2. cv2.IMREAD_GRAYSCALE : 흑백 이미지
# # 3. cv2.IMREAD_UNCHAGED : 투명 영역까지 포함

# img_color = cv2.imread('../img/img.jpg',cv2.IMREAD_COLOR)
# img_gray = cv2.imread('../img/img.jpg',cv2.IMREAD_GRAYSCALE)
# img_unchanged = cv2.imread('../img/img.jpg',cv2.IMREAD_UNCHANGED)

# cv2.imshow('img_color',img_color)
# cv2.imshow('img_gray',img_gray)
# cv2.imshow('img_unchage',img_unchanged)

# cv2.waitKey(0)
# cv2.destroyAllWindows() 

# # Shape
# # 이미지의 height , width , channel 정보

# img = cv2.imread('../img/img.jpg')
# print(img.shape)




# # 동영상 파일 출력 
# # google pexels 검색

# cap = cv2.VideoCapture('../movie/cat.mp4')

# while cap.isOpened():  # 동영상 파일이 올바로 열였는지?
#     ret,frame = cap.read() # ret: 성공여부 , frame : 받아온 이미지 (프레임) 
#     if not ret:
#         print('더 이상 가져올 프레임이 없어요')
#         break

#     cv2.imshow('video',frame)

#     if cv2.waitKey(1) == ord('q'):
#         print('사용자 입력에 의해 종료합니다.')
#         break

# cap.release() # 자원해제
# cv2.destroyAllWindows() # 모든 창 닫기


# # 카메라 출력 

# cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)
# if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
#     exit() # 프로그램 종료

# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow('camera',frame)
#     if cv2.waitKey(1) == ord('q'):  # 사용자가 q를 입력하면
#         break

# cap.release()
# cv2.destroyAllWindows()
