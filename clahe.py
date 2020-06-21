import cv2
import os

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))

basedir = 'chest_xray'
for subdir in os.listdir(basedir):
    for _class in os.listdir(os.path.join(basedir,subdir)):
        for image_dir in os.listdir(os.path.join(basedir,subdir,_class)):
            image_path = os.path.join(basedir,subdir,_class,image_dir)
            image = cv2.imread(image_path,0)
            img_clahe = clahe.apply(image)
            cv2.imwrite(os.path.join('clahe_chest_xray',subdir,_class,image_dir),img_clahe)
