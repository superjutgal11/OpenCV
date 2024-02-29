#!/usr/bin/env python
# coding: utf-8

# # 이미지 회전

# In[8]:


# 시계방향으로 90도 회전 = 반시계방향 270도 회전

import cv2
img = cv2.imread('img.jpg')

rotate = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# cv2.rotate(회전시킬 대상,시계방향으로 90도 회전 변수)

cv2.imshow('img_1',img)
cv2.imshow('img_2',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# In[10]:


# 180도 회전

import cv2
img = cv2.imread('img.jpg')

rotate_180 = cv2.rotate(img,cv2.ROTATE_180)
# cv2.rotate(회전시킬 대상,180도 회전 변수)
# 180도는 시계/반시계 의미가 없어서 댱 rotate_180 임

cv2.imshow('img_1',img)
cv2.imshow('img_2',rotate_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# In[11]:


# 시계방향 270도 회전 = 반시계방향 90도 회전

import cv2
img = cv2.imread('img.jpg')

rotate = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.rotate(회전시킬 대상,시계방향으로 90도 회전 변수)

cv2.imshow('img_1',img)
cv2.imshow('img_2',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
