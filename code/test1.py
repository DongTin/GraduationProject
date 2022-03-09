phoneMac = []
for i in range(1,3):
    fileName = "../datas/phone0%d.txt"%i
    file0 = open(fileName, 'r')
    print('file%s'%i)
    for i in file0:
        print(type(i))
        print(i)
        # phoneMac.append(i[0: -4])
        # print("%s:%s:%s:%s:%s:%s" % (i[90: 92], i[92: 94], i[95: 97], i[97: 99], i[100: 102], i[102: 104]))

# for i in phoneMac:
#     print("%s:%s:%s:%s:%s:%s"%(i[90: 92], i[92: 94],i[95: 97], i[97: 99], i[100: 102],i[102: 104]))


# 0000 1a00 2f48 0000 XXXX XXXX 0000 0000 0002 8509 a000 XXXX 0000
#                     Mac       timestamp                antenna signal