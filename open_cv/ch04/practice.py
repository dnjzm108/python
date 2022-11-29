# # 파일 저장
# #  이미지 저장

import cv2

# img = cv2.imread('../img/img.jpg',cv2.IMREAD_GRAYSCALE) # 흑백으로 불러오기

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# result = cv2.imwrite('../img/img_gray.jpg',img)
# print(result)

# # 저장 포멧 (jpg,png)

# img = cv2.imread('../img/img.jpg',cv2.IMREAD_GRAYSCALE) # 흑백으로 불러오기
# cv2.imwrite('../img/img_gray.png',img)


# #  동영상 저장

# cap = cv2.VideoCapture('../movie/cat.mp4')

# # 코덱 정의
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# # 프레임 크기 ,FPS
# width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #정수만 가져와야함 혹시 실수를 대비해 round()쓴다
# height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS) # 수치를 높이면 영상 속도가 빨라짐


# out = cv2.VideoWriter('../movie/output.mp4',fourcc,fps,(width,height))
# #                       저장 파일명  , 코덱 , FPS , 크키(가로,세로)

# while cap.isOpened():
#     ret,frame = cap.read()

#     if not ret:
#         break
#     out.write(frame) # 영상 데이터만 저장 (소리 x )
#     cv2.imshow('video',frame)
#     if cv2.waitKey(1) == ord('q'):
#         break

# out.release() # 자원 해제
# cap.release()
# cv2.destroyAllWindows()

# # codec = 'DIVX'
# # print(codec)
# # print(*codec)
# # print([codec])
# # print([*codec])


# # 크기 조정
# # 이미지
# # 고정크기 설정

# img = cv2.imread('../img/img.jpg')
# dst = cv2.resize(img,(400,500))  # width , height 고정 크기

# cv2.imshow('img',img)
# cv2.imshow('resize',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread('../img/img.jpg')
# dst = cv2.resize(img, None, fx=2, fy=2)  # x , y 비율 정의 (2 배로 확대)

# cv2.imshow('img', img)
# cv2.imshow('resize', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 보간법

# # cv2.INTER_AREA : 크기 줄일 때 사용
# # cv2.INTER_CUBIC : 크기 늘릴 때 사용 (속도 느림,퀄리티 좋음)
# # cv2.INTER_LINEAR : 크기 늘릴 때 사용 (기본값)

# # 보간법 적용하여 축소

# img = cv2.imread('../img/img.jpg')
# dst = cv2.resize(img, None, fx=0.5, fy=0.5,
#                  interpolation=cv2.INTER_AREA)  # x , y 비율 정의 (0.5뱌 축소)

# cv2.imshow('img', img)
# cv2.imshow('resize', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('../img/img.jpg')
# dst = cv2.resize(img, None, fx=1.5, fy=1.5,
#                  interpolation=cv2.INTER_CUBIC)  # x , y 비율 정의 (1.5배 확대)

# cv2.imshow('img', img)
# cv2.imshow('resize', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # 동영상 크기 조정 
# # 고정 크기로 설정 
# cap = cv2.VideoCapture('../movie/cat.mp4')

# while cap.isOpened():
#     ret,frame = cap.read()
#     if not ret:
#         break

#     frame_resized = cv2.resize(frame,(400,500))

#     cv2.imshow('video',frame_resized)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# # 비율로 설정

# cap = cv2.VideoCapture('../movie/cat.mp4')

# while cap.isOpened():
#     ret,frame = cap.read()
#     if not ret:
#         break

#     frame_resized = cv2.resize(frame,None,fx=1.5,fy=1.5, interpolation=cv2.INTER_CUBIC)

#     cv2.imshow('video',frame_resized)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()