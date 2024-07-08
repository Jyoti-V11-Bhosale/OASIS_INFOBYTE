#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
airbnb=pd.read_csv('AB_NYC_2019.csv')


# In[3]:


airbnb.shape


# In[4]:


airbnb.dtypes


# In[5]:


airbnb.info()


# In[9]:


airbnb.duplicated().sum()
airbnb.drop_duplicates(inplace=True)


# In[10]:


airbnb.isnull().sum()


# In[11]:


airbnb.drop(['name','id','host_name','last_review'], axis=1, inplace=True)


# In[13]:


airbnb.head(4)


# In[14]:


airbnb.isnull().sum()


# In[16]:


airbnb.fillna({'reviews_per_month':0}, inplace=True)

airbnb.reviews_per_month.isnull().sum()


# In[17]:


airbnb.isnull().sum()
airbnb.dropna(how='any',inplace=True)
airbnb.info()


# In[18]:


airbnb.describe()


# In[33]:


airbnb.columns


# In[24]:


airbnb_encoded = pd.get_dummies(airbnb, columns=['city', 'neighborhood'])
print(airbnb_encoded)


# In[27]:


airbnb.head(15)

