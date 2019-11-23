import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot_hist(src):

    plt.figure("RAW")
    plt.hist(src.ravel(),256,[0,255])
    plt.show()

def image_hist(src):

    color = ('blue','green','red')
    plt.figure("color")

    for i,color in enumerate(color):
        hist = cv.calcHist([src],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()



print(cv.__version__)
src = cv.imread("dataset/lena.jpg")
print(src.shape)
cv.imshow("RAW",src)

t1 = cv.getTickCount()
# plot_hist(src)
image_hist(src)
t2 = cv.getTickCount()
tim = (t2-t1)/cv.getTickFrequency()

print("time:%s s"%tim)

cv.waitKey(0)
cv.destroyAllWindows()