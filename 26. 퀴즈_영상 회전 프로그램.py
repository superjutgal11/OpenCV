#!/usr/bin/env python
# coding: utf-8

# # 퀴즈_OpenCV를 이용하여 가로로 촬영된 영상을 세로로 회전하는 프로그램 작성
# 
# ## # 조건
# 1. 회전은 시계 반대방향으로 90도 회전시킨다.
# 1. 재생속도는 원본의 4배 속도로 한다.
# 1. 원본 파일명 : city.mp4 , 출력 파일명 : city_output.avi (코덱 : DIVX)

# In[7]:


import cv2
cap = cv2.VideoCapture('city.mp4') # 원본 파일을 불러 옴
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 정수변환 필요
height= round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 비디오 writer 객체 생성
out = cv2.VideoWriter('city_output.avi',fourcc,fps*4,(height,width)) 
# fps4배 적용 , 90도 회전할 것임으로 높이와 낮이의 위치를 서로 변경

while cap.isOpened(): # 오픈에 문제가 없을 시 
    ret , frame = cap.read()
    if not ret: # 더 이상 가져올 프레임이 없을 시 루프 종료
        break
        
    
    # 시계 반대 방향으로 90도 회전
    rotate_frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
    # 회전한 프레임을 out객체에 저장
    out.write(rotate_frame)
    
    cv2.imshow('video',frame)
    cv2.imshow('video',rotate_frame) # 프레임을 video창에 출력
    
    if cv2.waitKey(1) == ord('q'):
        break
        
out.release()
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)


# In[ ]:




