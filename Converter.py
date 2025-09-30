import sys
!{sys.executable} -m pip install opencv-python

import cv2 as cv

path = r"C:\Users\yigit\Downloads\dog.jpg"

picture = cv.imread(path)

blackandwhite = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)

cv.imshow("picture1", picture)
cv.waitKey(0)

cv.imshow("picture2", blackandwhite)
cv.waitKey(0)

cv.destroyAllWindows()
