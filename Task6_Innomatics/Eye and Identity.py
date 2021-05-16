#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy
m,n=map(int,input().split())
numpy.set_printoptions(sign=" ")
print(numpy.eye(m,n))

