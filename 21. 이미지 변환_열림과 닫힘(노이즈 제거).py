#!/usr/bin/env python
# coding: utf-8

# # 이미지 변환 ( 열림 & 닫힘 ) : 노이즈 제거 기법
# 
# ## 열림 ( Opening )
# : 침식을 먼저 하고 팽창하는 것. dilate(erode(image)) 로 구현됨.

# In[7]:


import cv2
import numpy as np

img = cv2.imread('picture_2.jpg',cv2.IMREAD_GRAYSCALE)

# 커널 정의. 커널정의 시 넘파이에 임포트해야 함.(2번째 줄)
kernel = np.ones((3,3),dtype=np.uint8)

# 침식을 먼저 한다
erode = cv2.erode(img,kernel,iterations=10)

# 다음은 팽창. img가 아닌 erode가 들어감을 확인하자.
dilate = cv2.dilate(erode,kernel,iterations=10)

cv2.imshow('img',img)
cv2.imshow('erode',erode)
cv2.imshow('dilate',dilate)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 
# 원래 이미지엣 침식으로 흰 점들이 사라지고 글자가 얇아진 후 팽창하여 얇아진 글자가 다시 커짐.   
# 결론적으로 원본 이미지로부터 불필요한 노이즈를 제거한 결과를 얻어낼 수 있다.

# ## 닫힘 ( Closing )
# 
# : 팽창 후 침식하여 노이즈를 제거. erode(dilate(image)) 로 구현됨.

# In[8]:


import cv2
import numpy as np

img = cv2.imread('picture_1.jpg',cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3),dtype=np.uint8)


dilate = cv2.dilate(img,kernel,iterations=10)

erode = cv2.erode(dilate,kernel,iterations=10)



cv2.imshow('img',img)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 
# 글자에 있던 검정 구멍들을 메우고 글자를 팽창시키고 다시 글자를 침식시켜 노이즈를 제거한 사진을 얻어냈다.
