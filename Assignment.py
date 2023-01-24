# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:08:37 2023

@author: DELL
"""


import numpy as np
import cv2
import time

time_y = []
time_o = []
time_g = []
time_w = []
quad_y = []
quad_o = []
quad_g = []
quad_w = []
ball_y = [0]
ball_o = [0]
ball_g = [0]
ball_w = [0]

size = (1920, 1080)
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

quadrant = 0
f = open("solution.txt", "w")
color = ["Yellow","Orange","Green","White"]
start = time.time()
videoCapture = cv2.VideoCapture("video.mp4")

while(videoCapture.isOpened()):
    
    success,frame = videoCapture.read()
    
    if success == True:
        
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Resized_Window", 1920, 1080)
        
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.GaussianBlur(grayFrame, (17, 17), 0)
        #dp=1.4 --> circles that are closer to each other are merged
        #min_dist=90 --> min dist between two possible circles
        # param1=45 --> sensitivity (too high not enough circle and vice versa)
        # param 2=35 --> accuracy of circle detection (no. of edge points required)
        circles = cv2.HoughCircles(blurFrame,cv2.HOUGH_GRADIENT,1.4,90,
                                   param1=45, param2=35,minRadius=40,maxRadius=100)
        
        if circles is not None:
            
            # convert to numpy array
            circles = np.uint16(np.around(circles))
            
            #Loop over all found circles
            for pt in circles [ 0, :]:
                x,y,rad = pt[0], pt[1], pt[2]            
                cv2.circle(frame, (x, y), rad, (0, 255, 0), 4)
                b,g,r = frame[y, x]
                rgb = r,g,b
                timestamp = videoCapture.get(cv2.CAP_PROP_POS_MSEC)
                
                # YELLOW colour
                if r<160 and r>110 and g>104 and g<128 and b>39 and b<45 :
                    if ball_y[-1]==0:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            quadrant = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            quadrant = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            quadrant = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            quadrant = 4
                        quad_y.append(quadrant)
                        
                        ball_y.append(1)
                        time_y.append(int(timestamp))
                        text = ['\n',color[0]," Ball appeares at timestamp: ",str(time_y[0]), " at quadrant: ",str(quad_y[-1]),'\n'] 
                        cv2.putText(frame,color[0],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                                                
                        try:
                            f.writelines(text)
                        except:
                            pass
                    else:
                        cv2.putText(frame,color[0],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        time_y[len(time_y)-1]=int(timestamp)
                
                if ball_y[-1]==1:
                    if int(timestamp)!=time_y[-1] and int(timestamp)-time_y[-1]>1000:
                        ball_y.append(0)
                        time_y.append(int(timestamp))
                        text = ['\n',color[0]," Ball dissapears at timestamp: ",str(time_y[-1]),'\n']
                        
                        try:
                            f.writelines(text)
                        except:
                            pass
                elif len(ball_y)!=1 and ball_y[-1]==0:
                    if int(timestamp)!=time_y[-1]:
                        time_y[len(time_y)-1]=int(timestamp)
                    
                    
                
                # ORANGE colour
                if r<230 and r>210 and g>105 and g<130 and b>80 and b<105:
                    if ball_o[-1]==0:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            quadrant = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            quadrant = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            quadrant = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            quadrant = 4
                        quad_o.append(quadrant)
                        
                        ball_o.append(1)
                        time_o.append(int(timestamp))
                        text = ['\n',color[1]," Ball appeares at timestamp: ",str(time_o[0]), " at quadrant: ",str(quad_o[-1]),'\n'] 
                        cv2.putText(frame,color[1],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                                                
                        try:
                            f.writelines(text)
                        except:
                            pass
                    else:
                        cv2.putText(frame,color[1],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        time_o[len(time_o)-1]=int(timestamp)
                
                if ball_o[-1]==1:
                    if int(timestamp)!=time_o[-1] and int(timestamp)-time_o[-1]>1000:
                        ball_o.append(0)
                        time_o.append(int(timestamp))
                        text = ['\n',color[1]," Ball dissapears at timestamp: ",str(time_o[-1]),'\n']
                        
                        try:
                            f.writelines(text)
                        except:
                            pass
                elif len(ball_o)!=1 and ball_o[-1]==0:
                    if int(timestamp)!=time_o[-1]:
                        time_o[len(time_o)-1]=int(timestamp)
                
                # GREEN color
                if r<55 and r>30 and g>65 and g<90 and b>66 and b<99:
                    if ball_g[-1]==0:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            quadrant = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            quadrant = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            quadrant = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            quadrant = 4
                        quad_g.append(quadrant)
                        
                        ball_g.append(1)
                        time_g.append(int(timestamp))
                        text = ['\n',color[2]," Ball appeares at timestamp: ",str(time_g[0]), " at quadrant: ",str(quad_g[-1]),'\n'] 
                        cv2.putText(frame,color[2],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                                                
                        try:
                            f.writelines(text)
                        except:
                            pass
                    else:
                        cv2.putText(frame,color[2],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        time_g[len(time_g)-1]=int(timestamp)
                
                if ball_g[-1]==1:
                    if int(timestamp)!=time_g[-1] and int(timestamp)-time_g[-1]>1000:
                        ball_g.append(0)
                        time_g.append(int(timestamp))
                        text = ['\n',color[2]," Ball dissapears at timestamp: ",str(time_g[-1]),'\n']
                        
                        try:
                            f.writelines(text)
                        except:
                            pass
                elif len(ball_g)!=1 and ball_g[-1]==0:
                    if int(timestamp)!=time_g[-1]:
                        time_g[len(time_g)-1]=int(timestamp)
                
                # WHITE color
                if r<190 and r>160 and g>180 and g<190 and b>140 and b<170:
                    if ball_w[-1]==0:
                        if pt[0]>1252 and pt[0]<1735 and pt[1]>543 and pt[1]<1011:
                            quadrant = 1
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>543 and pt[1]<1010:
                            quadrant = 2
                        elif pt[0]>786 and pt[0]<1217 and pt[1]>24 and pt[1] <507:
                            quadrant = 3
                        elif pt[0]>1252 and pt[0]<1735 and pt[1]>24 and pt[1]<507:
                            quadrant = 4
                        quad_w.append(quadrant)
                        
                        ball_w.append(1)
                        time_w.append(int(timestamp))
                        text = ['\n',color[3]," Ball appeares at timestamp: ",str(time_w[0]), " at quadrant: ",str(quad_w[-1]),'\n'] 
                        cv2.putText(frame,color[3],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        
                        try:
                            f.writelines(text)
                        except:
                            pass
                    else:
                        cv2.putText(frame,color[3],(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                        time_w[len(time_w)-1]=int(timestamp)
                
                if ball_w[-1]==1:
                    if int(timestamp)!=time_w[-1] and int(timestamp)-time_w[-1]>1000:
                        ball_w.append(0)
                        time_w.append(int(timestamp))
                        text = ['\n',color[3]," Ball dissapears at timestamp: ",str(time_w[-1]),'\n']
                        
                        try:
                            f.writelines(text)
                        except:
                            pass
                elif len(ball_w)!=1 and ball_w[-1]==0:
                    if int(timestamp)!=time_w[-1]:
                        time_w[len(time_w)-1]=int(timestamp)          


        result.write(frame)
        cv2.imshow('Resized_Window',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
videoCapture.release()
cv2.destroyAllWindows()