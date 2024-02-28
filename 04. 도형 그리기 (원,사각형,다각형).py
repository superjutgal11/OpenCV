#!/usr/bin/env python
# coding: utf-8

# ## 원 그리기
# 
# 
# 1. 속이 비어있는 원 그리기

# In[7]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) # 자주 헷갈리는데 unit이 아니고 uint임

COLOR = (255,255,0) # 옥색에 가깝게
RADIUS = 50 # 원은 반지름도 설정해야 함
THICKNESS = 10

cv2.circle(img,(200,100),RADIUS,COLOR,THICKNESS,cv2.LINE_AA)
# cv2.circle(그릴 스케치북, 원 중심점 좌표, 반지름, 색깔, 두께 , 선의 타입 )를 통해 속이 빈 원을 만들 수 있다.

cv2.imshow('circle image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ![image.png](attachment:image.png)
# 
# 2. 속이 차 있는 원 그리기

# In[10]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) # 자주 헷갈리는데 unit이 아니고 uint임

COLOR = (255,255,0) # 옥색에 가깝게
RADIUS = 50 # 원은 반지름도 설정해야 함

cv2.circle(img,(400,100),RADIUS,COLOR,cv2.FILLED,cv2.LINE_AA)
# cv2.circle(그릴 스케치북, 원 중심점 좌표, 반지름, 색깔, cv2.FILLED , 선의 타입 )를 통해 속이 빈 원을 만들 수 있다.

cv2.imshow('circle image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 속이 비어있는 원과 차이는 선의 두께가 없고 그 자리에 cv2.FILLED 가 들어간다는 점이다.


# ![image.png](attachment:image.png)

# ## 사각형 그리기
# 
# 1. 속이 빈 사각형 그리기

# In[18]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) # 자주 헷갈리는데 unit이 아니고 uint임

COLOR = (0,255,0) # 초록색
THICKNESS = 3 # 두께

cv2.rectangle(img,(100,100),(200,200),COLOR,THICKNESS)
# 사각형 그리기 함수 = cv2.rectangle(스케치북,상단좌측좌표,하단좌측좌표,색깔,두께)

cv2.imshow('rectangle image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ![image.png](attachment:image.png)
# 
# 2. 속이 찬 사각형 그리기

# In[20]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) # 자주 헷갈리는데 unit이 아니고 uint임

COLOR = (0,255,0) # 초록색

cv2.rectangle(img,(200,100),(300,300),COLOR,cv2.FILLED)
# 안이 찬 사각형 그리기 함수 = cv2.rectangle(스케치북,상단좌측좌표,하단좌측좌표,색깔,cv2.FILLED)

cv2.imshow('rectangle image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ![image.png](attachment:image.png)

# ## 속이 빈 다각형 그리기

# In[1]:


# 다각형의 경우애는 직접 본인이 좌표를 입력해야 한다.

import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) 

COLOR = (0,0,255) # 빨간색
THICKNESS = 3 

pts1 = np.array([[100,100],[200,100],[100,200]])
# 포인트변수 pts1에 넘파이 어레이를 입력함. 총 3개의 지점 [] 을 리스트로 [] 감싼 것. 
# 여기서는 3개이기 때문에 3각형을 의미하고 지점 [] 에 좌표를 넣는다.

cv2.polylines(img,[pts1],False,COLOR,THICKNESS,cv2.LINE_AA)
# 다각형 그리는 변수 => cv2.polylines(스케치북,[그릴 위치],Bool,색깔,두께,라인타입)
# 포인트 변수는 리스트로 [ ] 감싸야 한다.
# Bool을 True로 하면 첫 점과 끝 점이 연결되고, False로 하면 연결되지 않는다.

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Bool이 True인 경우  
# ![image.png](attachment:image.png)
# 
# Bool이 False인 경우  
# ![image-2.png](attachment:image-2.png)

# In[11]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) 

COLOR = (0,0,255) # 빨간색
THICKNESS = 3 

# 이렇게 두개의 다각형의 꼭짓점을 표현하고
pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[200,100],[300,100],[300,200]])

# # 아래 두 줄처럼 해도 문제는 없지만
# cv2.polylines(img,[pts1],True,COLOR,THICKNESS,cv2.LINE_AA)
# cv2.polylines(img,[pts2],True,COLOR,THICKNESS,cv2.LINE_AA)

# 이렇게 하면 한줄로 표현이 가능하다. 시퀀스 객체이므로 , 로 리스트화 후 합치는게 가능하니까!
cv2.polylines(img,[pts1,pts2],False,COLOR,THICKNESS,cv2.LINE_AA)
# 여기서 주의점이 pts1의 끝점과 pts2의 시작점이 일자로 이어지는 게 아니므로 bool을 false로 하면
# 위 두줄로 표현한 것에서 둘 다 false인 것과 같은 출력값이 나옴을 확인할 수 있다.

# 또 위 방법처럼 인수로 넣을 때 리스트로 넣을 수도 있고 새로운 변수를 리스트형으로 지정해 그 변수를 써서 넣을 수도 있다. 아래 코드에 있음.

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ## 속이 찬 다각형 그리기

# In[16]:


import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8) 

COLOR = (0,0,255)

pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[200,100],[300,100],[300,200]]) # 여기는 대괄호가 2개 아래 pts3은 3개임을 보자.

pts3 = np.array([[[100,300],[200,300],[100,400]],[[200,300],[300,300],[300,400]]]) 
# 두 개의 삼각형 꼭짓점 리스트 두개를 하나의 리스트로 감싼 형태. pts3 자체가 리스트.

cv2.fillPoly(img,pts3,COLOR,cv2.LINE_AA) # pts3은 이미 리스트라 [pts3]으로 할 필요가 없다.
# 속이 찬 다각형 = cv2.fillPoly(스케치북,그릴 위치,색깔,선의 종류)
# 속이 찬 다각형이기에 두께랑 열림/닫힘여부는 필요가 없는 인수이다.

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

