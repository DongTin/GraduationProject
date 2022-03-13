MacModels = []

for n in range(1, 44):
    if n < 10:
        fileName = "../datas/phone0%d.txt" % n
    else:
        fileName = "../datas/phone%d.txt" % n
    file0 = open(fileName, 'r')
    num = 0

    phoneMac = []
    for i in file0:
        phoneMac.append(i[0: -4])

    MacModel = phoneMac[0]

    # print(len(phoneMac))
    # print(len(phoneMac[0]))

    for x in range(0, len(phoneMac) - 1):
        for i in range(0, len(phoneMac[0]), 5):
            if phoneMac[x][i: i + 4] == phoneMac[x + 1][i: i + 4]:
                temp0 = list(phoneMac[x])
                temp0[i: i + 4] = "____"
                phoneMac[x] = ''.join(temp0)

                # temp1 = list(MacModel)
                # if temp1[i: i + 4] == "XXXX":
                #     continue
                # else:
                #     temp1[i: i + 4] = "____"
                # MacModel = ''.join(temp1)
            else:
                temp1 = list(MacModel)
                temp1[i: i + 4] = "XXXX"
                MacModel = ''.join(temp1)

    MacModels.append(MacModel)
    # print('\n' + MacModel)
    file0.close()

with open("../data/MacModels.txt", "w") as f:
    nxx = 1
    for i in MacModels:
        print('MacModel%02d: %s' % (nxx, i))
        nxx += 1
        f.write(i)
        f.write('\n')

    # for i in range(0, len(phoneMac[0]), 5):
    #     temp1 = list(MacModel)
    #     if ''.join(temp1[i: i + 4]) == 'XXXX':
    #         continue
    #     else:
    #         temp1[i: i + 4] = "____"
    #     MacModel = ''.join(temp1)
    # print('\n' + MacModel)