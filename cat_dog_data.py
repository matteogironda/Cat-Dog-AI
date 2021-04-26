from PIL import Image
import numpy as np
import os
import time
import tensorflow as tf
import pathlib
tic = time.time()

cat_path = r"C:\Users\giron\Desktop\ai_set\kagglecatsanddogs_3367a\PetImages\Cat"
dog_path = r"C:\Users\giron\Desktop\ai_set\kagglecatsanddogs_3367a\PetImages\Dog"

cat_set_path = pathlib.Path(r"C:\Users\giron\Desktop\ai_set\cat_set")
dog_set_path = pathlib.Path(r"C:\Users\giron\Desktop\ai_set\dog_set")

files = os.listdir(cat_path) 

cat_set = np.zeros((64*64*3,12500))
dog_set = np.zeros((64*64*3,12500))

with os.scandir(cat_path) as cats:
    count = 0
    for cat in cats:
        try:
            im = Image.open(cat_path+'/'+str(count) + '.jpg', 'r')
            image = im.resize((64,64))
            #occasional grayscale error, make sure everything is in RGB
            image = image.convert('RGB')
            
            cat_array = tf.keras.preprocessing.image.img_to_array(image, data_format=None, dtype=None)
            print(cat_array.shape)
            cat_array_flatten = cat_array.flatten().reshape(cat_array.shape[0]*cat_array.shape[1]*cat_array.shape[2], 1)   
            print(cat_array_flatten.shape)

            for i in range(12288):
                cat_set[i,count] = cat_array_flatten[i]
            print(count)
            #print(cat_set)
            count += 1
        except Exception as e:
            print(e)

np.save(cat_set_path, cat_set) 

with os.scandir(dog_path) as dogs:
    count = 0
    for dog in dogs:
        try:
            im = Image.open(dog_path+'/'+str(count) + '.jpg', 'r')
            image = im.resize((64,64))
            image = image.convert('RGB')
            
            dog_array = tf.keras.preprocessing.image.img_to_array(image, data_format=None, dtype=None)
            dog_array_flatten = dog_array.flatten().reshape(dog_array.shape[0]*dog_array.shape[1]*dog_array.shape[2], 1)
            
            print(dog_array_flatten.shape)

            for i in range(12288):
                dog_set[i,count] = dog_array_flatten[i]
            print(count)
            print(dog_set)
            count += 1
        except Exception as e:
            print(e)

np.save(dog_set_path, dog_set) 

toc = time.time() - tic

print(toc)