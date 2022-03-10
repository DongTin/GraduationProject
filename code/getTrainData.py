import numpy as np
import torch

import conversion as con

# 要求：1-43文件中前50%的全部数据
def getTensorData(dataNum):
    num = 1
    out = []
    for i in range(1, 44):
        if i < 10:
            fileName = "../datas/phone0%d.txt" % i
        else:
            fileName = "../datas/phone%d.txt" % i
        file0 = open(fileName, 'r')
        # count = len(open(fileName, 'r').readlines())
        # print('file%s (%d rows) ' % (i, count))
        temp1 = np.empty([0, 1, 400], float)
        for x in file0:
            # dataNum的数据被用做训练集
            if num > dataNum:
                break
            # print('probe request %d : %s' % (num, x[65: -2]))
            # print('list %d : %s' % (num, con.ConversionAndNormalization(x)))
            # print('len : %d' % len(con.ConversionAndNormalization(x)))
            # print('----------------------------------------------------------------')

            # temp0是将list转为numpy再reshape为(1,400) 单个数据
            temp0 = np.empty([0, 0, 400], float)
            temp0 = np.append(temp0, con.ConversionAndNormalization(x))
            temp0 = temp0.reshape((1, 1, 400))
            temp2 = torch.from_numpy(temp0)
            temp2 = temp2.to(torch.float32)
            out.append((temp2, i))
            num += 1
        file0.close()
        # 输出一个list
        # list中有step个tuple 每个tuple里有两个元素
        # tuple[0]是(1*1*400)的Tenor tuple[1]是标签值的int
        # eg: out[0][0]                 out[0][1]
    return out


# outData = getNumpyData(4000)
# for step, out in enumerate(outData):
#     print('step:')
#     print(step + 1)
#     print(out[1])
