# 미니 프로젝트 : 반자동 문서 스캐너

# 마우스 이벤트 등록

import cv2
import numpy as np

# def mouse_handler(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN: #마우스 왼쪽 버튼 DOWN
#         print('왼쪽버튼 다운')
#         print(x,y)
#     elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼 Up
#         print('왼쪽버튼 업')
#         print(x,y)
#     elif event == cv2.EVENT_LBUTTONDBLCLK:  # 마우스 왼쪽 버튼 더블 클릭
#         print('왼쪽 버튼 Double Click')
#     # elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
#     #     print('마우스 이동')
#     elif event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 버튼 Down
#         print('오른쪽 버튼 Down')

# img = cv2.imread('../img/poker.jpg')
# cv2.namedWindow('img')  #  img 란 이름의 윈도우를 먼저 만들어 두는 것. 여기에 마우스 이벤트르르 처리 하기 위한 핸들러 적용
# cv2.setMouseCallback('img',mouse_handler)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 프로젝트

# point_list = []
# src_img = cv2.imread('../img/poker.jpg')
# COLOR = (255, 0, 255)  # 핑크


# def mouse_handler(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 DOWN
#        point_list.append((x, y))

#     for point in point_list:
#         cv2.circle(src_img, point, 10, COLOR, cv2.FILLED)

#     if len(point_list) == 4:
#         show_result()  # 결과 출력
#     cv2.imshow('img', src_img)


# def show_result():
#     width, height = 530, 710
#     src = np.float32(point_list)
#     dst = np.array([[0, 0], [width, 0], [width, height], [
#                    0, height]], dtype=np.float32)  # Output 4개 지점

#     matrix = cv2.getPerspectiveTransform(src, dst)  # Matric 얻어옴
#     result = cv2.warpPerspective(
#         src_img, matrix, (width, height))  # matrix대로 변환을 함
#     cv2.imshow('result', result)


# cv2.namedWindow('img')
# cv2.setMouseCallback('img', mouse_handler)
# cv2.imshow('img', src_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


point_list = []
src_img = cv2.imread('../img/poker.jpg')
COLOR = (255, 0, 255)  # 핑크
THICKNESS = 3
drawing = False  # 선을 그릴지 여부


def mouse_handler(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 DOWN
       drawing = True  # 선을 그리기 시작
       point_list.append((x, y))

    if drawing:
        prev_point = None  # 직선의 시작점
        for point in point_list:
            cv2.circle(src_img, point, 15, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(src_img, prev_point, point,
                         COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
            
    for point in point_list:
        cv2.circle(src_img, point, 10, COLOR, cv2.FILLED)

    if len(point_list) == 4:
        show_result()  # 결과 출력
    cv2.imshow('img', src_img)


def show_result():
    width, height = 530, 710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [
                   0, height]], dtype=np.float32)  # Output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)  # Matric 얻어옴
    result = cv2.warpPerspective(
        src_img, matrix, (width, height))  # matrix대로 변환을 함
    cv2.imshow('result', result)


cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
