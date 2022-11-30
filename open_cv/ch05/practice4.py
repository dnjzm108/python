# 미니 프로젝트 : 개별 카드 추출해서 파일 저장

import cv2

# img = cv2.imread('../img/card.png')
# target_img = img.copy()  # 사본 이미지

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# contours, hierachy = cv2.findContours(
#     otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 윤곽선 검출

# COLOR = (0, 200, 0)  # 녹색
# idx = 1
# for cnt in contours:
#     if cv2.contourArea(cnt) > 25000:
#         x, y, width, height = cv2.boundingRect(cnt)
#         cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2) 

#         crop = img[y:y+height, x:x+width]
#         cv2.imshow(f'card_crop_{idx}',crop)
#         cv2.imwrite(f'../img/card_crop_{idx}.png',crop)
#         idx += 1

# cv2.imshow('img', img)
# cv2.imshow('target_img', target_img)
# cv2.waitKey()
# cv2.destroyAllWindows()



# Quiz) OpenCV 를 이용하영 가로로 촬영된 영상을 세로로 회전하는 프로그램을 작성하시오

# 조건 1: 회전 시계 반대 방향으로 90도
# 조건 2 : 재생속도(FPS): 원본 X 4배
# 조건 3 : 출력 파일명 - city_output.avi (코덱:DIVX)

cap = cv2.VideoCapture('../movie/cat.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('cat_mission.mp4',fourcc,fps*4,(height,width))

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break

    rotate_frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대방향 90도
    out.write(rotate_frame)
    cv2.imshow('video',frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
