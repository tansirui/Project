import cv2 as cv
import numpy as np



def filter(img):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    dst = cv.filter2D(img,-1,kernel=kernel)
    cv.imshow("Filter",dst)


img = cv.imread("lena.jpg")

cv.imshow("RAW",img)

filter(img)


cv.waitKey(0)
cv.destroyAllWindows()