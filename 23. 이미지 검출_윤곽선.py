#!/usr/bin/env python
# coding: utf-8

# # 이미기 검출 : 윤곽선
# 
# ## 윤곽선 ( Contour ) : 경계선을 연결한 선

# In[4]:


import cv2
img = cv2.imread('card.png')

# 윤곽선 검출을 위해서는 정확성을 높이기 위해 바이너리 이미지를 사용한다. 즉 쓰레스홀드 등으로 전처리 과정을 함.
# 몇몇 함수는 원본 이미지를 수정 후 원본이미지로 저장해버리기에 원본 이미지 복사본에서 작업을 하도록 한다.

target_img = img.copy() # 사본 이미지를 하나 만듦

# 바이너리 처리를 진행
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 오츠 알고리즘으로 최적의 임계치를 받아 옴
ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 오츠 알고리즘으로 윤곽선을 찾아 본다. contours 함수를 쓸 것이다.
# contours 함수를 쓰면 윤곽선의 정보와 윤곽선간의 구조,계층구조 총 2개의 반환값을 낸다.

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) # 윤곽선 검출 함수
# 윤곽선 정보 , 윤곽선 구조 = cv2.findContours(이미지,윤곽선 찾는 모드,윤곽선 찾을 떄 쓰는 근사치 방법)

COLOR = (0,200,0) # 녹색
THICKNESS = 2

# 윤곽선 정보를 윤곽선 그려주는 함수에 넣어 윤곽선을 그려준다.
cv2.drawContours(target_img,contours,-1,COLOR,THICKNESS) # 윤곽선 그리는 함수
# 대상 이미지(복사본),윤곽선 정보, 인덱스(-1이 아니면 해당 윤곽선만을 그림),색깔,두께
# -1이면 모든 윤곽선을 다 그리라는 의미임.

cv2.imshow('img',img) # 원본 출력
cv2.imshow('gray',gray) # 바이너리 출력
cv2.imshow('otsu',otsu) # 오츠 출력
cv2.imshow('target_img',target_img) # 윤곽선 이미지 객체 출력

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image-2.png](attachment:image-2.png)

# contours , hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)  
# 에서 윤곽선 찾는 모드를 REFR_LIST 를 썼는데, 다른 것을 쓰고 변화를 봐 보자. 
# 
# 
# ## 윤곽선 찾기 모드
# 
# 1. cv2.RETR_EXTERNAL  : 가장 외각의 윤곽선만 찾음
# 1. cv2.RETR_LIST      : 모든 윤곽선을 찾음      (계층정보 없음)
# 1. cv2.RETR_TREE      : 모든 윤곽선을 찾음      (계층 정보를 트리 구조로 생성)
# 

# In[7]:


import cv2
img = cv2.imread('card.png')

target_img = img.copy() 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

COLOR = (0,200,0) 
THICKNESS = 2

cv2.drawContours(target_img,contours,-1,COLOR,THICKNESS) 

cv2.imshow('img',img) 
cv2.imshow('target_img',target_img) 

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ## RETR_EXTERNAL
# ![image.png](attachment:image.png)

# In[10]:


import cv2
img = cv2.imread('card.png')

target_img = img.copy() 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 

print(hierarchy) # 트리 구조 구성 출력
print(len(contours)) # 총 몇개의 윤곽선이 발견되었는지 확인

COLOR = (0,200,0) 
THICKNESS = 2

cv2.drawContours(target_img,contours,-1,COLOR,THICKNESS) 

cv2.imshow('img',img) 
cv2.imshow('target_img',target_img) 

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# # RETR_TREE
# ![image.png](attachment:image.png)
# 
# 그리고 밑에 트리(계층)구조의 형태를 출력했다.
