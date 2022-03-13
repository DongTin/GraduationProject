import torch
import torch.nn as nn
import torch.utils.data as data
from tqdm import tqdm
import getTrainData
import getTestData
import showLoss
import showAccuracy
import time

EPOCH = 15  # !!!
BATCH_SIZE = 50  # !!!
LR = 0.001  # learning rate !!!
TestDatasNum = 500


class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.mlp = nn.Sequential(
            # 全连接层的设置
            # 三个全连接层 43个手机所以最后输出结果为43个点
            nn.Linear(1 * 400, 1 * 256),
            # 为了防止过拟合添加dropout层
            nn.Dropout(0.3),
            nn.Linear(1 * 256, 1 * 128),
            nn.Dropout(0.3),
            nn.Linear(1 * 128, 44)
        )

    def forward(self, x):
        outputs = self.mlp(x)
        # return x for visualization
        return outputs, x


start = time.time()
mlp = MLP()
# net architecture
print(mlp)

# 自适应估计的随机目标函数一阶梯度优化算法 选择优化器
optimizer = torch.optim.Adam(mlp.parameters(), lr=LR)  # optimize all logistic parameters
# 设置学习率下降策略
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
# 构建交叉熵损失函数
loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted

tqdm.write("训练集文件读取".center(100 // 2, "-"))
train_data = getTrainData.getAllData()
train_loader = data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
tqdm.write("读取完成".center(100 // 2, "-") + '\n')
tqdm.write("测试集文件读取".center(100 // 2, "-"))
data, targets = getTestData.getRandomData(TestDatasNum)
test_x = torch.unsqueeze(data, dim=1).type(torch.FloatTensor)[:TestDatasNum]
test_y = targets[:TestDatasNum]
tqdm.write("读取完成".center(100 // 2, "-") + '\n')

loss_history = []
accuracy_history = []
# 导入数据 开始训练
for epoch in range(EPOCH):
    # step:第几个数据 b_x:输入数据  b_y:数据标签
    for step, (b_x, b_y) in enumerate(train_loader):  # gives batch data, normalize x when iterate train_loader
        b_x = b_x.view(-1, 1 * 400)

        output = mlp(b_x)[0]  # logistic output
        loss = loss_func(output, b_y)  # cross entropy loss
        # 梯度清零
        optimizer.zero_grad()  # clear gradients for this training step
        # 反向传播
        loss.backward()  # backpropagation, compute gradients
        # https://blog.csdn.net/qq_41468616/article/details/121244698
        # 执行一次优化步骤，通过梯度下降法来更新参数的值
        optimizer.step()  # apply gradients

        if step % 50 == 0:
            test_output, last_layer = mlp(test_x.view(-1, 1 * 400))
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_y.data.numpy()).astype(int).sum()) / float(test_y.size(0))
            if step % 2000 == 0:
                loss_history.append(loss.data.numpy())
                accuracy_history.append(accuracy)
            print('Epoch: ', epoch + 1, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)
    scheduler.step()


test_output, _ = mlp(test_x[:10].view(-1, 1 * 400))
pred_y = torch.max(test_output, 1)[1].data.numpy()
print('prediction phone : ', pred_y)
print('real phone       : ', test_y[:10].numpy())
showLoss.show(loss_history)
showAccuracy.show(accuracy_history)
end = time.time()
print("运行时间:%.2f秒" % (end - start))
