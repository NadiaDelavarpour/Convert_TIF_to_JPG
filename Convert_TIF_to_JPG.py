#!/usr/bin/env python
# coding: utf-8

# In[15]:


from osgeo import gdal
    
options_list = [
    '-ot Byte',
    '-of JPEG',
    '-b 1',
    '-b 2',
    '-b 3',
    '-scale'
]           

options_string = " ".join(options_list)
    
gdal.Translate(
    'C:/Users/nadia/Downloads/Test.jpg',
    'C:/Users/nadia/Downloads/Test.TIF',
    options=options_string
)


# In[18]:


import cv2
import os
from PIL import Image

def split(rows, cols, path_to_image):
    #number of rows and column you want to split your image
    #the exact directory to the image
    im = Image.open(path_to_image)
    im_width, im_height = im.size

    row_width = (im_width / rows)
    row_height = (im_height / cols)
    n = 0
    for i in range(0, cols):
        for j in range(0, rows):
            box = (j * row_width, i * row_height, j * row_width +
                   row_width, i * row_height + row_height)
            outp = im.crop(box)
            name, ext = os.path.splitext(path_to_image)
            outp_path = name + "_" + str(n) + ext
            print("Exporting image tile: " + outp_path)
            outp.save(outp_path)
            n += 1




path_to_image ='C:/Users/nadia/Downloads/Test.JPG'
im = cv2.imread(path_to_image)
split(2, 4, path_to_image)


# In[34]:


import os
from osgeo import gdal
import cv2
import os
from PIL import Image

rootdir = 'D:/Ortho_Data/Barely'
list = os.listdir(rootdir)
options_list = [
    '-ot Byte',
    '-of JPEG',
    '-b 1',
    '-b 2',
    '-b 3',
    '-scale'
]
n = 0
for item in list:
    print(item)
    path = os.path.join(rootdir, item)
    options_string = " ".join(options_list)
    name, ext = os.path.splitext(path)
    outp_path = name +'.jpg'            
    gdal.Translate(
    outp_path,
    path,
    options=options_string)
    im = cv2.imread(outp_path)
    split(2, 4, outp_path)
    n += 1


# In[ ]:




