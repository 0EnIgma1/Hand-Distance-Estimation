import cv2
import cvzone
import mediapipe as mp
#from cvzone.HandTrackingModule import HandDetector
from FindHands import HandDetector 

distance = 50
H = 4.62875

def focal(h,distance,H):
    f = (h * distance) / H
    print(f)
    return f

f = 45 #this is found by facing the hand at 50cm distance and measuring the height of the detectionbox and passing it to the focal function

def distance_find(f,H,h):
    #print(h)
    if h==0:
        return 0
    else:
        d = int((H * f) / h)
        return d

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    ret, img = cap.read()
    hands, img, height, dbox = detector.findHands(img) 
    pixel = height
    h = float(pixel * 0.02645)

    cv2.putText(img,f"{distance_find(f, H, h)} cm", dbox, cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
    cv2.imshow("test",img)
    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break
cv2.destroyAllWindows()
