#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import os
for dirname, _, filenames in os.walk("C:/Users/shahu/Downloads/archive (4)/UberDataset.csv"):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[9]:


data = pd.read_csv("C:/Users/shahu/Downloads/archive (4)/UberDataset.csv")
data.head()


# In[10]:


data.info()


# In[11]:


data = data.dropna()
data.isnull().values.sum()


# In[12]:


data.describe()


# In[13]:


start_place = data["START"].unique()
print(start_place)
print("The number of unique start stations are ",len(start_place))


# In[14]:


stop_place  = data["STOP"].unique()
print(stop_place)
print("The number of unique stop stations are ",len(stop_place))


# In[15]:


san_francisco = data[data["START"] == "San Francisco"]
san_francisco


# In[16]:


start_places_count = pd.DataFrame(data["START"].value_counts())
start_places_count = start_places_count.head().reset_index()
start_places_count = start_places_count.rename(columns = {'index':'START','START':'Counts'})
start_places_count.head()


# In[17]:


stop_places_count = pd.DataFrame(data["STOP"].value_counts())
stop_places_count = stop_places_count.reset_index()
stop_places_count = stop_places_count.rename(columns = {'index':'STOP','STOP':'Counts'})
stop_places_count.head()


# In[18]:


frequent_place = pd.DataFrame(data.groupby(["START","STOP"]).size())
frequent_place = frequent_place.rename(columns = {0:'Count'})
frequent_place[frequent_place["Count"] == max(frequent_place["Count"])]


# In[20]:


purVSmiles = pd.DataFrame(data["MILES"].groupby(data["PURPOSE"]).sum())
purVSmiles.plot(kind = "bar")
plt.show()


# In[21]:


tripVScat = pd.DataFrame(data["CATEGORY"].value_counts())
tripVScat.plot(kind = "bar")
plt.show()
proportion = data["MILES"].groupby(data["CATEGORY"]).sum()
print(proportion)
print("Business proportion is  ",proportion.iloc[0]/(proportion.iloc[0]+proportion.iloc[1]))
print("Personal proportion is ", proportion.iloc[1]/(proportion.iloc[0]+proportion.iloc[1]))


# In[22]:


purposes = data["PURPOSE"].unique()
data["MILES"].groupby(data["PURPOSE"]).sum()


# In[ ]:




