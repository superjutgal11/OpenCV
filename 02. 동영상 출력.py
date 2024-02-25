#!/usr/bin/env python
# coding: utf-8

# # 2. 동영상 출력
# 
# pexels.com 에서 무료 제공하는 영상들을 사용하였다.

# In[2]:


import cv2
cv2.__version__


# In[3]:


import os
print(os.getcwd())


# 비디오 이름은 video.mp4 로 하였으며, 현재 작업 디렉토리로 옮기는 과정을 수행했다.
# 
# 터미널 ) cp /Users/jeongjaehyeong/Downloads/video.mp4 /Users/jeongjaehyeong/PythonImageWorkspace/OpenCV
# 
# 참고 : 파인더에서 선택한 파일 경로 복사하기 : command + option + c

# ## 동영상을 파일로부터 출력
# 
# 동영상은 프레임을 연속적으로 보여짐으로써 표현된다.  
# 동영상의 프레임을 반복문을 통해 가져오는 작업을 하게 된다.

# In[17]:


import cv2

cap = cv2.VideoCapture('video.mp4') # 비디오 캡처 객체를 생성하는 함수.

while cap.isOpened: # 동영상 파일이 올바로 열려있는지 확인함. false시 반복 수행 안됨. 정해진 수만큼 반복이 아니니 while이 유리!!!
    ret , frame = cap.read() #cap.read로 2개의 값을 반환. ret는 성공여부를 뜻하는 bool데이터, frame은 받아 온 이미지.
    
    if not ret:
        print("더 이상 받아 올 프레임이 없습니다.")
        break
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) == ord('q'): # ord(값) 은 q를 누르면 이라는 뜻임. 아스키코드의 q를 넣어도 동작은 같음.
        print("사용자 입력에 의해 영상이 종료됩니다.")
        break

cap.release() # 자원반환.openCV에서 비디오 처리 후 비디오 객체(여기선cap)의 자원반환이 필수임.
cv2.destroyAllWindows() # 모든 창 닫기
cv2.waitKey(1)


# 모든 프레임을 다 가져왔을 시, if not ret: 코드가 실행되며 반복문이 종료가 되며,  
# q를 누르면 if cv.2waitKey 의 코드가 실행되며 도중에 반복문이 종료가 된다.
# 
# 저 상태 그대로 실행 시 꽤 빠른 속도로 영상이 진행되는걸 알 수 있는데, if cv2.waitKey(1) == ord('q'): 에서  
# waitKey() 안의 수를 변경하여 영상속도를 제어할 수 있다. 수가 클수록 느리게 재생되며 fps라 한다. (프레임 퍼 세컨드)

# ## 카메라 영상 출력

# In[4]:


import cv2
cap = cv2.VideoCapture(0) # 비디오 캡처 객체를 생성하는 함수. 위는 파일 경로를 줬지만 여기선 디바이스 아이디를 적는다.
# 0을 쓰면 0번째 카메라장치를 의미. 여러개 장치가 있다면 그 중 선택을 할 수 있다.

if not cap.isOpened(): # 카메라가 열리지 않은 경우
    exit() # 프로그램 종료 함수
    
while True: # 무한반복
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('camera',frame)
    if cv2.waitKey(1)  == ord('q'):# q를 입력 시 종료하는 조건문
        break

cap.release()
cv2.destroyAllWindows() # 모든 창 닫기
cv2.waitKey(1)

