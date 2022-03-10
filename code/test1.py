import numpy as np

import conversion as con


def getNumpyData():
    num = 1
    tag = []
    for i in range(1, 2):
        if i < 10:
            fileName = "../datas/phone0%d.txt" % i
        else:
            fileName = "../datas/phone%d.txt" % i
        file0 = open(fileName, 'r')
        count = len(open(fileName, 'r').readlines())
        print('file%s (%d rows) ' % (i, count))
        temp1 = np.empty([0, 1, 400], float)
        for x in file0:
            # 70%的数据被用做训练集
            if num > 5:
                break
            print('probe request %d : %s' % (num, x[65: -2]))
            print('list %d : %s' % (num, con.ConversionAndNormalization(x)))
            print('len : %d' % len(con.ConversionAndNormalization(x)))
            print('----------------------------------------------------------------')

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

            # temp0是将list转为numpy再reshape为(1,400)
            temp0 = np.empty([0, 0, 400], float)
            temp0 = np.append(temp0, con.ConversionAndNormalization(x))
            temp0 = temp0.reshape((1, 1, 400))
            # print(temp0)
            # print(temp0.shape)
            # print(temp0.ndim)
            # print('-------------------------------------------------------')

            # 将temp0连接到temp1上
            # 先将temp0 reshape整理格式，免去了temp1 reshape的过程，保证数据不出差错
            temp1 = np.concatenate((temp1, temp0))
            # print(temp1)
            # print(temp1.shape)
            # print(temp1.ndim)
            # print(temp1.size)
            # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            num += 1
            tag.append(i)
        file0.close()
        return temp1, tag


test_x, test_y = getNumpyData()
for x in enumerate(getNumpyData()):
    print('x:')
    print(x)
