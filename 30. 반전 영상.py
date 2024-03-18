#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 기본 반전

import cv2

img = cv2.imread('img.jpg')

#subtract the img from max value

img_neg = 255 - img
dst1 = cv2.vconcat([img,img_neg])
cv2.imshow('negative tranfer 1',dst1)
cv2.waitKey(0)
cv2.waitKey(0)

# invert the image using cv2.bitwise_not

img_neg = cv2.bitwise_not(img)
dst2 = cv2.vconcat([img,img_neg])
cv2.imshow('negative tranfer 2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)

# In[10]:


# 임계값을 이용한 이진화

import numpy as np
import cv2

def thh(src,th,value_min=0,value_max=255):
    dst = np.zeros(src.shape, dtype=np.uint8)
    for r in range(src.shape[0]):
        for c in range(src.shape[1]):
            if src[r,c] >- th:
                dst[r,c] = value_max
            else:
                dst[r,c] = value_min
    return dst

src = cv2.imread('video.mp4',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

dst = thh(gray,100)

cv2.imread("result",dst)


# In[ ]:




