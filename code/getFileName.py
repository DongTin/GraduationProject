def getFileName(num):
    if num < 10:
        fileName = "../datas/phone0%d.txt" % num
    else:
        fileName = "../datas/phone%d.txt" % num
    return fileName
