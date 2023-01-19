# Hand-Distance-Estimation

This program will help to estimate the distance of hand from webcam.

Two methods were followed to estimate the distance
>- Bounding box method
>- Index position method

## Bounding box method

>- dist_bbox.py

Bounding box method uses the hand's bounding box width and height. Converts the pixel values into centimeter(cm).

>- Prone to errors due to hand angles.

## Index Position method

>- dist_fp.py


Index postion methods finds the distance between Index 0 and Index 1 in mediapipe hand index landmarks and converts the value into centimeter(cm).

The distance between Indices were found using hypot() function

The hypot() method returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given.


Both methods have an error or 1-2 cm.

