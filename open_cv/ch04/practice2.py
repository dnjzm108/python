
# # 이미지 자르기 
# #  영역을 잘라서 새로운 윈도우(창)에 표시

import cv2 

# img = cv2.imread('../img/img.jpg')
# # img , shape (390,640,3)

# crop = img[100:200,200:400] # 세로 기준 100:200 까지 , 가로기준 200:400 까지 자름

# cv2.imshow('img',img)
# cv2.imshow('crop',crop)
# cv2.waitKey()
# cv2.destroyAllWindows()


# # 영역을 잘라서 기존 윈도우에 표시

# img = cv2.imread('../img/img.jpg')

# crop = img[100:200,200:400] # 세로 기준 100:200 까지 , 가로기준 200:400 까지 자름
# img[100:200,400:600] = crop

# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.destroyAllWindows()
