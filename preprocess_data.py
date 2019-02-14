from tensorflow import keras
import os

image_label_to_image_array = dict()
image_directory = os.getcwd()+'/train_images/'
for filename in os.listdir(image_directory):

    each_image = keras.preprocessing.image.load_img(os.path.join(image_directory,
                                                                 filename))
    image_label_to_image_array[filename] = keras.preprocessing.image.img_to_array(each_image)

print(len(image_label_to_image_array))
