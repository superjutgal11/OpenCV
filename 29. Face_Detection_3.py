#!/usr/bin/env python
# coding: utf-8

# # 직접 만든 그림을 덮어 씌우기
# 
# 맥북이라 그림판 사용에 제한이 있어서 설명을 작성  
# 
# 1. 그림판에 크기 조정을 하고(100x100 픽셀) 왼쪽 귀, 오른쪽 귀 그리기  
# 1. 그림판에 크기 조정을 하고(300x100 픽셀) 코 그리기  

# In[1]:


import cv2 # 라이브러리 설치
import mediapipe as mp # 미디어파이프 설치

# 얼굴을 찾고 찾은 얼굴에 표시를 위한 변수를 정의
mp_face_detection = mp.solutions.face_detection # 얼굴검출을 위한 face_detection 모듈을 사용
mp_drawing = mp.solutions.drawing_utils # 얼굴의 특징을 그리기 위한 drawing_utils 모듈을 사용

# 동영상 파일 열기
cap = cv2.VideoCapture('face_video.mp4') 

# 이 부분에서 위에서 그린 이미지를 불러온다.
image_right_eye = cv2.imread('right_eye.png') # 100x100
image_left_eye = cv2.imread('left_eye.png') # 100x100
image_nose = cv2.imread('nose.png') # 300x100 (가로,세로)

# 객체 생성 후 실행, 이후 자동 자원 해제
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.7) as face_detection:
    # model_selection은 0또는 1 가능, 0은 1~2m내의 가까운 거리에서 사용하기 적합하고 1은 5m이내에 적합함.
    # min_detection_confidence는 신뢰도 몇%이상이여야 얼굴로 인식될지를 의미함. 0.7는 70%를 의미함.
    
    while cap.isOpened(): # 영상 열렸는지 확인 코드
        success, image = cap.read() 
        
        if not success:       
            break
          
        # 하단은 성능향상을 위한 코드블럭
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB) # 얼굴검출 후 반환
        image.flags.writeable = False
        results = face_detection.process(image) 

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
        
        if results.detections: # 검출된 얼굴이 있다면
            for detection in results.detections: # 검출된 사람 얼굴만큼
                # mp_drawing.draw_detection(image, detection) 얼굴을 바운딩 박스로 둘러싸는 코드입니다.
                  # print(detection) # 검출된 얼굴의 속성을 출력하는 코든데 우선 주석처리함.
                  # 6개 특징을 뽑는데 오른쪽 눈, 왼쪽 눈, 코 끝부분, 입 중심, 오른쪽 귀, 왼쪽 귀(정확히는 귀구슬점,이주 부분)
                    
                  # 특정 위치를 가져오도록 해 보자
                keypoints = detection.location_data.relative_keypoints # 각각 인덱스에 특징 위치를 가지고 있음.
                right_eye = keypoints[0] # 오른쪽 눈
                left_eye = keypoints[1] # 왼쪽 눈
                  # 각각 눈의 xy 좌표를 각각 변수에 할당함. 이 눈 위치에 동그라미를 그리려 한다.   
                nose_tip = keypoints[2] # 코 끝부분
                
                # 이미지의 크기에 따라 xy좌표값의 위치가 크게 다를 수 있기 때문에 이미지 크기 정보를 가지고 좌표계산을 해 보자.
                h , w , _ = image.shape # _는(캐널) 안쓰는 값을 받는 용도로 쓰입니다. 높이와 넓이만 필요한 상황입니다.
                right_eye = (int(right_eye.x * w) , int(right_eye.y*h)) # 튜플 형태로 실제 좌표를 넣음 (x,y)
                left_eye = (int(left_eye.x * w) , int(left_eye.y*h))
                nose_tip = (int(nose_tip.x * w) , int(nose_tip.y*h))
                
                # 각 특징에 이미지를 그리기
                image[right_eye[1]-50:right_eye[1]+50,right_eye[0]-50:right_eye[0]+50] = image_right_eye
                # right_eye는 100x100이고 포인트는 중심지점이기에 상하 좌우 양 50만큼의 범위에 삽입함. (크롭 참고)
                image[left_eye[1]-50:left_eye[1]+50,left_eye[0]-50:left_eye[0]+50] = image_left_eye
                # 좌측 눈도 크기가 같으므로 같은 코드로 작성했습니다.
                
                image[nose[1]-50:nose[1]+50,nose[0]-150:nose[0]+150] = image_nose
                # 가로 픽셀 길이가 300이므로 가로는 중심점부터 150범위로 설정해 두었다.
                
                # 이후 위의 좌표에서 좀 더 자연스럽게 각각의 범위값을 수정해 주자.
                
            cv2.imshow('Face Detection',cv2.resize(image,None,fx=0.5,fy=0.5)) # 사이즈 변환
        
            if cv2.waitKey(1) == ord('q'):
                break
            
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)


# In[ ]:




