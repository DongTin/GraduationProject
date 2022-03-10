import torch
import torch.nn as nn

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
