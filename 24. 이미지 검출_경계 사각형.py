#!/usr/bin/env python
# coding: utf-8

# # 경계 사각형
# 
# : 윤곽선의 경계면을 둘러싸는 사각형  
# : 경계 사각형 함수 > boundingRect()

# In[4]:


# 23강의 코드를 가져오고 필요한 부분을 추가해간다.

import cv2
img = cv2.imread('card.png')

target_img = img.copy() 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 
# LIST로 모든 윤곽선을 찾아 온다. 여기서 contours(윤곽선 정보)는 아래 반복문에서 사용된다.

COLOR = (0,200,0) 
THICKNESS = 2

for cnt in contours: # 반복
    x , y , width , height = cv2.boundingRect(cnt)
    # 윤곽선을 둘러싸고 있는 사각형 정보를 x좌표, y좌표, 가로길이, 세로길이를 받아 온다. 반환값이 4개란 뜻임.
    cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)
    # 매개변수 순서 (스케치북,좌측상단 좌표,우측하단 좌표,색깔,두께,선택사항:선 타입,선택사항:좌표값 정밀도)

cv2.imshow('img',img) 
cv2.imshow('target_img',target_img) 

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)

# # 윤곽선의 면적을 구하기
# 
# contourArea( ) 함수를 사용하여 구한다.  
# 위 코드에서는 사진 내 모든 윤곽선을 다 구해왔는데, 이번엔 특정 면적이 넘는 윤곽선만 검출해 내고자 한다면  
# 예를들어 위에서 카드의 갯수를 알고싶다면 카드 내부의 문양은 지워야 한다.  이런 경우에 사용할 수 있다.

# In[5]:


import cv2
img = cv2.imread('card.png')

target_img = img.copy() 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 

COLOR = (0,200,0) 
THICKNESS = 2

for cnt in contours: # 넓이를 구할 때 여기 밑을 수정한다.
    if cv2.contourArea(cnt) > 25000: # 안에 윤곽선 정보를 넣고 원하는 면적의 비교연산을 진행. (가로길이 픽셀 x 세로길이 픽셀)
        x , y , width , height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)

cv2.imshow('img',img) 
cv2.imshow('target_img',target_img) 

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
