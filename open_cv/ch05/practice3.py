# 이미지 검출 - 경계선

#  cannyEdge Detection

import cv2

# img = cv2.imread('../img/snowman.png')

# def empty(pos):
#     pass
# name = 'Trackbar'
# cv2.namedWindow(name)
# cv2.createTrackbar('threshold1',name,0,255,empty) #minVal
# cv2.createTrackbar('threshold2',name,0,255,empty) #maxVal

# while True:
#     threshold1 = cv2.getTrackbarPos('threshold1',name)
#     threshold2 = cv2.getTrackbarPos('threshold2',name)

#     canny = cv2.Canny(img,150,200)
# # 대상 이미지 . minVal(하위 임계값) maxVal(최대 임계값)

#     cv2.imshow('img',img)
#     cv2.imshow(name,canny)
#     if cv2.waitKey(0) == ord('q'):
#         break
# cv2.destroyAllWindows()


# # 이미지 검충 - 윤곽선


# img = cv2.imread('../img/card.png')
# target_img = img.copy()  # 사본 이미지

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# contours, hierachy = cv2.findContours(
#     otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출
# # 윤곽선 정보,구조
# # 이미지,윤곽선 찾는 모드(mode),윤괃선 찾을 때 사용하는 근사치 방법(merhod) : CHAIN_APPROX_NONE , CHAIN_APPROX_SIMPLE

# COLOR = (0, 200, 0)  # 녹색
# cv2.drawContours(target_img, contours, -1, COLOR, 2)  # 윤곽선 그리기
# # 대상 이미지 ,윤곽선 정보 , 인덱스(-1 이면 전체) ,색깔,두께


# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('otsu', otsu)
# cv2.imshow('target_img', target_img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# # 윤곽선 찾기 모드
# # cv2.RETR_EXTERNAL : 가장 외각의 윤관선만 찾음
# # cv2.RERT_LISR : 모든 윤관선 찾음 (계층 정보 없음)
# # cv2.RERT_TREE : 모든 유관선 찾음 (계층 정보를 트이 구조로 생성)

# img = cv2.imread('../img/card.png')
# target_img = img.copy()  # 사본 이미지

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# # contours, hierachy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출
# # contours, hierachy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출
# contours, hierachy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출
# print(hierachy)
# print(len(contours))

# COLOR = (0, 200, 0)  # 녹색
# cv2.drawContours(target_img, contours, -1, COLOR, 2)  # 윤곽선 그리기

# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('otsu', otsu)
# cv2.imshow('target_img', target_img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# # 경계 사각형
# # 윤곽선의 경계면을 둘러싸는 사각형
# # boundingRect()

# img = cv2.imread('../img/card.png')
# target_img = img.copy()  # 사본 이미지

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# contours, hierachy = cv2.findContours(
#     otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출

# COLOR = (0, 200, 0)  # 녹색
# for cnt in contours:
#     x, y, width, height = cv2.boundingRect(cnt)
#     cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2)  # 사각형 그림


# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('otsu', otsu)
# cv2.imshow('target_img', target_img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 면적
# contourArea()


img = cv2.imread('../img/card.png')
target_img = img.copy()  # 사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierachy = cv2.findContours(
    otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출

COLOR = (0, 200, 0)  # 녹색
for cnt in contours:
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2) 


cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('target_img', target_img)
cv2.waitKey()
cv2.destroyAllWindows()

