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

#### Figure 1. Illustrative Examples of Chest X-Rays in Patients with Pneumonia

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/Illustrative%20Examples%20of%20Chest%20X-Rays%20in%20Patients%20with%20Pneumonia.png>

## Technique Used for Preprocessing
We do two main steps of preprocessing our poor quality of acquired raw images is 

Initially, by doing intensity correction of the raw image is encountered by the log-normalization function which adjusts the intensity contrast of the image dynamically.

Secondly, the Contrast Limited Adaptive Histogram Equalization (CLAHE) method is used for enhancing small details, textures and local contrast of the images. The proposed approach was tested using a radiographic survey phantom and a radiographic chest phantom and compared with conventional enhancement methods, such as histogram equalization, unsharp masking, CLAHE.

The results show that the CLAHE method yields great improvement on the pre-processing correction for digital chest radiography.

#### Figure 2. Image before CLAHE

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/image%20before%20CLAHE.jpeg>

#### Figure 3. Image after CLAHE

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/image%20after%20CLAHE.jpeg>

## Technique Used for Training Model 
Fine tuning using Convolutional Neural Network (CNN) Mobilenet Architecture

By using the pre-trained model of Mobilenet architecture, we can gain more accuracy in our model and make the training process much faster

## Result: Baseline CNN Implementation (without improvement)

Validation Accuracy: 81%

Test Accuracy: 79.16%

Macro Precision = 87%

Macro Recall = 72%

f1 score = 79%

Fluctuative training (fig 1/top) and loss (fig 2/bottom)

#### Figure 4. Accuracy Graph - without improvement

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/Accuracy%20Graph%20-%20without%20improvement.png>

## Result: Improvement

Validation Accuracy: 93.75%

Test Accuracy: 79.96%

Macro Precision = 88%

Macro Recall = 73%

f1 score = 80%

Stable accuracy after 30 epoch (fig 1 / top)

Stable loss after 20 epoch (fig 2 / bottom)

#### Figure 5. Accuracy - with improvement

<img src=https://github.com/YuanitaIP/DPS3-D-Bangkit-Final-Project-Assignment---Pneumonia-Classification/blob/master/Accuracy%20Graph%20-%20with%20improvement%20.png>

## Required Instalment 
1. Install Python 
    
    [Python] (https://www.python.org/downloads/)
    
2. Install TensorFlow
    
    [TensorFlow] [https://www.tensorflow.org/install) or (pip install tensorflow)
    
3. Install Jupyter Notebook

    [Jupyter] 

## Testing
Run the tests for this system 
1. Cloning the repository
2. Enter to this folder repo
3. Running code on Jupyter Notebook

## 

Team members:
I Putu Bagus Gede Prasetyo Raharja,
Yuanita Intan Paramitasari,
Muhammad Irzam Kasyfillah
