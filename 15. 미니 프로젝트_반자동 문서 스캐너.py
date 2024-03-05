#!/usr/bin/env python
# coding: utf-8

# # 미니 프로젝트 : 반자동 문서 스캐너
# 
# 지금까지 배운 내용들을 바탕으로 반자동 문서 스캐너를 만든다.  
# 이미지에서 4개의 지점을 클릭받아 해당 좌표를 저장하고, 모두 입력되면 원근 기법으로 직사각형 형태로 출력되게 만드는 프로제트이다.

# In[8]:


import cv2
import numpy as np


source_img = cv2.imread('newspaper.jpg') # 다운해 둔 포커사진 이미지를 읽어 온다

point_list = [] # 좌표를 넣을 빈 리스트를 선언해 둠

COLOR = (255,0,255) # BGR , 핑크색


def mouse_handler(event,x,y,flags,param): # 마우스 핸들러 함수를 만듦
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼을 누르는 이벤트 발생 시
        point_list.append((x,y)) # 튜플 형태로 클릭한 위치의 좌표값을 넣는다.
        
    for point in point_list:
        cv2.circle(source_img,point,10,COLOR,cv2.FILLED)
        # 4개의 클릭한 지점의 점을 그림에 그려 넣을 것이다.
        # source_img창에 중심좌표(point에 좌표가 있으니 그냥 point를 씀)에 반지름 10의 핑크색깔의 가득 찬 원을 그리는 함수임.
        
    if len(point_list) == 4: # 총 4번 이미지를 클릭할 시
        show_result() # 결과를 출력하는 새로운 함수
    
    cv2.imshow('img',source_img)
    # 마우스 클릭 때마다 변경된 이미지가(점이) img창에 덮어씌어진다.


def show_result():
    width,height = 640,240
    src = np.float32(point_list) # 포인트리스트의 4개 지점을 float32형태의 array를 만들어 주는 numpy함수로 input지정
    dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) # output 지정
    
    mtr = cv2.getPerspectiveTransform(src,dst) # 매트릭스를 얻어 옴
    result = cv2.warpPerspective(source_img,mtr,(width,height))
    cv2.imshow('result',result)
    
    
cv2.namedWindow('img') # img라는 이름의 핸들러를 먼저 만들어 준다.
cv2.setMouseCallback('img',mouse_handler)
cv2.imshow('img',source_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
