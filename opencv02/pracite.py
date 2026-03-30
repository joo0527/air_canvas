# 녹색 배경을 가진 피사체 영상을 `lena.jpg` 배경 위에 자연스럽게 합성해 봅니다. (기상캐스터 원리)

# 1. **준비물:** 녹색 배경의 인물/물체 이미지 (또는 웹캠의 녹색 종이), 배경으로 쓸 `lena.jpg`.
# 2. **배경 제거:** 입력 영상에서 녹색 영역을 찾아내어 마스크를 만듭니다. 
# 3. **전경 추출:** 마스크를 반전시켜 피사체(사람)만 떼어냅니다. 
# 4. **배경 구멍 뚫기:** `lena.jpg`에서 피사체가 들어갈 위치를 검은색으로 비워둡니다. 
# 5. **합성:** 두 이미지를 합칩니다.

# import cv2
# import numpy as np
# chroma = cv2.imread("chroma.jpg")
# chroma = cv2.resize(chroma, (512,512))
# lena = cv2.imread("lena.jpg")

# #2. 배경 제거:녹색 영역 마스크 만들기 
# green_mask = cv2.inRange(chroma, (0, 150, 0), (150, 255, 150))

# #3.전경추출:사람만 떼어내기
# mask_inv = cv2.bitwise_not(green_mask)
# foreground = cv2.bitwise_and(chroma, chroma, mask=mask_inv)

# #4.배경 구멍 뚫기
# background_cut = cv2.bitwise_and(lena, lena, mask=green_mask)

# #5. 합성
# result = cv2.add(foreground, background_cut)

# #cv2.imshow("src",chroma)
# #cv2.imshow("green mask", green_mask)
# cv2.imshow("foreground",foreground)
# cv2.imshow("background", background_cut)
# cv2.imshow("result",result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
chroma = cv2.imread("chroma.jpg")
chroma = cv2.resize(chroma, (512,512))
lena = cv2.imread("lena.jpg")

#2. 배경 제거:녹색 영역 마스크 만들기 
green_mask = cv2.inRange(chroma, (0, 120, 0), (100, 255, 100))

#3.전경추출:사람만 떼어내기
mask_inv = cv2.bitwise_not(green_mask)
foreground = cv2.bitwise_and(chroma, chroma, mask=mask_inv)

#4.배경 구멍 뚫기
background_cut = cv2.bitwise_and(lena, lena, mask=green_mask)

#5. 합성
result = cv2.add(foreground, background_cut)

#cv2.imshow("src",chroma)
#cv2.imshow("green mask", green_mask)
cv2.imshow("foreground",foreground)
cv2.imshow("background", background_cut)
cv2.imshow("result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()