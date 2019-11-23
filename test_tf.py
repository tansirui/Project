#数据可视化

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import tensorflow as tf


import requests
from bs4 import BeautifulSoup
url = 'www.baidu.com'


inputX = np.random.rand(100)
inputY = np.multiply(3,inputX) + 1
x = tf.placeholder("float32")
# 定义变量
weight = tf.Variable(0.25)
bias = tf.Variable(0.25)


y = tf.multiply(weight,x) + bias
y_ = tf.placeholder("float32")

loss = tf.reduce_sum(tf.pow((y-y_),2))

train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

sess = tf.Session()

init = tf.global_variables_initializer()

sess.run(init)

for _ in range(1000):
    sess.run(train_step,feed_dict={x:inputX,y_:inputY})
    if _%20 == 0:
        print("w的值为：",weight.eval(session=sess),"; bias的值为：",bias.eval(session=sess))



# img = np.mat(np.zeros((300,300)))
# cv.imshow("img",img)
# cv.waitKey(0)








# #冒泡排序法
# import numpy as np
# a = []
# for k in range(20):
#     a.append(np.random.randint(0,100))
#
# print(a)
#
# def bubble(l):
#     for i in range(0,len(l)):
#         for j in range(len(l)-1,i,-1):
#             if l[j]<l[j-1]:
#                 temp = l[j]
#                 l[j]=l[j-1]
#                 l[j-1]=temp
#     return 1
#
# b = bubble(a)
# print(a)















