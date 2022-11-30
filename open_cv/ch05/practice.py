# 이미지 변형 (이진화)
# 특정값을 기준으로 흰색과 검은색으로 나누는 것
# 흰색과 검은색을 가지는 바이너리 이미지로 바꾸는 것

import cv2

# # Threshold
# img = cv2.imread('../img/book.jpg', cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('img', img)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # Trackbar (값 변화에 따른 변형 확인)

# def empty(pos):
#     print(pos)
#     pass


# img = cv2.imread('../img/book.jpg', cv2.IMREAD_GRAYSCALE)

# name = 'Trackbar'
# cv2.namedWindow(name)

# cv2.createTrackbar('threshold', name, 127, 255, empty)
# #  bar 이름 , 창의 이름,초기값,최대값,이벤트 처리

# while True:
#     thresh = cv2.getTrackbarPos('threshold', name)  # bar 이름 ,창의 이름
#     ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

#     if not ret:
#         break

#     cv2.imshow(name, binary)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cv2.destroyAllWindows()


# Adaptive Threshold
# 이미지를 작은 영역으로 나누어 임계치 적용


# def empty(pos):
#     print(pos)
#     pass


# img = cv2.imread('../img/book.jpg', cv2.IMREAD_GRAYSCALE)

# name = 'Trackbar'
# cv2.namedWindow(name)

# cv2.createTrackbar('block_size', name, 25, 255, empty)  # 홀수만 가능 1 보다는 큰 값
# cv2.createTrackbar('c', name, 25, 255, empty)  # 일반적으로 양수의 값을 사용

# while True:
#     block_size = cv2.getTrackbarPos('block_size', name)  # bar 이름 ,창의 이름
#     c = cv2.getTrackbarPos('c', name)

#     if block_size <= 1:  # 이하면 3으로
#         block_size = 3

#     if block_size % 2 == 0:  # 짝수이면 홀수로
#         block_size += 1
#     binary = cv2.adaptiveThreshold(
#         img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, c)

#     cv2.imshow(name, binary)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cv2.destroyAllWindows()



# # 오츠 알고리즘 
# # Bimodal image 에 사용하기 적합(최적의 임계치를 자동으로 발견)
# img = cv2.imread('../img/book.jpg', cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('otsu threshold',ret)

# cv2.imshow('img', img)
# cv2.imshow('binary', binary)
# cv2.imshow('otsu', otsu)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

