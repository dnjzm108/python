# # 이미지 변환 (팽창)

import cv2
import numpy as np

# kernel = np.ones((3,3),dtype=np.uint8)
# # kernel

# img = cv2.imread('../img/test.jpg',cv2.IMREAD_GRAYSCALE)
# dilate1 =cv2.dilate(img,kernel,iterations=1) #반복 횟수
# dilate2 =cv2.dilate(img,kernel,iterations=2) #반복 횟수
# dilate3 =cv2.dilate(img,kernel,iterations=3) #반복 횟수


# cv2.imshow('img',img)
# cv2.imshow('dilate1',dilate1)
# cv2.imshow('dilate2',dilate2)
# cv2.imshow('dilate3',dilate3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 이미지 변환 (침식) Erosion
# 이미지를 깍아서 노이즈 제거
# 흰색 영역의 외곽 픽셀을 검은색으로 변경

# kernel = np.ones((3,3),dtype = np.uint8)

# img = cv2.imread('../img/test2.jpg',cv2.IMREAD_GRAYSCALE)

# erode1 = cv2.erode(img,kernel,iterations=1)
# erode2 = cv2.erode(img,kernel,iterations=2)
# erode3 = cv2.erode(img,kernel,iterations=3)

# cv2.imshow('img',img)
# cv2.imshow('erode1',erode1)
# cv2.imshow('erode2',erode2)
# cv2.imshow('erode3',erode3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 이미지 변환 (열림 & 닫힘)
# 열림 (Opening) : 침식 후 팽창. 깍아서 노이즈 제거 후 살찌움
# dilate(erode(image))

# kernel = np.ones((3, 3), dtype=np.uint8)

# img = cv2.imread('../img/test2.jpg', cv2.IMREAD_GRAYSCALE)

# erode = cv2.erode(img, kernel, iterations=3)
# dilate = cv2.dilate(erode, kernel, iterations=3)

# cv2.imshow('img', img)
# cv2.imshow('erode', erode)
# cv2.imshow('dilate', dilate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 닫힘 (Cloding) : 팽창 후 침식. 구멍을 메운 후 다시 깍음
# erode(dilate(image))

kernel = np.ones((3, 3), dtype=np.uint8)

img = cv2.imread('../img/test.jpg', cv2.IMREAD_GRAYSCALE)

dilate = cv2.dilate(img, kernel, iterations=3)
erode = cv2.erode(dilate, kernel, iterations=3)

cv2.imshow('img', img)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()