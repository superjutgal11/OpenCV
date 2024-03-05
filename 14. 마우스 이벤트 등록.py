#!/usr/bin/env python
# coding: utf-8

# # 마우스 이벤트 등록
# 
# 

# ### 마우스 이벤트 등록
# : opencv 창에서 마우스 버튼을 누르거나, 떼거나, 움직이는 등의 이벤트를 처리하는 것을 의미함.

# In[ ]:


import cv2


def mouse_handler(event,x,y,flags,param): # 마우스에 특정 동작을 하면 실행되는 함수를 선언
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼을 누르는 이벤트 발생 시
        print("왼쪽버튼 다운")
        print(x,y) # x와 y가 현재 클릭된 사진의 좌표가 되고 그 좌표를 출력하는 함수
        
    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼을 뗌
        print("왼쪽버튼 업")
        
    elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼쪽 버튼을 더블(DBL)클릭(CLK)한 경우
        print("왼쪽버튼 더블클릭")
        
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동 이벤트
        pass # print("마우스가 이동 중") 너무 출력이 많이 되어서 주석처리함.
    
        # 위 이벤트들의 L 을 R 로 바꾸면 오른쪽 버튼으로 바뀌게 됨 !!!!
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("오른버튼 다운")
        
    elif event == cv2.EVENT_MBUTTONDOWN: # 휠 버튼 클릭
        print("휠 버튼 클릭")

    
img = cv2.imread('poker_1.jpg')
cv2.namedWindow('img')
# 이미지를 표시할 윈도우를 생성하는 함수로, 마우스 이벤트 등록 전에 선언 해 둬야 함.


cv2.setMouseCallback('img',mouse_handler)
# 마우스 이벤트를 처리하기 위해 사용되는 함수로서, 이미지 윈도우에서 발생하는 마우스 이벤트를 감지하고 그에 따른 동작을 정의한다.
# 마우스 이벤트가 발생할 때마다 호출되는 함수이기에 for문 등을 써서 반복할 필요가 없다.


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)


# ![image.png](attachment:image.png)
