from tensorflow import keras
import os
import pandas as pd
import numpy as np

def images_to_array():
    image_label_to_image_array = dict()
    image_directory = os.getcwd()+'/train_images/'
    image_array = []
    count = 0
    for filename in os.listdir(image_directory):
        #count += 1
        #if count>10:
        #    break
        each_image = keras.preprocessing.image.load_img(os.path.join(image_directory,
                                                                     filename))
        array = keras.preprocessing.image.img_to_array(each_image)
        print(array.shape)
        image_label_to_image_array[filename] = array
        image_array.append(array)
    image_array = np.array(image_array)
    print(image_array.shape)
    return image_label_to_image_array,image_array

def read_labels():
    labels_directory = os.getcwd() + '/traininglabels.csv'
    labels = pd.read_csv(labels_directory)
    labels = labels.drop('score', 1)
    labels_values = labels.iloc[:,1].values
    print(labels_values.shape)
    return labels.to_dict(),labels_values

if __name__=='__main__':
    #images_to_array()
    labels = read_labels()
    print(len(labels))