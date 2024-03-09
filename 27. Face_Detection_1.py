#!/usr/bin/env python
# coding: utf-8

# # 얼굴 인식 프로젝트_1
# 
# ## 얼굴인식 관련 학문
# 
# 1. face detection [ 얼굴 검출 ] : 이미지/영상에서 인간의 특성을 파악하여 인식함.  
# 1. face recognition [ 얼굴 인식 ]: 이미지/영상에서 인간의 얼굴이 누구인지 파악함.  
# 
# 참고로 추적은 tracking 이라고 함.

# 사용할 라이브러리는 mediapipe라는 라이브러리로, 구글에서 제공하며 비디오 형식 데이터를 대상으로 AI기능을 파이프라인 형태로 쉽게 사용할 수 있도록 돕는다.  
# 여러 데이터셋을 통한 훈련이 된 상태이기에 간단히 사용이 가능하다. 대표적인 기능으로는 다음과 같다.  
# 
# 1. Face Detection
# 1. Face Mesh : 얼굴 특징 파악
# 1. 손 행동 인식 
# 1. 포즈 인식
# 1. box tracking
# 1. 머리카락 변환

# In[2]:


# pip install --user mediapipe 로 패키지 설치

import mediapipe as mp

# 문제가 없어야 잘 설치된 것임.


# In[7]:


import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('face_video.mp4') 
# 매개변수가 0이면 웹캠, 파일에서 가져올 것이므로 파일 이름을 적음. 

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    
      while cap.isOpened():
          success, image = cap.read()
        
          if not success:
                break
                
          image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
          image.flags.writeable = False
            
          results = face_detection.process(image)

          image.flags.writeable = True
          image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
          if results.detections:
              for detection in results.detections:
                  mp_drawing.draw_detection(image, detection)
                    
          cv2.imshow('Face Detection',cv2.resize(image,None,fx=0.5,fy=0.5)) # 사이즈 변환
        
          if cv2.waitKey(1) == ord('q'):
              break
            
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)


# ## 커널이 죽은 경우 kernel 에서 restart 하면 됩니다.
