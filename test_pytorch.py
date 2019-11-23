# 加载准备数据

import numpy as np
import matplotlib.pyplot as plt

import torch
from torch.autograd import Variable

from torch.utils.data import DataLoader
import torchvision.datasets as dsets
import torchvision.transforms as transforms

batch_size = 100

#下载训练集、数据集数据
train_dataset = dsets.MNIST(root = 'pymnist',
                            train = True,
                            transform = transforms.ToTensor(),
                            download = False
                            )

test_dataset = dsets.MNIST(root = 'pymnist',
                           train = False,
                           transform = transforms.ToTensor(),
                           download = False
                           )




#加载数据
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)


#打印数据集
print("train_data:",train_dataset.train_data.size())
print("train_labels:",train_dataset.train_labels.size())


print("test_data:",test_dataset.test_data.size())
print("test_labels:",test_dataset.test_labels.size())


print("批次的尺寸:",train_loader.batch_size)
print("load_train_data:",train_loader.dataset.train_data.shape)
print("load_train_labels:",train_loader.dataset.train_labels.shape)


# 搭建网络

import torch.nn as nn
import torch


#这是测试行

#mnist像素为28*28
input_size = 784
hiden_size = 500
#输出10个类别
num_classes = 10

class Neural_net(nn.Module):
    def __init__(self,input_num,hidden_size,output):
        super(Neural_net,self).__init__()
        self.layer1 = nn.Linear(input_num,hidden_size)
        self.layer2 = nn.Linear(hiden_size,output)


    def forward(self, x):
        out = self.layer1(x)
        out = torch.relu(out)
        out = self.layer2(out)
        return out


net = Neural_net(input_size,hiden_size,num_classes)
print(net)



## 训练
from torch.autograd import Variable
import torch.nn as nn
import torch
import numpy as np

learning_rate = 1e-1
num_epoches = 5

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(),lr=learning_rate)

for epoch in range(num_epoches):
    print("current epoch = %d " %epoch)

    for i, (images,labels) in enumerate(train_loader):#利用enumerate取出一个可迭代对象的内容

        images = Variable(images.view(-1,28*28))
        labels = Variable(labels)

        outputs = net(images)

        loss = criterion(outputs,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if i % 100 == 0:
            print("current loss = %.5f" % loss.item())

print("finished training")











# tensor = torch.linspace(-6,6,200)
# tensor = Variable(tensor)
# np_data = tensor.numpy()
#
# y_relu = torch.relu(tensor).data.numpy()
#
#
#
# plt.figure(1,figsize=(8,6))
# # plt.subplot(221)
# plt.plot(np_data,y_relu,c = 'red',label = 'relu')
# plt.legend(loc='best')
# plt.show()




# np_data = np.arange(8).reshape((2,4))
# torch_data = torch.from_numpy(np_data)
# print(np_data)
# print(torch_data)
# np_data2 = torch_data.numpy()
# print(np_data2)