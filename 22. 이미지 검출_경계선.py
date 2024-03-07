#!/usr/bin/env python
# coding: utf-8

# # 이미지 검출 : 경계선
# 
# 인간의 눈으로 어떤 물체를 보고 경계선을 구분하는 것은 급격한 색의 변화가 있는 지점에서의 판단에 의한 것이다.  
# 컴퓨터도 똑같기에 어떤 사진의 픽셀의 색이 급격히 변화하는 지점을 경계선으로서 검출해낼 수 있다.  

# ## Canny Edge Detection 기법 : 가장 대중적인 경계선 검출 기법

# In[4]:


import cv2
img = cv2.imread('snowman.png')

canny = cv2.Canny(img,250,200)
# 매개변수 = 개상 이미지, min Value(하위 임계값), max Value(상위 임계값)
# 이미지 픽셀이 상위 임계값보다 큰 변화(기울기)를 가지면 경계선으로 간주, 하위임계값보다 낮은 경우 경계선으로 고려하지 않음.

cv2.imshow('img',img)
cv2.imshow('img_2',canny)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)

# In[2]:


# Threshold 값을 변경해 보며 어떻게 결과가 달라지는지 확인해 보자. 이번에는 트렉바를 사용하도록 한다.

import cv2
img = cv2.imread('snowman.png')

def empty(pos): # 핸들러 함수 empty는 pass로 비워 둔다.
    pass

name = 'Track bar' # 트렉바 사용 전 윈도우가 먼저 만들어져야 함.
cv2.namedWindow(name) # 
cv2.createTrackbar('threshold_1',name,0,255,empty) # min value
cv2.createTrackbar('threshold_2',name,0,255,empty) # max value


while True:
    threshold_1 = cv2.getTrackbarPos('threshold_1',name)
    threshold_2 = cv2.getTrackbarPos('threshold_2',name)
    
    canny = cv2.Canny(img,threshold_1,threshold_2) # 트렉바 값을 하위 임계값과 상위 임계값으로 설정

    cv2.imshow('img',img)
    cv2.imshow(name,canny) # 트렉바가 포함되도록
    
    if cv2.waitKey(1) == ord('q'): # q 입력 시 루프 탈출
        break
    
cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 처음에는 하늘색체의 미세한 색갈차이에도 선이 그러질 정도로 민감하게 반응한다.  
# 
# ![image-2.png](attachment:image-2.png)
# 최대 임계값을 늘릴수록 민감도가 낮아진다.  
# 
# ![image-3.png](attachment:image-3.png)
# 하위도 마찬가지이다.
