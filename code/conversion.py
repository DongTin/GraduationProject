import numpy as np


# 格式转化和归一化
# input:datas数据 output:归一化的400维list[1*400]
def ConversionAndNormalization(inputStr):
    inputStr = inputStr[0: -2]
    temp0 = []
    temp1 = []
    # 格式转化
    for x in range(0, len(inputStr) - 1):
        temp0.append(inputStr[x])
    temp0 = [i for i in temp0 if i != ' ']
    # print(len(temp0))
    bytesSize = 400
    while len(temp0) < bytesSize:
        temp0.append('0')
    while len(temp0) > bytesSize:
        temp0 = temp0[0: bytesSize]
    # 归一化
    for i in range(0, len(temp0)):
        # print(temp0[i: i + 2])
        b = int(temp0[i], 16)
        if b == 15:
            temp1.append(1)
        else:
            b = float(b) / float(16)
            temp1.append(b)
    # inputStr = ''.join(temp0)
    # print(inputStr)
    # print(len(inputStr))

    # print(output)

    return temp1


str0 = "0000 1a00 2f48 0000 3c16 4601 0000 0000 0002 8509 a000 b200 0000 4000 0000 ffff ffff ffff a0cc 2bcd 5df1 ffff " \
       "ffff ffff 0046 0000 0104 0204 0b16 3208 0c12 1824 3048 606c 0301 052d 1aef 111b ffff 0000 0000 0000 0000 0000 " \
       "0000 0000 0000 0000 0000 007f 0800 0008 8001 4000 40dd 1300 904c 0408 bf0c b279 910f faff 0000 faff 0000 dd07 " \
       "0050 f208 0014 00dd 0900 1018 0200 0010 0000 dd1d 0090 4c5c 0201 0a00 0807 010f 0000 0000 0001 0a01 0101 010f " \
       "0000 0000 00 ,4 "


# num = 1
# for i in range(1, 2):
#     if i < 10:
#         fileName = "../datas/phone0%d.txt" % i
#     else:
#         fileName = "../datas/phone%d.txt" % i
#     file0 = open(fileName, 'r')
#     print('file%s' % i)
#     for x in file0:
#         print('probe request %d: %s' % (num, x[65: -2]))
#         ConversionAndNormalization(x)
#         num += 1
#     file0.close()

# print('list: %s' % ConversionAndNormalization(str0))
# print(len(ConversionAndNormalization(str0)))
# print(ConversionAndNormalization(str0))
# print(type(ConversionAndNormalization(str0)))
