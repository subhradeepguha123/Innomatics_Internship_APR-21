#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
def arrays(arr):
    return numpy.array(arr,float)[::-1]
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

