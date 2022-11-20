import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt
import PIL
from PIL import Image
(train_images,train_labels),(test_images,test_labels) = mnist.load_data()
train_images.shape
len(train_labels)
train_labels
test_images.shape
len(test_labels)
test_labels
#導入MNIST數據集

'''plt.imshow(train_images[819], cmap=plt.get_cmap('gray'))
print(train_images[819])
print(train_labels[819])'''
#運用熱點圖查看MNIST數據集

from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))
#構建網絡（含有兩個dense層）

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
#編譯網絡

train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32')/255
test_images = test_images.reshape((10000,28*28))
test_images = test_images.astype('float32')/255

from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images,train_labels,epochs=5,batch_size=128)
#訓練循環

test_loss , test_acc = network.evaluate(test_images,test_labels)
print('test_acc:',test_acc)
#輸出精度
network.save('m_lenet.h5')