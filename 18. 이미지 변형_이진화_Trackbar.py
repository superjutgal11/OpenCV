#!/usr/bin/env python
# coding: utf-8

# # 이미지 변형 _ 이진화
# 
# 이진화 : 특정값을 기준으로 흰색과 검은색만을 갖는 바이너리 이미지로 바꾸는 과정.

# In[2]:


import cv2

img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE) # 이진화를 하려면 GRAYSCALE로 읽어와야 한다.

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# 위처럼 이진화를 위해선 먼저 사진을 불러올 때 GRAYSCALE로 받아오고나서, 쓰레스홀드를 써야 한다.  
# 쓰레스홀드를 이해하기 위해 다음의 상황을 생각해보자.  
# 
# 만약 바닥에 다양한 크기의 보석이 흩뿌려져 있고 각 보석을 1초에 1개씩 가져갈 수 있다.  
# 만약 10초의 시간 뿐이라면 큰 보석에서 작은보석 순서대로 챙길 것이고, 시간 제한이 없다면 크기 상관없이 아무거나 주울 것이다.  
# 주어진 시간에 따라 작은보석/중간보석/큰보석 에서 챙기는 기준이 달라진다.  
# 이때 이 기준이 쓰레스홀드 즉 임계값이 된다.

# In[4]:


import cv2

img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE) 

# 임계값을 지정하기 위해서 쓰레스함수를 사용한다. 리턴값이 두 개이므로 값을 받을 변수를 2개 지정한다.
ret , binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # 리턴값은 여기선 쓰지 않으므로 변수를 _ 로 처리해도 된다.
# threshold(처리할 이미지,임계값(255를 2로 나눈 임의의 값을 넣음),임계값을 넘었을 때 밸류지정(흰색으로 변환,나머지는 검정)
# cv2.THRESH_BINARY 이미지를 이진화하는 데 사용되는 상수

cv2.imshow('img',img)
cv2.imshow('binary',binary) # 받아온 바이너리(이진화) 이미지를 출력
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
# 
# 값을 변형시켜가며 달라지는 것을 확인하고 싶을 때 트렉바를 사용할 수 있음.  
# ## Trackbar ( 값 변화에 따른 변형 확인 )

# In[ ]:


import cv2

def empty(pos): # 트렉바의 값을 받는 매개변수 = 포지션
    pass


img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE) 

# 트렉바를 사용하기 위해 윈도우를 하나 만들어 둬야 함.
name = 'Trackbar'
cv2.namedWindow(name) # Trackbar라는 이름의 윈도우를 하나 만들어 둠.

cv2.createTrackbar('트렉 바',name,127,255,empty)
# 트렉바 만드는 함수 > cv2.createTrackbar('바의 이름',바가 들어갈 윈도우 이름,초기값,최댓값,값을 바꿀 때 이벤트 처리함수)

while True: # 무한 루프. 트렉바로 받은 값을 바탕으로 제어해야 함.
    thresh = cv2.getTrackbarPos('트렉 바',name) 
    # 트렉바로 받은 값을 저장 : cv2.getTracbarpos('바의 이름',바가 들어가 있는 윈도우 이름)
    
    ret , binary = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY) # thresh를 임계값으로 넣어 줌.
    
    if not ret: # return 값이 없다면
        break
        
    cv2.imshow(name,binary)
    
    if cv2.waitKey(1) == ord('q'): # q를 누르면 종료
        break

cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
# 
# ![image-2.png](attachment:image-2.png)
