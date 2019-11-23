import cv2 as cv

def add_pixels(img1,img2):
    dst = cv.add(img1,img2)
    cv.imshow("Add_Img",dst)


def subtract_pixels(img1,img2):
    dst = cv.subtract(img2,img1)
    cv.imshow("Subtract_Img",dst)

def multipy_pixels(img1,img2):
    dst = cv.multiply(img2,img1)
    cv.imshow("Multipy_Img",dst)


def logic_pixels(img1,img2):


    not_dst = cv.bitwise_not(img1,img2)
    cv.imshow("not",not_dst)

    or_dst = cv.bitwise_or(img2,img1)
    cv.imshow("or",or_dst)

    and_dst = cv.bitwise_and(img2,img1)
    cv.imshow("and",and_dst)






#算图像均值cv.mean()
#通过算均值和方差确认图像内容是否有较大差异，从而确认信息量如何

print(cv.__version__)

img1 = cv.imread("WindowsLogo.jpg")
img2 = cv.imread("LinuxLogo.jpg")


#打印大小
print(img1.shape)
print(img2.shape)

cv.imshow("Windows",img1)
cv.imshow("Linux",img2)

add_pixels(img1,img2)
subtract_pixels(img1,img2)
multipy_pixels(img1,img2)
logic_pixels(img1,img2)

cv.waitKey(0)
cv.destroyAllWindows()