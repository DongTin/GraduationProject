import matplotlib.pyplot as plt


# loss率以及accuracy率可视化

def show(accuracy_history):
    plt.plot(accuracy_history)
    plt.ylabel("Accuracy")
    # 0, 5 x轴下标 0, 1 y轴下标
    plt.axis([0, len(accuracy_history) - 1, 0, 1])
    # plt.savefig('accuracy', dpi=600)
    plt.legend(["Accuracy"])
    plt.grid()
    plt.show()
