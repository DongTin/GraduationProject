phoneMac = []
for i in range(1,3):
    fileName = "../datas/phone0%d.txt"%i
    file0 = open(fileName, 'r')
    print('file%s'%i)
    for i in file0:
        # phoneMac.append(i[0: -4])
        print("%s:%s:%s:%s:%s:%s" % (i[90: 92], i[92: 94], i[95: 97], i[97: 99], i[100: 102], i[102: 104]))

# for i in phoneMac:
#     print("%s:%s:%s:%s:%s:%s"%(i[90: 92], i[92: 94],i[95: 97], i[97: 99], i[100: 102],i[102: 104]))