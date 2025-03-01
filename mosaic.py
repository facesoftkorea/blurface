import cv2
import os

def mosaic_video(input_path, output_path):
    # Haar Cascade를 사용하여 얼굴 검출
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # 동영상 읽기
    video = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 동영상 저장 설정
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # 그레이스케일로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            # 얼굴 영역 모자이크 처리
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (w // 10, h // 10))
            face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = face
        
        out.write(frame)

    video.release()
    out.release()
    #cv2.destroyAllWindows()

    return output_path
