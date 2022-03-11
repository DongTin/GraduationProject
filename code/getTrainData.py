from tqdm import tqdm
import numpy as np
import torch
import conversion as con
import getFileName as gFN


# 要求：1-43文件中前80%的全部数据
def getTensorData():
    out = []
    with tqdm(range(1, 44), desc='ReadingTrainDatas ', leave=True, position=0) as t:
        for i in t:
            num = 1
            fileName = gFN.getFileName(i)
            file0 = open(fileName, 'r')
            count = len(open(fileName, 'r').readlines())
            # print('file%s (%d rows) ' % (i, count))
            for x in file0:
                # count数量的数据被用做训练集
                if num > count * 0.8:
                    break
                # print('file %d : =========>' % i)
                # print('probe request %d : %s' % (num, x[65: ]))
                # print('list %d : %s' % (num, con.ConversionAndNormalization(x)))
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
        t.close()
    return out


# tqdm.write("训练集文件读取".center(100 // 2, "-"))
# for step, out in enumerate(outData):
#     print('step:', end='')
#     print(step + 1)
#     # print(out)
