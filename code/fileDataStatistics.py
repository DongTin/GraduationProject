import matplotlib.pyplot as plt
import getFileName as gFN

fileData = []
nameList = []

for id in range(1, 44):
    fileName = gFN.getFileName(id)
    count = len(open(fileName, 'r').readlines())
    fileData.append(count)
    nameList.append('File%d' % id)
    print('File%d : %d Rows' % (id, count))

fig = plt.figure(figsize=(20, 10))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.ylabel("数量（条）")
plt.xlabel("文件编号")
plt.title(u"文件数据统计")
p0 = plt.bar(range(len(fileData)), height=fileData, width=0.8, tick_label=nameList, label="数据条数", color="green")
for a, b in zip(range(len(fileData)), fileData):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=30)
plt.legend()
# 存储
# plt.savefig('../picture/fileStatistics0', dpi=1200)
# 网格
# plt.grid()

sum = 0
for i in fileData:
    sum += i

print('Total = %d' % sum)
print("Max = %d" % max(fileData))
print("Average = %d" % (sum / len(fileData)))

fig1 = plt.figure(figsize=(10, 20))
dataList = [sum, max(fileData), min(fileData), (sum / len(fileData))]
nameList2 = ("总数", "最大值", "最小值", "平均值")
plt.ylabel("数量（条）")
plt.title(u"文件数据统计")
p1 = plt.bar([1, 2, 3, 4], height=dataList, width=0.8, tick_label=nameList2, label="数据条数", color="green")
for a, b in zip([1, 2, 3, 4], dataList):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.legend()
# plt.savefig('../picture/fileStatistics1', dpi=1200)

plt.show()
