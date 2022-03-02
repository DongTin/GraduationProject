import numpy as np
import pylab
import tensorflow as tf
import tensorflow.python.keras as keras
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras import utils
import tensorflow.keras.layers as layers
from tensorflow.keras import utils
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
reshape3to2 = lambda a: a.reshape(a.shape[0], a.shape[1] * a.shape[2])
asfloat = lambda a: a.astype('float32')
normalization = lambda a: a / 255  # RGB的值最大是255
one_hot_result = lambda a: utils.to_categorical(a, 10)
batch_handle_data = lambda a: normalization(asfloat(reshape3to2(a)))
batch_handle_tag = lambda a: one_hot_result(a)

x_train = batch_handle_data(x_train)
x_test = batch_handle_data(x_test)

y_train = batch_handle_tag(y_train)
y_test = batch_handle_tag(y_test)
print(x_train.shape)
print(y_train.shape)


class MNISTCnnOriginal(keras.Model):
    # 定义网络的层结构
    def __init__(self):
        super(MNISTCnnOriginal, self).__init__()
        self.layer1_dense = layers.Dense(1024, activation="relu", name="dense_layer")
        self.layer1_normalization = layers.BatchNormalization(name="normalization")
        self.layer1_dropout = layers.Dropout(0.2)

        self.layer2_dense = layers.Dense(512, kernel_regularizer=keras.regularizers.l2(0.01))
        self.layer2_normalization = layers.BatchNormalization(name="normalization")
        self.layer2_activation = layers.Activation("relu")
        self.layer2_dropout = layers.Dropout(0.2)

        self.layer_output = layers.Dense(10, activation="softmax")

    # 定义网络的前向传播
    def call(self, inputs):
        networks = [
            self.layer1_dense,
            self.layer1_normalization,
            self.layer1_dropout,
            self.layer2_dense,
            self.layer2_normalization,
            self.layer2_activation,
            self.layer2_dropout,
            self.layer_output
        ]
        data = inputs
        for i in networks:
            data = i(data)
        return data


print(x_train.shape)

model = MNISTCnnOriginal()
model(x_train)
# utils.plot_model(model)
model.summary()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(x_train, y_train, epochs=15, batch_size=128, validation_data=(x_test, y_test), verbose=1,
                    validation_split=0.1)

print(x_train.shape)


def show_info(x):
    plt.figure()
    for i in x:
        plt.plot(i[0], label=i[1])
    plt.legend()
    pylab.show()

    show_info([
        [history.history['loss'], "train"],
        [history.history["val_loss"], "val"]
    ])
    show_info([
        [history.history['accuracy'], "acc"]
    ])
