#마우스 클릭 이벤트로 

import cv2
import numpy as np

pts1 = []

img = cv2.imread("tilt.jpg")

dst = cv2.resize(img, (512, 512))

def mouse_callback(event, x, y ,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pts1.append([x, y])
        cv2.circle(dst, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("dst",dst)

        if len(pts1) == 4:
            perform_transdorm()

def perform_transdorm():
    src_pts = np.float32(pts1)

    dst_pts = np.float32([[0,0],[512,0],[0,512],[512,512]])

    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)

    result = cv2.warpPerspective(dst, matrix, (512,512))
    cv2.imshow("new_image",result)

cv2.imshow("original",dst)
cv2.setMouseCallback("original",mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()