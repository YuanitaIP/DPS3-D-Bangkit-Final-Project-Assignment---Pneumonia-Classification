import tensorflow as tf
import cv2
new_model = tf.keras.models.load_model('DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/model_version_1.h5')
new_model.summary()
from PIL import Image
import numpy as np
from skimage import transform
import os

def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (224, 224,3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image
    
basedir = 'DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/chest_xray/train/Normal'
for _class in os.listdir(os.path.join(basedir)):
        image_path = os.path.join(basedir,_class)
        print(image_path)
        image = load(image_path)
        predict = new_model.predict(image)
        y_classes = predict.argmax(axis=1)
        print(y_classes)


