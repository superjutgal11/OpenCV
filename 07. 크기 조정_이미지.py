#!/usr/bin/env python
# coding: utf-8

# # 7. 크기 조정
# 
# 이미지나 동영상의 프레임 크기를 조정하는 것이다.  

# ## 이미지 크기 조정
# 
# 1. 고정 크기로 설정

# In[3]:


import cv2
img = cv2.imread('img.jpg')
dst = cv2.resize(img,(400,500))
# 사이즈 조정 함수 = cv2.resize(바꿀 대상 객체,(바꿀 사이즈 가로,세로))

cv2.imshow('img',img)
cv2.imshow('resize_img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
# --------------------------------------------------------------------------------------------
# 2. 비율을 유지하고 크기를 설정

# In[5]:


import cv2
img = cv2.imread('img.jpg')
dst = cv2.resize(img,None,fx=0.5,fy=0.5) # 비율을 유지한 태 0.5배로 축소
# 사이즈 조정 함수 = cv2.resize(바꿀 대상 객체,None,fx=크기,fy=크기)

cv2.imshow('img',img)
cv2.imshow('resize_img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
# 
# # 보간법
# 
# : 이미지를 줄이거나 키울 때, 보다 자연스러운 처리를 위한 방법으로 예를들어 100x100픽셀을 1000x1000로 확대할 때 비게 되는 픽셀들을 처리하는 등의 방법이다. 보간법 적용은 resize 함수 인수로 interpolation= 과 함께 넣어 준다.
# 
# 1. cv2.INTER_AREA    : 크기를 줄일 때 사용 
# 1. cv2.INTER_CUBIC   : 크기를 늘릴 때 사용 (속도는 느리나 퀄리티가 좋음)
# 1. cv2.INTER_LINEAR  : 크기를 늘릴 때 사용 (디폴트값)  

# In[9]:


# 보간법 적용하여 축소

import cv2
img = cv2.imread('img.jpg')
dst = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA) # 비율을 유지한 태 0.5배로 축소
# 사이즈 조정 함수 = cv2.resize(바꿀 대상 객체,None,fx=크기,fy=크기)

cv2.imshow('img',img)
cv2.imshow('resize_img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
# 
# 시각적으로 큰 차이는 없음.

# 보간법 적용하여 확대

# In[13]:


# 보간법 적용하여 확대 

import cv2
img = cv2.imread('img.jpg')
dst_1 = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC) # 속도는 느리나 퀄리티가 높음
dst_2 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR) # 디폴트값
# 사이즈 조정 함수 = cv2.resize(바꿀 대상 객체,None,fx=크기,fy=크기)

cv2.imshow('img',img)
cv2.imshow('resize_1',dst_1)
cv2.imshow('resize_2',dst_2) # 세개를 동시에 출력한다.

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
