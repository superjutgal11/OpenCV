#!/usr/bin/env python
# coding: utf-8

# # 이미지 변형_흑백처리
# 
# 이미지 전처리 : 이미지 내에서 불필요하거나 부정확한 부분을 걸러 내는 과정.  
# 이미지 변형에서 흑백은 불러온 이미지를 흑백으로 만드는 과정임.

# In[1]:


import cv2
img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE) # 이미지를 불러올 때 흑백으로 받아오는 것.
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# 위 코드는 불러올 때부터 흑백으로 받아오는 것이다. 이 방법 말고 일반적으로 불러온 경우 그 이미지를 흑백처리하는 방법은 아래와 같다.

# In[6]:


import cv2
img = cv2.imread('img.jpg') # 이미지를 불러올 때 흑백으로 받아오는 것.

dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# OpenCV에서는 색상을 BRG로 받아옴. 그렇게 받아온 이미지를 GRAY색으로 바꾸는 함수임.

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# # 이미지 변형 _ 블러처리
# 
# 보이는 정보를 조정하여 외각선 검출을 단순하게 하기 위해 고의적으로 하는 경우가 있다.

# ## 가우시안 블러 
# : 이미지를 흐리게 또는 노이즈 제거가 가능하여 이미지 연산에 더 빠르고 정확한 계산이 가능.
# 1. 커널 사이즈 변화에 따른 블러 처리
# 1. 표준 편차의 변화에 따른 블러 처리

# In[11]:


# 1. 커널 사이즈 변화에 따른 블러 처리

# 커널(Kernel)은 이미지 처리에서 필터의 역할을 하는 행렬이며, 커널 크기는 이 행렬의 크기를 나타낸다. 
# 커널 크기는 여러 가지 작업에 사용되며, 대표적으로 이미지의 선명도 조절, 경계 검출 등에서 쓰인다.

import cv2
img = cv2.imread('img.jpg')

# 커널사이즈는 양수의 홀수로 지정하는것이 성능적 이유로 일반적으로 쓰이고 튜플형태를 가진다.
kn_3 = cv2.GaussianBlur(img,(3,3),0)
kn_5 = cv2.GaussianBlur(img,(5,5),0)
kn_7 = cv2.GaussianBlur(img,(7,7),0)
# cv2.GaussianBlur(처리할 이미지객체,(커널 크기 튜플),표준편차고 0이면 자동으로 결정됨)

cv2.imshow('img',img)
cv2.imshow('kn_3',kn_3)
cv2.imshow('kn_5',kn_5)
cv2.imshow('kn_7',kn_7)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
# 
# 커널 사이즈가 커질수록 블러 처리의 강도가 올라간다.

# In[13]:


# 2. 표준 편차의 변화에 따른 블러 처리

import cv2
img = cv2.imread('img.jpg')

# 표준편차의 변화에 따른 블러 처리 시에는 커널크기를(0,0)으로 두면 sigma_x에 의해 자동으로 커널크기가 결정됨
sigma_1 = cv2.GaussianBlur(img,(0,0),1) # sigma_x = 가우시안 커널의 x방향의 표준편차
sigma_2 = cv2.GaussianBlur(img,(0,0),2)
sigma_3 = cv2.GaussianBlur(img,(7,7),3)

cv2.imshow('img',img)
cv2.imshow('sigma_1',sigma_1)
cv2.imshow('sigma_2',sigma_2)
cv2.imshow('sigma_3',sigma_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
