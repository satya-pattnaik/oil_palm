import pathlib
import os
import tensorflow as tf
import pandas as pd
AUTOTUNE = tf.contrib.data.AUTOTUNE


def get_all_images():
    all_image_paths = os.path.join(os.getcwd(), 'train_images')
    all_image_paths = pathlib.Path(all_image_paths)

    all_image_paths = list(all_image_paths.glob('*.jpg'))
    all_image_paths = [str(path) for path in all_image_paths]
    image_count = len(all_image_paths)
    print('The length of training set:', image_count)
    return all_image_paths
def preprocess_image(image_path,label):
    image = tf.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize_images(image, [256, 256])
    print(image.shape)
    image /= tf.reduce_max(image)  # normalize to [0,1] range

    return image,label

def read_labels():
    labels_directory = os.getcwd() + '/traininglabels.csv'
    labels = pd.read_csv(labels_directory)
    labels = labels.drop('score', 1)
    labels_values = labels.iloc[:,1].values
    print(labels_values.shape)
    return labels_values

def batch_data(batch_size = 64):
    all_image_paths = get_all_images()
    all_image_labels = read_labels()
    labels_count = all_image_labels.shape
    print('The length of training set labels:',labels_count)

    path_ds = tf.data.Dataset.from_tensor_slices((all_image_paths, all_image_labels))

    path_ds = path_ds.map(preprocess_image)
    path_ds = path_ds.batch(batch_size)
    global AUTOTUNE
    path_ds = path_ds.prefetch(AUTOTUNE)

    return path_ds

if __name__=='__main__':

    path_ds = batch_data()
    print(path_ds)