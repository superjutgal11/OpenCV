#!/usr/bin/env python
# coding: utf-8

# # 도형 그리기
# 
# 원, 삼각형, 다각형 등을 그리는 방법.  
# 이미지나 동영상에서 특정 위치를 표시할 때(얼굴인식,사물인식 등) 도형을 사용할 수 있음.
#   
#     
# 
# 
# 
# ## 빈 스케치북 그리기

# In[5]:


import cv2
import numpy as np     # 넘파이 사용

# 세로 480크기, 가로 640의 크기, 채널은 3channel (RGB)에 해당하는 스케치북 만들기.
img = np.zeros((480,640,3),dtype=np.uint8) # 0으로 가득 채운 공간을 만들라.

print(img)

# 이렇게 하면 공간이 생긴다. [[0,0,0],[0,0,0], ...] ... 


# 위에서 만약 0이 아닌 다른 값으로 채우고 싶다면 밑에 이 코드를 적는다.(ex, 255는 흑색)   
#   
# img[:] = (255,255,255)  
# 전체공간([:])을 255(흰색)으로 채우라는 의미의 코드가 된다.
# 
# 참고로 openCV에서는 RGB가 아니고 BGR로 표시됨. 

# In[ ]:


import cv2
import numpy as np     # 넘파이 사용

# 세로 480크기, 가로 640의 크기, 채널은 3channel (RGB)에 해당하는 스케치북 만들기.
img = np.zeros((480,640,3),dtype=np.uint8) # 0으로 가득 채운 공간을 만들라.
img[:] = (255,0,0) # BGR순서로 255,0,0 즉 파란색만 출력됨

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
# 파란색 창이 출력됨.


# ## 일부 영역 색칠

# In[2]:


import cv2
import numpy as np     

img = np.zeros((480,640,3),dtype=np.uint8) 
img[100:200,200:300] = (255,255,255) # 가로기준 100~200픽셀까지 그리고 가로기준 200~300픽셀까지 
                                     # 곂치는 부분을 흰색(255)로 채우기.
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


# ## 직선 그리기
# 
# 직선에는 종류가 몇가지 있다.  
# 1. cv2.LINE_4    상하좌우 4방향으로 연결된 선  
# 1. cv2.LINE_8    대각선을 포함한 8방향으로 연결된 선(디폴트값)  
# 1. cv2.LINE_AA   부드러운 선(안티 앨라이징)

# In[6]:


import cv2
import numpy as np   

img = np.zeros((480,640,3),dtype=np.uint8) 

COLOR = (0,255,255) # 노란색 생성
THICKNESS = 3 # 두께

cv2.line(img,(50,100),(400,50),COLOR,THICKNESS,cv2.LINE_8) # x가 50,y가 100인 시작점부터 (400,50)까지 선을 그려라
# 도형객체,시작점,끝점,색상,두께,선종류 순으로 값을 넣어 줌. line함수를 통해 해당 값의 라인을 그림. 

cv2.imshow('Line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

# 출력값은 다음과 같다.


# ![image.png](attachment:image.png)

# In[ ]:


import cv2
import numpy as np   

img = np.zeros((480,640,3),dtype=np.uint8) 

COLOR = (0,255,255) # 노란색 생성
THICKNESS = 3 # 두께

cv2.line(img,(50,100),(400,50),COLOR,THICKNESS,cv2.LINE_8) # 디폴트
cv2.line(img,(50,200),(400,50),COLOR,THICKNESS,cv2.LINE_4) # line-4
cv2.line(img,(50,300),(400,50),COLOR,THICKNESS,cv2.LINE_AA) # 안티 앨러이싱

cv2.imshow('Line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

# 출력값은 다음과 같다.


# ![image.png](attachment:image.png)

# 여기서 line_4 랑 라인_8 의 차이는 아래와 같다.  
# 
# ![image.png](attachment:image.png)  
# 
# Line-4 는 대각선의 연결이 반드시 서로 연결되어 있으나,  
# Line-8 는 대각선의 연결이 없어도 된다. 그림판을 생각 해 보자.
