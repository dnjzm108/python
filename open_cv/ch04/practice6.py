#  이미지 변형 (원근)


import cv2
import numpy as np

# # 사다리꼴 이미지 펼치기
# img = cv2.imread('../img/news.jpg')

# width, height = 640, 240  # 가로 크기 640,세로크기 240 으로 결과물 출력

# src = np.array([[511, 352], [1008, 345], [1122, 534], [455, 594]], dtype=np.float32)  # input 4개 지점

# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)  # Output 4개 지점
# #  좌상, 우상,우하,좌하 (시계 방향으로 4개 지점 정의)
# matrix = cv2.getPerspectiveTransform(src, dst)  # Matric 얻어옴
# result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환을 함

# cv2.imshow('img', img)
# cv2.imshow('result',result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 회전된 이미지 세로 세우기

img = cv2.imread('../img/poker.jpg')

width, height = 530, 710  # 가로 크기 530,세로크기 710 으로 결과물 출력

src = np.array([[702,143], [1133,414], [726,1007], [276,700]], dtype=np.float32)  # input 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)  # Output 4개 지점
#  좌상, 우상,우하,좌하 (시계 방향으로 4개 지점 정의)
matrix = cv2.getPerspectiveTransform(src, dst)  # Matric 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환을 함

cv2.imshow('img', img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
