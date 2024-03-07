#!/usr/bin/env python
# coding: utf-8

# # 이미지 변환 : 팽창과 침식 (노이즈 제거)
# 
# ### 이미지 팽창
# 
# : 이미지를 확장하여 밝은 부분을 채우는 것.

# In[2]:


import cv2
import numpy as np

kerner = np.ones((3,3),dtype=np.uint8) 
# 커널을 만들어 둔다. 커널은 주로 팽창이 이루어질 때 각 픽셀의 주변 영역을 어떻게 고려할지를 정의하는 데 사용됨.
# 3행 3렬의 1로 구성된 행렬을 만든다.

img = cv2.imread('picture_1.jpg',cv2.IMREAD_GRAYSCALE) # 그레이스케일로 받아온다
# 불러온 사진은 검정 화면에 흰 글씨가 있고 흰 글씨에 검정색 점이 박혀있는 이미지이다.

dilate1 = cv2.dilate(img,kerner,iterations=1)
# 넣을 이미지 객체,커널,반복 횟수
dilate2 = cv2.dilate(img,kerner,iterations=2) # 2번 반복
dilate3 = cv2.dilate(img,kerner,iterations=3) # 3번 반복

cv2.imshow('gray',img)
cv2.imshow('dilate1',dilate1)
cv2.imshow('dilate2',dilate2)
cv2.imshow('dilate3',dilate3)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 
# 눈에 크게 띄지 않지만 반복횟수가 많아질수록 흰색이 팽창하며 구멍이 메꿔짐을 확인할 수 있다. (글자도 커진다) 
# 이 기능을 이용하여 위처럼 검정 구멍을 메꾸는 등의 작업이 가능해진다.

# ### 이미지 침식
# 
# : 흰색 영역의 외각 픽셀을 검은색으로 변경. 즉 검정색이 번지는 거라고 보면 됨

# In[ ]:


import cv2
import numpy as np

kerner = np.ones((3,3),dtype=np.uint8) 
# 침식 또한 커널이 필요함.

img = cv2.imread('picture_2.jpg',cv2.IMREAD_GRAYSCALE) # 그레이스케일로 받아온다
# 불러온 사진은 검정 화면에 흰 글씨가 있고 검은 화면에 흰 점들이 박혀있는 이미지이다.

erode1 = cv2.erode(img,kerner,iterations=1)
# 넣을 이미지 객체,커널,반복 횟수
erode2 = cv2.erode(img,kerner,iterations=2) # 2번 반복
erode3 = cv2.erode(img,kerner,iterations=3) # 3번 반복

cv2.imshow('gray',img)
cv2.imshow('erode1',erode1)
cv2.imshow('erode2',erode2)
cv2.imshow('erode3',erode3)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 
# 흰 점들이 메꿔짐을 알 수 있다.
