#!/usr/bin/env python
# coding: utf-8

# # 사다리꼴 이미지 펼치기

# In[ ]:


# 우선 원근기법을 적용할 새로운 신문사진을 불러왔다.

import cv2
img = cv2.imread('newspaper.jpg')

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# In[2]:


# 원근 적용을 위해서는 input값이 필요함. 인풋값은 그림에서 받아내는 4개의 점을 의미하고 그 인풋을 아웃풋으로 바꿔내는 작업을 할 것임.
# 원근을 적용하기 위해 먼저 직사각형으로 바꿀 네 지점의 좌표를 찾아야 함. 맥북에서 미리보기로 픽셀좌표를 찍는다.


import cv2
import numpy as np # 넘파이를 참조한다.


img = cv2.imread('newspaper.jpg')


width,height = 640,240 # 가로크기 640, 세로크기 240 설정 변수. 출력창의 크기를 의미함.


src = np.array([[497,341],[1005,325],[1116,572],[441,560]],dtype=np.float32) # input 4개 지점 지정
# 4개의 점의 좌표를 list형으로 선언함.
# 순서는 시계방향으로 지정한다.  좌상>우상>우하>좌하


dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) # output 4개 지점 지정
# 위 src에서 받아 온 사진을 새로운 창에 넣는 변수이다.


matrix = cv2.getPerspectiveTransform(src,dst) # 사진 크기 변경 함수를 매트릭스 변수에 넣음.


result = cv2.warpPerspective(img,matrix,(width,height))
# img의 사진을 matrix변수 크기로 튜플크기의 크기를 갖는 변수의 형태로 변환을 한다. 최종 결과 이미지를 불러오는 함수.


cv2.imshow('img',img)
cv2.imshow('img_2',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)

# # 회전된 이미지 재회전

# In[6]:


import cv2
import numpy as np 


img = cv2.imread('poker_1.jpg') # 위 코드에서 복붙 후 이미지 설정을 했다.

# 이후 미리보기에서 포커_1 사진의 각 좌표를 가져왔다.

width,height = 530,710 # 사이즈를 카드크기에 맞게 설정함


src = np.array([[700,141],[1120,415],[720,995],[281,693]],dtype=np.float32) 
# 회전된 포커카드 이미지 픽셀 포인트들을 넣음


dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) 


matrix = cv2.getPerspectiveTransform(src,dst)


result = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow('img',img)
cv2.imshow('img_2',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ![image.png](attachment:image.png)
