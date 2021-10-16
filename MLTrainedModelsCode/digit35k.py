import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

#To import matlab format dataset
from scipy import io as spio
from scipy.io import loadmat
emnist = spio.loadmat("matlab/emnist-digits.mat")

# load training dataset
X_train = emnist["dataset"][0][0][0][0][0][0]
X_train = X_train.astype(np.float32)
y_train = emnist["dataset"][0][0][0][0][0][1]

# load test dataset
X_test = emnist["dataset"][0][0][1][0][0][0]
X_test = X_test.astype(np.float32)
y_test = emnist["dataset"][0][0][1][0][0][1]

print(X_train.shape)
print(y_train.shape)

#Normalize the features (preprocessing phase)
X_train/=255
X_test/=255

# reshape (image of 28*28) (preprocessing phase)
X_train = X_train.reshape(X_train.shape[0], 28, 28,1, order="A")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1,order="A")
print(X_train.shape)
print(X_test.shape)

# one hot encode
number_of_classes = 10
y_train = np_utils.to_categorical(y_train, number_of_classes)
y_test = np_utils.to_categorical(y_test, number_of_classes)
print(y_train.shape)
print(y_test.shape)

# create model
model = Sequential()
model.add(Conv2D(32, (5, 5), input_shape=(X_train.shape[1], X_train.shape[2], 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(number_of_classes, activation='softmax'))


# Compile model
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200)

# Save the model
model.save('digits_new.h5')

# Final evaluation of the model
metrics = model.evaluate(X_test, y_test, verbose=0)
print("Metrics(Test loss & Test Accuracy): ")
print(metrics) 


#delete from  dataset
'''
i=0
for y in y_train:
  if y[0]==0:
    y_train=np.delete(y_train,i,axis=0)
    X_train=np.delete(X_train,i,axis=0)
  else:
    y_train[i][0]=y[0]-1
    i+=1
  print(i) 
i=0
for y in y_test:
  if y[0]==0:
    y_test=np.delete(y_test,i,axis=0)
    X_test=np.delete(X_test,i,axis=0)
  else:
    y_test[i][0]=y[0]-1
    i+=1
 ''' 

#Data Augmentation (preprocessing phase)
'''
from keras.preprocessing.image import ImageDataGenerator
batch_size = 512
gen = ImageDataGenerator(rotation_range=12, width_shift_range=0.1, shear_range=0.3,
                        height_shift_range=0.1, zoom_range=0.1, data_format='channels_last')
batches = gen.flow(X_train, y_train, batch_size=batch_size)
test_batches = gen.flow(X_test, y_test, batch_size=batch_size)
steps_per_epoch = int(np.ceil(batches.n/batch_size))
validation_steps = int(np.ceil(test_batches.n/batch_size))

import matplotlib.pyplot as plt

# load ONE image from training set to display on screen
img = X_train[1]

# visualize original image
plt.imshow(img[:,:,0], cmap='gray')

# trick our generator into believing img has enough dimensions
# and get some augmented images for our single test image
img = np.expand_dims(img, axis=0)
aug_iter = gen.flow(img)

aug_img = next(aug_iter)[0].astype(np.float32)
aug_img.shape

import matplotlib.pyplot as plt

# show augmented images
f = plt.figure(figsize=(12,6))
for i in range(8):
    sp = f.add_subplot(2, 26//3, i+1)
    sp.axis('Off')
    aug_img = next(aug_iter)[0].astype(np.float32)
    plt.imshow(aug_img[:,:,0], cmap='gray')  
    
print(X_train.shape)  
'''
 