import cv2
import numpy as np
import random

#그림을 그릴 판
canvas = None
#이전좌표
prev_point = None

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("연결 됨")
else:
    print("연결 안됨")

draw_color = (0, 0, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #좌우 반전
    frame = cv2.flip(frame, 1)

    #웹캠 크기와 똑같은 창 생성
    if canvas is None:
        canvas = np.zeros_like(frame)

    #BRG를 HSV로 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Hue(색상)-Saturation(채도)-Value(명도)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    #마스크 생성
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #물체의 윤곽선 찾기
    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    curr_point = None

    if len(cnts) > 0:
        #가장 큰 빨간색 물체 찾기
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        #어느 정도 크기가 있는 물체만 펜으로 인식 (노이즈 방지)
        if radius > 10:
            # 물체의 중심점 계산
            M = cv2.moments(c)
            if M["m00"] > 0:
                curr_point = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                #canvas에 선 그리기
                if prev_point is not None:
                    # 이전 점과 현재 점을 선으로 연결
                    cv2.line(canvas, prev_point, curr_point, draw_color, 5)
                
                # 현재 점을 이전 점으로 저장
                prev_point = curr_point
    else:
        prev_point = None

    result = cv2.add(frame, canvas)

    if draw_color == (0, 0, 255):
        color_text = "RED"
    elif draw_color == (0, 255, 0):
        color_text ="GREEN"
    else:
        color_text = f"RGB{draw_color}" # 현재 적용된 BGR 값 표시

    #화면에 텍스트 쓰기 
    cv2.putText(result, f"Current Color: {color_text}", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, draw_color, 2, cv2.LINE_AA)

    cv2.imshow("original",frame)
    cv2.imshow("result", result)
    cv2.imshow("canvas",canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('p'):
        b =random.randint(0, 255)
        r =random.randint(0, 255)
        g =random.randint(0, 255)
        draw_color = (b, g, r)
    

    
cv2.destroyAllWindows()