#!/usr/bin/env python
# coding: utf-8

# ## 이미지를 파일로 저장
# 
# OpenCV에서는 이미지를 회전,흑백화 등 다양한 처리를 할 수 있는데 그 결과물을 다운받는 방법이라고 생각하면 된다.  
# 이미지에 대한 처리는 나중에 하고 이미지 저장부터 배운다.

# In[7]:


import cv2
img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

# 위쪽 코드는 기본적인 이미지 불러오기 코드임.

result = cv2.imwrite('img_save.jpg',img) # 위 이미지를 img.jpg로 저장한 것을 bool로 받음. 
print(result) # 정상적으로 저장 시 True 출력


# 잘 저장됨을 확인함
# 
# ![image.png](attachment:image.png)

# In[10]:


import cv2
img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE) 
cv2.imshow('img',img) # 중앙에 버튼 누를 때까지 딜레이 함수 부분 없앰.
result = cv2.imwrite('img_save.png',img) # jpg뿐 아닌 png확장자도 가능.
print(result) 


# png로 저장됨을 확인
# 
# ![image.png](attachment:image.png)

# ## 동영상 저장

# In[4]:


import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret,frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('video',frame)
    if cv2.waitKey(10) == ord('q'): # q 누르면 창 끄기
        break
    
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1) # 맥북 닫기

# 위쪽은 기본적인 동영상 재생 함수


# 코덱 : 코더/디코더의 합성어로 동영상, 음성, 이미지 등의 멀티미디어를 압축하고 다시 해제하여 저장 혹은 전송할 때 쓴다.사용 이유는 저장공간 절약, 전송효율, 재생성능 향상 등이 있다.
# 
# 문자 코드 : 인간의 문자를 컴퓨터가 이해할 수 있도록 하는 체계. 대표적으로 아스키코드가 있다.  

# In[5]:


# 위 방식으로 불러온 동영상을 다른 형식으로 저장하는 코드를 작성 해 보자. 
# 코덱 정의 > 프레임 크기와 재생속도 정의 > 반복문으로 영상 저장 과정을 거친다.

import cv2
cap = cv2.VideoCapture('video.mp4')

# 코덱 정의(어떤 형태로 저장할 것인지 정의)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# fourcc 에서 cc 는 캐릭터코드(문자코드)를 의미.
# *'DIVX' 는 'D','I','V','X' 의 축약식으로 *는 시퀀스 객체의 요소들을 각각 떼어 내오는 연산자이다. 비디오 압축 기술을 의미함.

# 코덱 정의 후 어떤 크기,속도,fps로 저장할지 지정해야 함.

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 크기 변경 가능
# width에는 정수가 들어가야 하므로 반올림 함수 round로 감싸준다. 영상의 속성창에서 넓이 확인이 가능한데 그걸 그대로 받아오는 함수임.

height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 크기 변경 가능
# height에는 정수가 들어가야 하므로 반올림 함수 round로 감싸준다. 영상의 속성창에서 높이 확인이 가능한데 그걸 그대로 받아오는 함수임.

fps = cap.get(cv2.CAP_PROP_FPS) # 만약 여기에 *2 를 곱하면 2배 재생속도가 되는 것이다.
# 해당 영상의 재생속도를 받아 온다.

# 최종적으로 비디오라이터 객체를 만듦
out = cv2.VideoWriter('output.avi',fourcc,fps,(width,height)) # 코덱에서 CIVX이기에 확장자는 .avi로
# 저장 파일명, 코덱, FPS, 크기(넓이,높이)


while cap.isOpened():
    ret,frame = cap.read()
    
    if not ret:
        break
    
    out.write(frame) # 영상 데이터만 저장(소리는 저장되지 않음)
    
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'): # q 누르면 창 끄기
        break
    
    
out.release() # 자원 해제

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1) # 맥북 닫기

