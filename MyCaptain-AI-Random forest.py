#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


train_data = pd.read_csv("C:/Users/match/Downloads/archive (2)/mnist_train.csv")
test_data=pd.read_csv("C:/Users/match/Downloads/archive (2)/mnist_test.csv")


# In[5]:


#viewing training data
train_data.head()


# In[10]:


#extracting data from the dataset and viewing them up close
a=train_data.iloc[2,1:].values


# In[11]:


a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[12]:


#separating labels and data value
x_train=train_data.iloc[:,1:]
y_train=train_data.iloc[:,0]
x_test=test_data.iloc[:,1:]
y_test=test_data.iloc[:,0]


# In[13]:


rf=RandomForestClassifier(n_estimators=100)


# In[14]:


rf.fit(x_train,y_train)


# In[15]:


pred=rf.predict(x_test)
pred


# In[16]:


#prediction accuracy
s=y_test.values
count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count=count+1
    


# In[17]:


count


# In[18]:


len(pred)


# In[19]:


#accuracy value
9703/10000


# In[ ]:




