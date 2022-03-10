import numpy as np
import torch

import conversion as con

# 已知bug：无法跨文件
# 要求：1-43文件中随机选择文件抽取后20%的随机一条累计n条
def getTensorData(dataNum):
    num = 1
    for i in range(1, 44):
        if i < 10:
            fileName = "../datas/phone0%d.txt" % i
        else:
            fileName = "../datas/phone%d.txt" % i
        file0 = open(fileName, 'r')
        data = np.empty([0, 1, 400], float)
        targets = np.empty(0, int)
        for x in file0:
            # dataNum的数据被用做训练集
            if num > dataNum:
                break
            # print('probe request %d : %s' % (num, x[65: -2]))
            # print('list %d : %s' % (num, con.ConversionAndNormalization(x)))
            # print('len : %d' % len(con.ConversionAndNormalization(x)))
            # print('----------------------------------------------------------------')

            # temp1 = np.append(temp1, con.ConversionAndNormalization(x))
            # # print(temp1)
            # # print(temp1.shape)
            # # print(temp1.ndim)
            # # print('----------------------------------------------------------------')
            # temp1 = temp1.reshape(num, 400)
            # print('numpy : \n%s' % temp1)
            # print('numpy.shape : ', end='')
            # print(temp1.shape)
            # print('numpy.ndim : %d' % temp1.ndim)

            # temp0是将list转为numpy再reshape为(1,400) 单个数据
            temp0 = np.empty([0, 0, 400], float)
            temp0 = np.append(temp0, con.ConversionAndNormalization(x))
            temp0 = temp0.reshape((1, 1, 400))

            data = np.concatenate((data, temp0))
            targets = np.append(targets, i)
            data = torch.from_numpy(data)
            targets = torch.from_numpy(targets)
            # print(temp1)
            # print(temp1.shape)
            # print(temp1.ndim)
            # print(temp1.size)
            # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            num += 1
        file0.close()
        # 输出一个step 一个list
        # list中有step个tuple 每个tuple里有两个元素
        # tuple[0]是(1*1*400)的Tenor tuple[1]是标签值的int
        # eg: out[0][0]                 out[0][1]
        return data, targets


# data, targets = getNumpyData(5)
#
# print(data)
# print(data.shape)
# print(targets)
