from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
(x_train,y_train),(x_test,y_test)=mnist.load_data() #loading data from keras datasets

# x_train is the features, y_train is the labels or classes of the data (train is for training our model)
# x_test is the features, y_test is the labels or classes of the data (test is for testig the model)

print(x_train.shape) #checking the dimensions of the data

#Now we will check see some random images from our dataset using matplotlob library

k=331
for i in range(0,9):
    plt.subplot(k) #subplot takes a 3 digit integer where 1st digit=number of row, 2nd digit=number of column and 3rd digit = position
    k+=1
    random_index=np.random.randint(0,len(x_train)) #generating a random number using numpy
    # plt.imshow(x_train[random_index]) #ploting the image in the image
    #we can also plot the image in gray scale using cmap=plt.get_cmap('gray')
    plt.imshow(x_train[random_index], cmap=plt.get_cmap('gray')) #ploting the image in grayscale
plt.show() #showing the image
