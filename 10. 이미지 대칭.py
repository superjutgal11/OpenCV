#!/usr/bin/env python
# coding: utf-8

# # 이미지 대칭

# In[5]:


# 좌우대칭 (수평대칭)

import cv2
img = cv2.imread('img.jpg')

flip = cv2.flip(img,1)
# 대칭함수 > cv2.flip(대칭시킬 사진객체,클립 코드)
# 플립코드가 0보다 크면 좌우대칭

cv2.imshow('img_1',img)
cv2.imshow('img_2',flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# In[8]:


# 상하대칭 (수직대칭)

import cv2
img = cv2.imread('img.jpg')

버티컬 = cv2.flip(img,0)
# 대칭함수 > cv2.flip(대칭시킬 사진객체,클립 코드)
# 플립코드가 0이면 상하대칭

cv2.imshow('img_1',img)
cv2.imshow('img_2',버티컬)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# In[10]:


# 상하좌우대칭 

import cv2
img = cv2.imread('img.jpg')

flip = cv2.flip(img,-1)
# 플립코드가 0보다 작으면 상하좌우대칭

cv2.imshow('img_1',img)
cv2.imshow('img_2',flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
