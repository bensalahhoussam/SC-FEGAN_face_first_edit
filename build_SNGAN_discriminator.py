import tensorflow as tf
from keras.layers import Conv2D,LeakyReLU,Input
from keras.models import Model
from sn import SpectralNormalization

def dis_conv(x):
    x = SpectralNormalization(Conv2D(64*1, (3, 3),strides=2, activation=LeakyReLU(alpha=0.1)))(x)
    x = SpectralNormalization(Conv2D(64*2, (3, 3), strides=2,activation=LeakyReLU(alpha=0.1) ))(x)
    x = SpectralNormalization(Conv2D(64*4, (3, 3), strides=2,activation=LeakyReLU(alpha=0.1) ))(x)
    x = SpectralNormalization(Conv2D(64*4, (3, 3), strides=2,activation=LeakyReLU(alpha=0.1)))(x)
    x = SpectralNormalization(Conv2D(64*4, (3, 3),strides=2, activation=LeakyReLU(alpha=0.1)))(x)
    x = SpectralNormalization(Conv2D(64*4, (3, 3), strides=2,activation=LeakyReLU(alpha=0.1)))(x)
    return x
inputs = Input(shape=(512,512,5))
output=dis_conv(inputs)
SNGAN_discriminato_model=Model(inputs=inputs,outputs=output)
print(SNGAN_discriminato_model.summary())
