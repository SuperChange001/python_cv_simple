import numpy as np
import cv2
import cv
import time
cap = cv2.VideoCapture(1) # 从摄像头中取得视频


# 获取视频播放界面长宽
width = int(320 + 0.5)
height = int(240 + 0.5)

# 定义编码器 创建 VideoWriter 对象
fourcc = cv2.cv.CV_FOURCC(*'mp4v') # Be sure to use the lower case
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
#face_cascade = cv2.CascadeClassifier( '/Users/superchange/Documents/develop/opencv-2.4.13/data/lbpcascades/lbpcascade_frontalface.xml' ) 
#face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-2.4.9/data/lbpcascades/banana.xml' ) 
t_start = time.time()
fps = 0

while(cap.isOpened()):
    #读取帧摄像头
    ret, frame = cap.read()
    if ret == True:
        #输出当前帧
        out.write(frame)

        cimg = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
        img = cv2.medianBlur(cimg,3)

        circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                                    param1=50,param2=30,minRadius=50,maxRadius=100)

        
        circles = np.uint16(np.around(circles,0))

        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

        cv2.namedWindow("ball",0)
        cv2.imshow('detected circles',frame)
        
        #键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

# 释放资源
out.release()
cap.release()
cv2.destroyAllWindows()