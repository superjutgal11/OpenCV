#!/usr/bin/env python
# coding: utf-8

# # 환경설정
# 
# 아나콘다 프롬프트(맥북에선 터미널)에서 다음 명령을 수행함.  
# > pip install opencv-python
# 
# 환경설정이 잘 되었는지 확인을 위해 다음을 임포트한다.
# > import cv2
# > cv2.__version__

# In[8]:


# 환경설정 코드

import cv2
cv2.__version__


# ## OpenCV (Computer Vision)
# 
# 다양한 영상(이미지)/동영상 처리에 사용되는 오픈소스 라이브러리

# # 1. 이미지 출력
# 
# 필자는 pixabay에서 무료이미지를 받아 옴.

# In[28]:


import cv2

img = cv2.imread('img.jpg')#해당 경로의 파일 읽어오기
cv2.imshow('img',img)    #imshow('창의 이름',보여줄 이미지 객체 선택)
cv2.waitKey(0)       #표시하자마자 끝나면 안되므로 특정 동작을 할 때까지 기다리기 위해 넣음. waitkey는 특정 키 입력까지 기다리는 것.
                        #0을 넣으면 무한정 대기하라는 의미임. 이후 다음 셀로 내려가 계속 실행.
cv2.destroyAllWindows()    #모든 창 닫기
cv2.waitKey(1)             #맥북에서 위 명령으로 창이 잘 안닫히는데 이거 밑에 써주면 잘 닫힘.


# imread()는 OpenCV에서 이미지를 읽어오는 함수이다. img객체에 사진파일의 이름을 적는다.  
# 여기서 사진을 불러오기 위해서는 현재 작업하는 디렉토리내로 사진을 옮겨야 한다.  
#   
# - import os  
# - print(os.getcwd())  
# 
# 위 두 줄로 현재 작업하는 디렉토리의 주소를 복사할 수 있다. 터미널에서   
# cp 옯기려는현재사진경로 옮길디렉터리경로   
# 를 통해 옮길 수 있다.  
# 
# imshow( , )함수는 OpenCV에서 이미지를 화면에 표시하는 함수다.  
# 이 함수는 두 개의 인자를 받는데 첫 번째 인자는 창의 이름(Title), 두 번째 인자는 표시할 이미지의 이름이다.  
#   
# waitKey()는 사용자의 입력을 기다리는 함수로 들어가는 숫자는 ms 단위이기에 5000을 넣으면 5초이다.  
# 0을 넣으면 특정 키를 입력할 때까지 무한정 기다린다.  
# 
# destroyAllWindows() 는 매개변수를 받지 않으며, 현재 열려있는 모든 창을 닫는 함수이다.  
# 꿀팁으로 맥에서 잘 안닫히는 경우 많은데 cv2.waitKey(1) 를 밑에 써주면 잘 닫힌다.

# In[29]:


#아스키코드 출력

import cv2
img = cv2.imread('img.jpg')

cv2.imshow('img2',img)     # 같은 사진파일을 띄우는 창 이름을 바꾸고
key = cv2.waitKey(0)       # key라는 변수에 waitKey()를 할당.
cv2.destroyAllWindows()    # 키 입력되어 창 종료. 이때 내가 누른 키의 아스키 값이 key로 들어감.
cv2.waitKey(1)             # 맥북에러, 확실히 종료
print(key)                 # 아스키코드 출력. 무슨 버튼을 눌렀냐에 따라 값이 달라짐

# 이 아스키코드를 이용하여 특정 키를 누른 경우에 하고싶은 동작을 설정하는 등의 코드를 작성할 수 있음. 나중에 설명.


# ## 이미지출력의 3가지 읽기 옵션
# 
# 1. cv2.IMREAD_COLOR : 컬러이미지로 불러오기. 투명영역은 무시되고 이미지를 이걸로 읽어오면 이 코드가 기본값으로 설정됨.
# 1. cv2.IMREAD_GRAYSCALE : 흑백이미지로 불러오기.
# 1. cv2.IMREAD_UNCHANGED : 사진을 바꾸지 않고 불러오기. 투명영역까지 포함되어 불러옴.

# In[10]:


import cv2

img_color = cv2.imread('img.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow("img_color",img_color)
cv2.imshow("img_gray",img_gray)
cv2.imshow("img_unchanged",img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
            
#출력 결과 : 3개의 창이 뜨고 각각 한 사진을 다르게 읽어오고 출력함.


# ![image.png](attachment:image.png)

# ## Shape
# 
# 불러온 이미지의 높이와 너비 등의 정보를 출력하는 함수.  
# 높이(세로), 가로(너비), 채널정보순으로 출력됨.

# In[13]:


import cv2
img = cv2.imread('img.jpg')
img.shape

# 출력값 : (427, 640, 3)    
# 채널정보가 3이라는 건 r,g,b를 말하고 나중에 투명영역도 다루면 투명까지 4가 출력될 것이나 jpg이므로 여기선 3 출력.

