import cv2
import numpy as np
import speech_recognition as sr
import pyttsx3 as p
import time

def speak(str):
    engine =p.init()
    engine.say(str)
    engine.runAndWait()
    time.sleep(1)

video = cv2.VideoCapture("test3.mp4")
flag=0
while True:
	ret, orig_frame = video.read()
	if not ret:
		video = cv2.VideoCapture("test3.mp4")
		continue
	if(flag!=20):
		flag+=1
		continue
	flag=0
	frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	low_yellow = np.array([18, 94, 140])
	up_yellow = np.array([48, 255, 255])
	mask = cv2.inRange(hsv, low_yellow, up_yellow)
	edges = cv2.Canny(mask, 50, 150)
	#print(cv2.HOUGH_PROBABILISTIC)
	
	lines = cv2.HoughLinesP(edges, 1, (np.pi)/180, 100, maxLineGap=50)
	if lines is not None:
		line = lines[0]
		x1, y1, x2, y2 = line[0]
		cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
		vari=((y2-y1)/(x2-x1))
			
		if(vari<-0.5):
			speak("straight")

			  
			continue

		speak("right")
			


	cv2.imshow("frame", frame)
	cv2.imshow("edges", edges)

	key = cv2.waitKey(25)
	if key == 27:
		break
video.release()
cv2.destroyAllWindows()