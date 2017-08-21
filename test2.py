import numpy as np
import cv2
import cv
import time
cap = cv2.VideoCapture(0) # 从摄像头中取得视频


# 获取视频播放界面长宽
width = int(320 + 0.5)
height = int(240 + 0.5)

# 定义编码器 创建 VideoWriter 对象
fourcc = cv2.cv.CV_FOURCC(*'mp4v') # Be sure to use the lower case
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
face_cascade = cv2.CascadeClassifier( '/Users/superchange/Documents/develop/opencv-2.4.13/data/lbpcascades/lbpcascade_frontalface.xml' ) 
#face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-2.4.9/data/lbpcascades/banana.xml' ) 
t_start = time.time()
fps = 0

while(cap.isOpened()):
    #读取帧摄像头
    ret, frame = cap.read()
    if ret == True:
        #输出当前帧
        out.write(frame)

        # Use the cascade file we loaded to detect faces
        gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
        faces = face_cascade.detectMultiScale( gray )
        print "Found " + str( len( faces ) ) + " face(s)"

        # Draw a rectangle around every face and move the motor towards the face
        for ( x, y, w, h ) in faces:

            cv2.rectangle( frame, ( x, y ), ( x + w, y + h ), ( 100, 255, 100 ), 2 )
            cv2.putText( frame, "Face No." + str( len( faces ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )




         # Calculate and show the FPS
        fps = fps + 1
        sfps = fps / ( time.time() - t_start )
        cv2.putText( frame, "FPS : " + str( int( sfps ) ), ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )    


        cv2.imshow('My Camera',frame)

        #键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

# 释放资源
out.release()
cap.release()
cv2.destroyAllWindows()