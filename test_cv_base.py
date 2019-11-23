import cv2 as cv
import numpy as np


def access_pixels(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print("width:%s, height:%s, channels:%s"%(width,height,channels))
    #实现像位取反操作
    for row in range(height):
        for col in range(width):
            for ch in range(channels):
                pv = img[row,col,ch]
                img[row,col,ch] = 255 - pv
    cv.imshow("pixels",img)


def inverse(img):
    dst = cv.bitwise_not(img)
    cv.imshow("inverse",dst)

def create_img():

    # #三通道的图像
    # img = np.zeros([400,400,3],np.uint8)
    # #通道 BGR
    # # img[: ,: ,0] = np.ones([400,400])*255
    # img[: ,: ,2] = np.ones([400,400])*255
    # cv.imshow("create_test",img)

    # #单通道图像
    # img = np.zeros([400,400,1],np.uint8)
    # img[: ,: ,0] = np.ones([400,400]) * 125
    # cv.imshow("huidu",img)


    #单通道图像 使用ones灵活处理
    img = np.ones([400,400,1],np.uint8)
    img = img * 225
    cv.imshow("huidu",img)
    cv.imwrite("test_img.jpg",img)



print(cv.__version__)
src = cv.imread("test.jpg")
cv.namedWindow("RAW",cv.WINDOW_AUTOSIZE)
cv.imshow("RAW",src)
# t1 = cv.getTickCount()
# access_pixels(src)
# # create_img()
# t2 = cv.getTickCount()
# print("time:%s s"%((t2-t1)/cv.getTickFrequency()))


t3 = cv.getTickCount()
inverse(src)
t4 = cv.getTickCount()
print("time:%s s"%((t4-t3)/cv.getTickFrequency()))


cv.waitKey(0)

cv.destroyAllWindows()