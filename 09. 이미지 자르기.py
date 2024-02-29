#!/usr/bin/env python
# coding: utf-8

# # 이미지 자르기
# 
# 앞으로 동영상이나 이미지나 적용법이 같기 때문에 동영상에 대한 내용의 작성은 하지 않는다.  

# In[2]:


# 첫 번째 방법 : 원하는 영역을 잘라서 새로운 윈도우 창에 표시하는 방법

import cv2
img = cv2. imread('img.jpg')
img.shape # 이미지 크기를 알아내는 방법. 출력치는 (427, 640, 3)
# 위 부분보다는 작은 크기를 잘라내야 한다.

crop = img[100:200,200:400]
# 자른객체변수 = 기존객체변수[가로범위 , 세로범위]

# 원본 이미지와 자른 이미지를 둘 다 다른 창으로 표시하도록 하겠다

cv2.imshow('image',img)
cv2.imshow('img_mod',crop)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)

# In[3]:


# 두 번째 방법 : 영역을 잘라서 기존 윈도우 창에 표시

import cv2
img = cv2. imread('img.jpg')

crop = img[100:200,200:400] # 잘라 낸 이미지 객체

img[100:200,400:600] = crop # 잘라 낸 이미지 객체를 img의 영역에 넣음

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
