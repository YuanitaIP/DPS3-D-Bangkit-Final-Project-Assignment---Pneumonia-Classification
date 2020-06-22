# Pneumonia Classification 
## Overview
Bangkit Final Project is the final assignment given to the Bangkit's participant for the requirement to be graduated from the program. Team DPS3-D is choosing the pneumonia dataset and making the classification platform using Contrast-limited Adaptive Histogram Equalization (CLAHE) for preprocessing and applying the Convolutional Neural Network (CNN) Mobilenet Architecture layer for the model.

The initiation using pneumonia is because the condition in the time of the final project given is mostly all countries over the world are stroke by pandemic respiratory disease.

By constructing the pneumonia detector app, it can help medical officers to do a quick preliminary examination for further lab check at the hospital to determine this patient is suffering from ordinary pneumonia or COVID19-related pneumonia.

## Problem
Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. 

Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.

It is needed efficient decision-making in determining patient’s preliminary pneumonia indication. 
As pneumonia can be a life-threatening.

## Dataset
Our dataset is named Chest X-Ray Images (Pneumonia) by Paul Mooney.

The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

For the details of the datasets, you can visit: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

## Context
The normal chest X-ray (left panel) depicts clear lungs without any areas of abnormal opacification in the image. Bacterial pneumonia (middle) typically exhibits a focal lobar consolidation, in this case in the right upper lobe (white arrows), whereas viral pneumonia (right) manifests with a more diffuse ‘interstitial’ pattern in both lungs.

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/Illustrative%20Examples%20of%20Chest%20X-Rays%20in%20Patients%20with%20Pneumonia.png>

## Preprocessing
We do two main steps of preprocessing our poor quality of acquired raw images is by intensity correction of the raw image is encountered by the log-normalization function which adjusts the intensity contrast of the image dynamically. 

Secondly, the Contrast Limited Adaptive Histogram Equal- ization (CLAHE) method is used for enhancing small details, textures and local contrast of the images. The proposed ap- proach was tested using a radiographic survey phantom and a radiographic chest phantom and compared with conven- tional enhancement methods, such as histogram equalization, unsharp masking, CLAHE. 

The results show that the CLAHE method yields great improvement on the pre-processing correction for digital chest radiography.

## Model
Downloading, extracting, and placing the model in the assets folder is managed automatically.

## Required Installment 
1. Install Python 
    
    [Python] (https://www.python.org/downloads/)
    
2. Install TensorFlow
    
    [TensorFlow] [https://www.tensorflow.org/install) or (pip install tensorflow)
    
3. Install Jupyter Notebook

## Testing
Run the tests for this system 
1. Cloning the repository
2. Enter to this folder repo
3. Running code on Jupyter Notebook

## Accuracy Obtained
According to the final test model, the value of accuracy obtained is:


## Technique Used
Convolutional Neural Network or CNN is being used 

## 

Team members:
I Putu Bagus Gede Prasetyo Raharja,
Yuanita Intan Paramitasari,
Muhammad Irzam Kasyfillah
