import cv2
import mediapipe
import cvzone
from FindHands import HandDetector

lst = []
distance = 30
H = 60.715
f = 30

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(detectionCon = 0.7, maxHands = 1)

def focal(h,distance,H):
    f = (h * distance) / H
    print(f)
    return f

def distance_find(f,H,h):
    #print(h)
    if h==0:
        return 0
    else:
        d = int(1.1 *((H * f) / h))
        return d

while True:
    ret, img = cap.read()
    hands, img, height, dbox = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    
    
    if hands:
        hand = hands[0]
        
        if len(lmlist)!=0:
            x0, y0 = lmlist[0][1:] #point 0 position
            x1, y1 = lmlist[1][1:] #point 1 position
            x17, y17 = lmlist[17][1:] #point 17 position

            #print(f"Point 0 Location in pixel : {[x0,y0]}") 
 
            length, info, img = detector.findDistance(img = img,p1 = (x0,y0),p2 = (x1,y1))
            cv2.putText(img,f"{distance_find(f, H, length)} cm", dbox, cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

    cv2.imshow("frame", img)
    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break
#print(int(sum(lst) / len(lst)))
cv2.destroyAllWindows()