#!/usr/bin/env python
# coding: utf-8

# # 동영상 크기 조정
# 
# 
# 전체적으로 이미지 크기 조정과 비슷하다.  
# 
# 1. 고정크기로 설정

# In[14]:


import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret,frame = cap.read() # ret는 리턴을 의미함
    if not ret:
        break
        
    frame_resized = cv2.resize(frame,(800,500)) # resize 함수 사용
    
    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


# 2. 비율로 설정

# In[16]:


import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret,frame = cap.read() # ret는 리턴을 의미함
    if not ret:
        break
        
    frame_resized = cv2.resize(frame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC) # resize 함수 사용
    
    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

