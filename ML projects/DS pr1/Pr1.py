#!/usr/bin/env python
# coding: utf-8

# In[91]:


pip install openpyxl


# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('D:/2021/Yearly Consolidated/BANKNIFTY.csv')     #importing the banknifty dataset


# In[3]:


df.head()


# In[9]:


df.columns


# In[5]:


df.insert(7,column="RANGE",value=df["HIGH"]-df["LOW "])    #inserting the required range column


# In[6]:


df.to_excel("BANKNIFTY_NEW.xlsx")                    #creating an excel file of the updated dataset


# In[7]:


df1=pd.read_csv('D:/2021/Yearly Consolidated/NIFTY.csv')        #importing the nifty dataset


# In[8]:


df1.head()


# In[10]:


df1.columns


# In[12]:


df1.insert(7,column="RANGE",value=df1["HIGH"]-df1["LOW"])     #inserting the required range column


# In[13]:


df1.head()


# In[14]:


df1.to_excel("NIFTY_NEW.xlsx")      #creating an excel file of the updated dataset


# In[ ]:




