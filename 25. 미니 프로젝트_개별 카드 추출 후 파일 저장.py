#!/usr/bin/env python
# coding: utf-8

# # 미니 프로젝트_개별 파일 추출 후 파일 저장
# 
# ### 목표
# 
# 1. 카드가 여러장 주어진 파일에서 카드를 추출하여 작업 디렉토리 파일에 저장한다.  
# 1. 카드의 갯수만큼의 파일이 자동으로 저장되게 코딩한다.   

# In[ ]:


import cv2
img = cv2.imread('card.png')

target_img = img.copy() 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours , hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 

COLOR = (0,200,0) 
THICKNESS = 2

index = 1

for cnt in contours: 
    if cv2.contourArea(cnt) > 25000: 
        x , y , width , height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)
        
        # 카피 이미지로 저장하면 지저분하게 저장되므로 원본 이미지를 대상으로 작업하여 저장시키도록 한다.
        crop = img[y:y+height,x:x+width]
        
        cv2.imshow(f'card_crop{index}',crop) # 파일 열기
        cv2.imwrite(f'card_crop{index}.png',crop) # 파일 저장. 확장자 꼭 써주기.
        index+=1

        # 파이썬에서 f(포맷 문자열)을 앞에 써 주면 '' 내에서 {} 로 인덱스 접근이 가능함.
        
cv2.imshow('img',img) 

cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()


# ![image.png](attachment:image.png)
# 
# ![image-2.png](attachment:image-2.png)
# #디렉토리에 저장됨을 확인했다.
