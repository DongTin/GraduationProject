import torch
import torch.nn as nn
import torch.utils.data as data
import getTrainData
import getTestData

EPOCH = 1  # !!!
BATCH_SIZE = 50  # !!!
LR = 0.001  # learning rate !!!


class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.mlp = nn.Sequential(
            # 全连接层的设置
            # 三个全连接层 43个手机所以最后输出结果为43个点
            nn.Linear(1 * 400, 1 * 400),
            nn.Linear(1 * 400, 1 * 400),
            nn.Linear(1 * 400, 43)
        )

    def forward(self, x):
        output = self.mlp(x)
        # return x for visualization
        return output, x


mlp = MLP()
# net architecture
print(mlp)

# 自适应估计的随机目标函数一阶梯度优化算法
optimizer = torch.optim.Adam(mlp.parameters(), lr=LR)  # optimize all logistic parameters
# 构建交叉熵损失函数
loss_func = nn.CrossEntropyLoss()                      # the target label is not one-hotted

train_data = getTrainData.getTensorData(50000)
train_loader = data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
data, targets = getTestData.getTensorData(100)
test_x = torch.unsqueeze(data, dim=1).type(torch.FloatTensor)[:100]
test_y = targets[:100]
# print(test_x)
# print(type(test_x))
# print(test_x.shape)
# print(test_y)

# 导入数据 开始训练
for epoch in range(EPOCH):
    # step:第几个数据 b_x:输入数据  b_y:数据标签
    for step, (b_x, b_y) in enumerate(train_loader):   # gives batch data, normalize x when iterate train_loader
        # print(b_x.size())
        # print(b_x)
        # print(type(b_x))
        b_x = b_x.view(-1, 1*400)
        # print(b_x.size())

        output = mlp(b_x)[0]               # logistic output
        loss = loss_func(output, b_y)   # cross entropy loss
        # 梯度清零
        optimizer.zero_grad()           # clear gradients for this training step
        # 反向传播
        loss.backward()                 # backpropagation, compute gradients
        # https://blog.csdn.net/qq_41468616/article/details/121244698
        # 执行一次优化步骤，通过梯度下降法来更新参数的值
        optimizer.step()                # apply gradients

        if step % 50 == 0:

            test_output, last_layer = mlp(test_x.view(-1, 1*400))
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_y.data.numpy()).astype(int).sum()) / float(test_y.size(0))
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)
            # if HAS_SK:
            #     # Visualization of trained flatten layer (T-SNE)
            #     tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
            #     plot_only = 500
            #     low_dim_embs = tsne.fit_transform(last_layer.data.numpy()[:plot_only, :])
            #     labels = test_y.numpy()[:plot_only]
            #     plot_with_labels(low_dim_embs, labels)
# plt.ioff()

# print 10 predictions from test data
test_output, _ = mlp(test_x[:10].view(-1, 1*400))
pred_y = torch.max(test_output, 1)[1].data.numpy()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')
