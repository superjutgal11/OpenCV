#!/usr/bin/env python
# coding: utf-8

# ## 텍스트
# 
# OpenCV에서 제공하는 글꼴 종류는 다음과 같다.
# 1. cv2.FONT_HERSHEY_SIMPLEX          : 보통 크기의 산 세리프(sans-serif) 글꼴
# 1. cv2.FONT_HERSHEY_PLAIN            : 작은 크기의 산 세리프 글꼴
# 1. cv2.FONT_HERSHEY_TRIPLEX          : 보통 크기의 세리프 글꼴
# 1. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX   : 필기체 스타일 글꼴
# 1. cv2.FONT_ITALIC           : 기울임(이탤릭체) , 다른 폰트를 먼저 지정 이후 사용

# In[14]:


# 텍스트도 도형처럼 빈 스케치북을 만들고 작성한다.

import numpy as np
import cv2

img = np.zeros((480,640,3),dtype=np.uint8)

SCALE = 1 # 글자 크기
COLOR = (255,255,255) # 흰색
THICKNESS = 3

cv2.putText(img,"SIMPLEX",(20,50),cv2.FONT_HERSHEY_SIMPLEX,SCALE,COLOR,THICKNESS)
cv2.putText(img,"PLAIN",(20,150),cv2.FONT_HERSHEY_PLAIN,SCALE,COLOR,THICKNESS)
cv2.putText(img,"TRIPLEX",(20,250),cv2.FONT_HERSHEY_TRIPLEX,SCALE,COLOR,THICKNESS)
cv2.putText(img,"SIMPLEX",(20,350),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,SCALE,COLOR,THICKNESS)
cv2.putText(img,"ITALIC",(20,450),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX|cv2.FONT_ITALIC,SCALE,COLOR,THICKNESS)
# 위의 5번째 줄 이탤릭은 앞에 다른 폰트와 | 를 통해 동시에 입력한다.

# cv2.putText(스케치북,"쓸 내용",(시작 좌표),글자폰트,글자크기,색깔,글자두께)

cv2.imshow('text image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) # 맥북 닫힘 에러 해결

# 맨 처음 할당 변수들(두께,크기 등)을 바꿔 출력물의 결과를 바꿀 수 있다.


# ### 출력치
# 
# ![image-3.png](attachment:image-3.png)

# ## 한글 우회

# In[17]:


# 이번 코드는 한글이 cv2 라이브러리에서 안됨을 설명한다.

import numpy as np
import cv2

img = np.zeros((480,640,3),dtype=np.uint8)

SCALE = 1 
COLOR = (255,255,255) # 흰색
THICKNESS = 3

cv2.putText(img,"정재형",(20,50),cv2.FONT_HERSHEY_SIMPLEX,SCALE,COLOR,THICKNESS)
# 첫번째 코드 변경없이 영어대신 한글을 적어버리면 출력문이 ?????? 로 나온다. openCV에서 한글을 제공하지 않기 때문인데 우회를 해야한다.
# 다른 라이브러리의 도움을 받아야 한다.

cv2.imshow('text image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) 


# ### 출력창
# ![image.png](attachment:image.png)
# 
# 이렇게 cv2 라이브러리에서는 한글출력이 지원되지 않기 때문에 FIL (python image library)를 쓴다.   
#   
# 이 라이브러리를 쓰기 위해서는 from PIL import ImageFont,ImageDraw,Image를 임포트하여 가져오고,  
# 새로운 함수를 정의한다.

# In[8]:


import numpy as np
import cv2
# 한글 우회 라이브러리를 가져옴
from PIL import ImageFont,ImageDraw,Image

def myPutText(src,text,pos,font_size,font_color): # 매개변수 : 스케치북 , "내용" , 폰트위치 , 폰트크기 , 폰트색깔
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('AppleGothic.ttf',font_size) 
    draw.text(pos,text,font=font,fill=font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3),dtype=np.uint8)

FONT_SIZE = 30
COLOR = (255,255,255) # 흰색

# 위에서 만든 함수에 인수를 넣기. return함수이기에 받아줄 변수(kr_img)에 넣었다.
kr_img = myPutText(img,"정재형입니다.",(20,50),FONT_SIZE,COLOR)

cv2.imshow('kr text image',kr_img)
cv2.waitKey(0)
cv2.destroyAllWindows
cv2.waitKey(1)


# ![image.png](attachment:image.png)
# 
# 맥북환경에서 서체를 찾는 방법은 다음과 같다.
# 1. finder 켜기
# 1. 응용프로그램 > 서체관리자 켜기
# 1. 모든 서체 보기
