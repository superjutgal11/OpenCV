#!/usr/bin/env python
# coding: utf-8

# Threshold 함수로 이진화하는 방법을 배워 왔는데, Threshold의 문제가 있다.  
# ![image.png](attachment:image.png)
# 위 사진에서 책에 있는 글자를 받아 오고 싶은데, Threshold로 받아오면 글자들이 흰색으로 변질되어 버린다.  
# 이를 해결하기 위해 어댑티브 쓰레시홀드를 사용할 수 있다.

# ## Adaptive Threshold
# : 일반 Threshold는 사진 전체에 임계치를 적용하지만 Adaptive Threshold는 영역을 세분화(작은 영역으로 나눔)하여 임계치를 적용할 수 있다.

# In[28]:


# 18강의 trackbar코드를 가져와 수정했다.


import cv2

def empty(pos): 
    pass


img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE) 

name = 'Trackbar'
cv2.namedWindow(name)


cv2.createTrackbar('block_size',name,25,100,empty) 
# blocksize는 세분화하는데의 블럭 크기를 정의하며, 홀수만 가능하고 1보다는 큰 값을 정의해야 함.

cv2.createTrackbar('c',name,3,10,empty)
# c 는 상수값으로 쓸 것이고 일반적으로 양수의 값을 씀

while True: 
    
    block_size = cv2.getTrackbarPos('block_size',name) 
    c = cv2.getTrackbarPos('c',name) 
    # 트랙바는 최소값이 0이고 우린 범위를 1~100 이며 홀수만을 받으려 하기 때문에, 짝수가 오면 홀수로 바꿔주는 처리를 진행한다.
    
    if block_size <= 1: # 1이하면 3으로 처리
        block_size = 3
        
    if block_size % 2 == 0: # 짝수라면
        blck_size += 1 # 홀수로 바꿔 줌
    
    binary = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,c)
    # adaptiveThreshold 로 함수이름을 바꿔 줌. 해당 함수는 리턴값이 1개임.
    # cv2.adaptiveThreshold(창,임계치 초과 시 처리치,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blocksize,c)
    
    cv2.imshow(name,binary) 
    
    if cv2.waitKey(1) == ord('q'): 
        break

cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
# 
# 음영이 다르거나 빛의 반사가 심해 특정 부분은 밝고 특정 부분은 어두운 등의 경우는 어댑티브 쓰레시를 사용하면 됩니다.

# # 오츠 알고리즘
# 
# : 오츠가 개발한 최적의 임계치를 자동적으로 발견하도록 만든 알고리즘.

# In[30]:


import cv2

img = cv2.imread('book.jpg',cv2.IMREAD_GRAYSCALE) 

ret , binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # 일반 threshold
ret , otsu = cv2.threshold(img,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 오츠 알고리즘 적용
# OTSU알고리즘을 사용 시 초기값이 무시되므로 알아보기 쉽게 -1을 넣었다.

print('otsu threshold = ',ret)
# 최적의 임계치를 출력

cv2.imshow('img',img)
cv2.imshow('binary',binary)
cv2.imshow('otsu',otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
# 
# 오츠알고리즘은 Bimodal Imaged에 사용하기에 적합한 처리방법이다.
