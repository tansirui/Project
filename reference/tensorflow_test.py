'''
    (versions: 1.2.0rc2, 1.2.0, 1.2.1, 1.3.0rc0, 1.3.0rc1, 1.3.0rc2, 1.3.0, 1.4.0rc0, 1.4.0rc1, 1.4.0, 1.5.0rc0, 1.5.0rc1, 1.5.0, 1.5.1, 
        1.6.0rc0, 1.6.0rc1, 1.6.0, 1.7.0rc0, 1.7.0rc1, 1.7.0, 1.7.1, 1.8.0rc0, 1.8.0rc1, 1.8.0, 1.9.0rc0, 1.9.0rc1, 1.9.0rc2, 1.9.0, 
        1.10.0rc0, 1.10.0rc1, 1.10.0, 1.11.0rc0, 1.11.0rc1, 1.11.0rc2, 1.11.0, 1.12.0rc0, 1.12.0rc1, 1.12.0rc2, 1.12.0, 1.12.2, 1.12.3, 
        1.13.0rc0, 1.13.0rc1, 1.13.0rc2, 1.13.1, 1.13.2, 1.14.0rc0, 1.14.0rc1, 1.14.0, 1.15.0rc0, 1.15.0rc1, 1.15.0rc2, 1.15.0rc3, 1.15.0, 
        2.0.0a0, 2.0.0b0, 2.0.0b1, 2.0.0rc0, 2.0.0rc1, 2.0.0rc2, 2.0.0)

'''


'''
    防止提示 Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2

    # os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
    # os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error 
'''

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error  



import numpy
import tensorflow as tf

print("Hello Python")

raw = tf.constant('Hello TensorFlow')

sess = tf.Session()

with tf.Session() as ss :
    print(sess.run(raw))




# state = tf.Variable()























'''
    信仰，那曾经是多么厚重的力量。那是你无数次想要放弃之时坚持下来的理由。你愿意为她付出青春、热血、甚至献出生命也在所不惜。
    那是光，是电，是暖，是茫茫暗夜里海上的灯塔，立在天边，任他风雨侵蚀，任他天摇地动，也不会倒下。那是最绝望的境遇里始终闪烁的星点希望

'''