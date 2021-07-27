#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


dataset=pd.read_csv('kickstarter_projects.csv')


# In[7]:


dataset.head()


# In[8]:


dataset.tail()


# In[10]:


dataset.shape


# In[13]:


dataset.columns


# In[17]:


dataset.nunique()


# In[18]:


dataset['ID'].value_counts


# In[19]:


dataset['ID'].dtype


# In[20]:


dataset.info()


# In[ ]:




