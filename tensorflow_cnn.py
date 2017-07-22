# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:17:30 2017

@author: O222069
"""
print(python.__version__)
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense,Dropout

classifier=Sequential()
#step 1 Convolution
#classifier.add(Convolution2D(64,3,3,input_shape=(3,32,32)))
classifier.add(Conv2D( 32, 3,3,input_shape=(64, 64,3),activation='relu'))
#step 2 Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

#adding second convolution layer
classifier.add(Conv2D( 2, (3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
#step 3 Flatten
classifier.add(Flatten())
#step 4 Full Connection
classifier.add(Dense(output_dim=128,activation='relu'))

classifier.add(Dense(output_dim=1,activation='sigmoid'))

#compiling the CNN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#P2 fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datgen=ImageDataGenerator(rescale=1./255)

train_set=train_datagen.flow_from_directory('dataset/training_set/',target_size=(64,64),batch_size=128,class_mode='binary')

test_set=train_datagen.flow_from_directory('dataset/test_set/',target_size=(64,64),batch_size=128,class_mode='binary')

classifier.fit_generator(train_set,steps_per_epoch=8000,epochs=2,validation_data=test_set,validation_steps=2000)



# For a single-input model with 2 classes (binary classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
#model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=200, batch_size=10)
