#!/usr/bin/env python
# coding: utf-8

# # 지점 선 긋기

# In[3]:


# 15강에서 했던 미니프로젝트의 코드를 가져와 수정해가며 활용해 보았다.

import cv2
import numpy as np


source_img = cv2.imread('newspaper.jpg') 

point_list = [] 


COLOR = (255,0,255) 
THICKNESS = 3     # 선에 필요한 두께에 대한 변수를 할당
DRAWING = False   # 선을 그릴지 여부

def mouse_handler(event,x,y,flags,param):
    global DRAWING # mouse_handler함수에서 외부 전역변수 DWAWING을 사용하겠다는 선언식
    
    if event == cv2.EVENT_LBUTTONDOWN: 
        point_list.append((x,y)) 
        DRAWING = True # 버튼 클릭 시 참으로 됨(선을 그리기 시작)
    
    if DRAWING : # Drawing 이 참이 되면 분기
        prev_point = None # 직선의 시작점
        for point in point_list:
            cv2.circle(source_img,point,10,COLOR,cv2.FILLED) # 동그라미를 그리고
            
            # 직선도 그려야 하는데 점이 1개이면 그릴 수가 없다. 선이 2개는 되어야 이어 그릴 수 있으니 그 논리를 구현한다.
            
            if prev_point: # None이면 F이고 수가 들어 있으면 T이므로 이 식은 prev에 값이 있으면 분기한다는 의미이다.
                cv2.line(source_img,prev_point,point,COLOR,THICKNESS,cv2.LINE_AA)
                # 소스_이미지창에 prev부터 현재포인트까지 색과 두께를 지정한 라인을 그리며 라인타입은 AA임.
            
            prev_point = point # 두번째 포인트 지정 시부터 그리기 시작하게 됨.
        
        
    if len(point_list) == 4: 
        show_result() 
    
    cv2.imshow('img',source_img)


def show_result():
    width,height = 640,240
    src = np.float32(point_list) 
    dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32) 
    
    mtr = cv2.getPerspectiveTransform(src,dst) 
    result = cv2.warpPerspective(source_img,mtr,(width,height))
    cv2.imshow('result',result)
    
    
cv2.namedWindow('img') 
cv2.setMouseCallback('img',mouse_handler)
cv2.imshow('img',source_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
# 
# 잘 실행 되었으나 4번째 지점과 1번째 지점이 연결되지 않은 채 출력되었고, 두 지점을 클릭해야 비로소 선이 연결됨을 확인할 수 있다.
# 다음 장에서는 실시간 선 긋기로 이 부분을 보완해보겠다.
