import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
from PIL import Image

model = load_model('m_lenet.h5')

def pre_pic(picName):
    # 先打開傳入的原始圖片
    img = Image.open(picName)
    # 使用消除鋸齒的方法resize圖片
    reIm = img.resize((28,28),Image.ANTIALIAS)
    # 變成灰度圖，轉換成矩陣
    im_arr = np.array(reIm.convert("L"))
    return im_arr

im1 = pre_pic('9.jpg')
print('輸入數字：')

plt.imshow(im1,cmap=plt.get_cmap('gray'))
plt.show
#hello

im1 = im1.reshape((1,28*28))
im1 = im1.astype('float32')/255


predict = model.predict(im1)
predict=np.argmax(predict,axis=1)
print ('識別爲：')
print (predict)