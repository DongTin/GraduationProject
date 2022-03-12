import random
import torch
import conversion as con
from tqdm import tqdm
import numpy as np
import getFileName as gFN


# 要求：1-43文件中随机选择文件抽取后20%的随机一条累计n条
def getRandomData(dataNum):
    data = np.empty([0, 1, 400], float)
    targets = np.empty(0, int)
    with tqdm(range(0, dataNum), desc='ReadingTestDatas ', leave=True, position=0) as t:
        for num in t:
            rowNum = 1
            fileNum = random.randint(1, 43)
            fileName = gFN.getFileName(fileNum)
            count = len(open(fileName, 'r').readlines())
            file = open(fileName, 'r')
            fileRow = random.randint(int(count * 0.8), count - 1)

            for rowData in file:
                if rowNum == fileRow:
                    temp0 = np.empty([0, 0, 400], float)
                    temp0 = np.append(temp0, con.ConversionAndNormalization(rowData))
                    temp0 = temp0.reshape((1, 1, 400))

                    data = np.concatenate((data, temp0))
                    targets = np.append(targets, fileNum)
                    data = torch.from_numpy(data)
                    data = data.to(torch.float32)
                    targets = torch.from_numpy(targets)

                rowNum += 1
            file.close()
    t.close()
    return data, targets

# tqdm.write("测试集文件读取".center(100 // 2, "-"))
# data, targets = getTensorData(5)
# print(data)
# print(data.shape)
# print(targets)
# print(targets.shape)
