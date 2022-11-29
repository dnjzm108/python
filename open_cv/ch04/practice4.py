# 이미지 회전

import cv2

# # 시계 방향 90도 회전

# img = cv2.imread('../img/img.jpg')

# rotate_90 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)  # 시게 방향으로 90 회전

# cv2.imshow('img',img)
# cv2.imshow('rotate_90',rotate_90)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 시계방향 180 도 회전

# img = cv2.imread('../img/img.jpg')

# rotate_180 = cv2.rotate(img,cv2.ROTATE_180)  # 시게 방향으로 180 회전

# cv2.imshow('img',img)
# cv2.imshow('rotate_180',rotate_180)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 시계 반대 방향 90도 회전

img = cv2.imread('../img/img.jpg')

rotate_270 = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)  # 시게 반대 방향으로 90 회전

cv2.imshow('img',img)
cv2.imshow('rotate_270',rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()