import cv2
import numpy as np

point_list = []
src_img = cv2.imread('../img/poker.jpg')
COLOR = (255, 0, 255)
THICKNESS = 3
drawing = False


def mouse_handler(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))

    if drawing:
        prev_point = None
        for point in point_list:
            cv2.circle(src_img, point, 15, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(src_img, prev_point, point,
                         COLOR, THICKNESS, cv2.LINE_AA)
                prev_point = point

        for point in point_list:
            cv2.circle(src_img, point, 10, COLOR, cv2.FILLED)
        if len(point_list) ==4:
            show_result()
        cv2.imshow('img',src_img)

    def show_result():
        width,height = 530,710
        src = np.float32(point_list)
        dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)
     
        matrix = cv2.getPerspectiveTransform(src,dst)
        result = cv2.warpPerspective(
            src_img,matrix,(width,height))
        cv2.imshow('result',result)

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse_handler)
cv2.imshow('img',src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()