
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import os
import random
import cv2 


# In[14]:


pts_img = np.array([[597,702 ], [723, 730], [637, 802],[512, 775]]) 


# In[15]:


pts_wrd = np.array([[0, 0], [1, 0], [1, 1],[0, 1]])      


# In[16]:


h1, status = cv2.findHomography(pts_img, pts_wrd) 


# In[12]:


bl_pix = np.array([0,1080,1])             # pixel location of bottom-left image 
bl_meter = h1.dot(bl_pix)                # world-coordinate of bottom-left 
h2 = np.array([[1, 0, abs(bl_meter[0])],[0, -1 ,abs(bl_meter[1])],[0, 0, 1]])

h = h2.dot(h1)              # the final homography matrix


# In[66]:


file = open("Downloads/final_pos.txt","r")


# In[67]:


file1=open("Downloads/real_coordinates.txt","w")


# In[68]:


for line in file:
    fields = line.split(" ")
    frame=fields[0]
    print(type(frame))
    ped_id=fields[1]
    print(type(ped_id))
    x=fields[3]
    y=fields[2]
    print("x:" + x +"y:" + y)
    x=int(x)
    y=int(y)
    test_pt1_pix = np.array([x,y,1])
    print(test_pt1_pix)
    test_pt1_met = h.dot(test_pt1_pix)
    print(test_pt1_met)
    opt =["%.2f" % i for i in test_pt1_met]
    print("Converted array to string:\n")
    print(opt)
    data=frame+" "+ped_id+" "+opt[1]+" "+opt[0]+"\n"
    file1.write(data)
file.close()    
file1.close()

