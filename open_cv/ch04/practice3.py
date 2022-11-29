# 이미지 대칭

import cv2

# # 좌우대칭
# img = cv2.imread('../img/img.jpg')
# flip_horizontal = cv2.flip(img,1) #flipCode > 0 좌우대칭 Horizontal

# cv2.imshow('img',img)
# cv2.imshow('flip_horizontal',flip_horizontal)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 상하 대칭

# img = cv2.imread('../img/img.jpg')
# flip_Vertical = cv2.flip(img,0) #flipCode == 0 :상하좌우 Vertical

# cv2.imshow('img',img)
# cv2.imshow('flip_Vertical',flip_Vertical)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 상하 좌우 대칭
img = cv2.imread('../img/img.jpg')
flip_both = cv2.flip(img,-1) # flioCode < 0 상하 좌우 대칭

cv2.imshow('img',img)
cv2.imshow('flip_both',flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()