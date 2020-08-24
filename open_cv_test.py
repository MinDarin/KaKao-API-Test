import numpy as np
import cv2

# color 설정
color = (255, 255, 255)


# 모두 0으로 되어 있는 빈 Canvas(검정색)
img = np.zeros((700, 700, 4), np.uint8)
#img = cv2.line(img, (372,194), (372,194), blue_color, 5) #1
#img = cv2.line(img, (356,192), (356,192), blue_color, 5) #2
#img = cv2.line(img, (356,189), (356,189), blue_color, 5) #3
#img = cv2.line(img, (356,189), (356,189), blue_color, 5) #4
#img = cv2.line(img, (354,195), (354,195), blue_color, 5) #5

img = cv2.line(img, (358,148), (358,148), color, 5) #6
img = cv2.line(img, (354,145), (354,145), color, 5) #7
img = cv2.line(img, (391,241), (391,241), color, 5) #8
img = cv2.line(img, (366,221), (366,221), color, 5) #9
img = cv2.line(img, (385,323), (385,323), color, 5) #10
img = cv2.line(img, (368,289), (368,289), color, 5) #11
img = cv2.line(img, (226,80), (226,80), color, 5) #12
img = cv2.line(img, (224,80), (224,80), color, 5) #13
img = cv2.line(img, (115,169), (115,169), color, 5) #14
img = cv2.line(img, (133,169), (133,169), color, 5) #15
img = cv2.line(img, (150,315), (150,315), color, 5) #16
img = cv2.line(img, (166,284), (166,284), color, 5) #17

#왼쪽
img = cv2.line(img, (358,148), (391,241), color, 1) #6-8 어깨 - 팔꿈치 
img = cv2.line(img, (391,241), (385,323), color, 1)#8-10 팔꿈치  -손목
img = cv2.line(img, (358,148), (226,80),  color, 1)#6-12 어깨  - 엉덩이
img = cv2.line(img,  (226,80), (115,169), color, 1)#12-14 엉덩이 - 무릎
img = cv2.line(img, (115,169), (150,315), color, 1)#14-16 무릎 - 발목

#오른쪽
img = cv2.line(img, (354,145), (366,221), color, 1) #7-9 어깨 - 팔꿈치 
img = cv2.line(img, (366,221), (368,289), color, 1) #9-11 팔꿈치  -손목
img = cv2.line(img, (354,145), (224,80),  color, 1) #7-13 어깨  - 엉덩이
img = cv2.line(img,  (224,80), (133,169), color, 1) #13-15 엉덩이 - 무릎
img = cv2.line(img, (133,169), (166,284), color, 1) #15-17 무릎 - 발목

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
