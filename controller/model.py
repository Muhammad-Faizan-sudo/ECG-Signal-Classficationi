from controller.libraries import *
from tensorflow.keras.layers import Input
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def model(optimizer, loss_fun, classes, X_train, y_train, epochs, batch_size):
    img_width = 500
    img_height = 500

    cnn = Sequential()    
    cnn.add(Conv2D(32, (3, 3), activation="relu", input_shape=(img_width, img_height, 1)))
    cnn.add(MaxPooling2D(pool_size = (2, 2)))
    cnn.add(Conv2D(32, (3, 3), activation="relu", input_shape=(img_width, img_height, 1)))
    cnn.add(MaxPooling2D(pool_size = (2, 2)))
    cnn.add(Conv2D(32, (3, 3), activation="relu", input_shape=(img_width, img_height, 1)))
    cnn.add(MaxPooling2D(pool_size = (2, 2)))
    cnn.add(Conv2D(64, (3, 3), activation="relu", input_shape=(img_width, img_height, 1)))
    cnn.add(MaxPooling2D(pool_size = (2, 2)))
    cnn.add(Conv2D(64, (3, 3), activation="relu", input_shape=(img_width, img_height, 1)))
    cnn.add(MaxPooling2D(pool_size = (2, 2)))
    cnn.add(Flatten())
    cnn.add(Dense(activation = 'relu', units = 128))
    cnn.add(Dense(activation = 'relu', units = 64))
    cnn.add(Dense(activation = 'relu', units = 32))
    cnn.add(Dense(activation = 'relu', units = 16))
    cnn.add(Dense(activation = 'softmax', units = classes))

    cnn.compile(optimizer = optimizer, loss = loss_fun, metrics = ['accuracy'])
    cnn.fit(X_train, y_train, epochs = epochs, batch_size = batch_size)
    return cnn

