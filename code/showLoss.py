import matplotlib.pyplot as plt


# loss率以及accuracy率可视化

def show(loss_history):
    plt.plot(loss_history)
    plt.xlabel("EpochsNumber")
    plt.ylabel("Loss")
    # 0, 5 x轴下标 0, 1 y轴下标
    plt.axis([0, len(loss_history) - 1, 0, max(loss_history)])
    # plt.savefig('accuracy', dpi=600)
    plt.legend(["Loss"])
    plt.grid()
    plt.show()
