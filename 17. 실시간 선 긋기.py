#!/usr/bin/env python
# coding: utf-8

# # 실시간 선 긋기
# 
# 현재 마우스가 위치한 지점까지 선이 자동으로 그어진 상태를 만든다.

# In[9]:


import cv2
import numpy as np

source_img = cv2.imread('newspaper.jpg') 

point_list = [] 

COLOR = (255,255,255) 
THICKNESS = 3     
DRAWING = False   

def mouse_handler(event,x,y,flags,param):
    global DRAWING
    copy_img = source_img.copy() 
    # source_img를 복제한 새로운 창을 만듦. 이걸 선언하여 source_img창에 마우스 이동궤적에 따른 연속적인 선이 생기지 않도록 우회.
    
    if event == cv2.EVENT_LBUTTONDOWN: # 이 부분에서 따로 _MOVE를 지정하지 않았기에 마우스 움직임에 실행되지 않는 상태이다.
        point_list.append((x,y)) 
        DRAWING = True 
    
    if DRAWING :
        prev_point = None 
        for point in point_list:
            cv2.circle(copy_img,point,10,COLOR,cv2.FILLED) # 복제 이미지를 그리는 곳으로 지정
                  
            if prev_point: 
                cv2.line(copy_img,prev_point,point,COLOR,THICKNESS,cv2.LINE_AA) # 복제 이미지를 그리는 곳으로 지정
            
            prev_point = point 
        
        next_point = (x,y) # 마우스핸들러로부터 받아온 마우스 픽셀 좌표 매개변수를 받아 오며 계속 갱신 중임.
        if len(point_list) == 4: # 좌표 4개가 지정되면 더이상 마우스로 직선을 그을 이유가 없고 첫번째 지점과 연결해야 함.
            show_result() 
            next_point = point_list[0] # 다음 지정 좌표를 첫 좌표로 변경
            
        cv2.line(copy_img,prev_point,next_point,COLOR,THICKNESS,cv2.LINE_AA)
        # 그려지는 이미지를 copy_img 로 바꾸고 이어지는 포인트를 point에서 next_point로 변경을 해 준다.
        

    
    cv2.imshow('img',copy_img) # 복제창으로 바꿈

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


# ![image-3.png](attachment:image-3.png)
# 
# 첫번째 지점을 선택하자마자 마우스 위치에 따른 실시간 직선이 생기도록 만들었다.  
# 만약 copy_img 가 아닌 source_img 에 직선을 그리면 지워지지 않고 마우스커서를 따라 번지듯 생기는 직선들이 그려지게 된다.
