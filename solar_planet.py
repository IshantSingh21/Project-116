import cv2
img = cv2.imread('C:/Users/MICROSOFT/OneDrive/Desktop/Python/Project 116/solar-system.jpg')
cv2.putText(img,
"Sun",
 (20,300),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )

cv2.putText(img,
"Mercury",
 (110,250),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Venus",
 (190,260),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Earth",
 (285,270),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Mars",
 (380,260),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Jupiter",
 (580,395),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Saturn",
 (780,305),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Uranus",
 (968,305),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.putText(img,
"Neptune",
 (1109,305),
   cv2.FONT_HERSHEY_TRIPLEX,
     0.5,
       (255,255,255) )
cv2.imshow('Solar System!', img)
cv2.waitKey(0)