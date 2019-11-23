# -- coding: utf-8 --

import cv2 as cv
import numpy as np

# def extrace_object(img):
def extrace_object():
    # hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    #
    # lower_hsv = np.array([37,43,46])
    # upper_hsv = np.array([77,255,255])
    #
    # #分离出绿色
    # mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
    # cv.imshow("MASK",mask)

    cap = cv.VideoCapture("vtest.avi")
    while(True):
        ret,frame = cap.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])

        #分离出绿色
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        #合并图像
        dst = cv.bitwise_and(frame,frame,mask=mask)

        cv.imshow("RAW",frame)
        cv.imshow("MASK",dst)

        c = cv.waitKey(40)
        if c == 27:
            break


def color_space(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(img,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)


print(cv.__version__)
src = cv.imread("test.jpg")

# cv.namedWindow("RAW",cv.WINDOW_AUTOSIZE)
# cv.imshow("RAW",src)

#裁剪图像
resizeImg = cv.resize(src,(800,800))
cv.imshow("裁剪",resizeImg)

extrace_object()

# #分离成三个通道
# b,g,r = cv.split(resizeImg)
# cv.imshow("B",b)
# cv.imshow("G",g)
# cv.imshow("R",r)
#
# #剔除一个通道的颜色
# resizeImg[:,:,0] = 0
# cv.imshow("删除",resizeImg)
#
# #合并分离通道
# mergeImg = cv.merge([b,g,r])
# cv.imshow("合并",mergeImg)

cv.waitKey(0)
cv.destroyAllWindows()