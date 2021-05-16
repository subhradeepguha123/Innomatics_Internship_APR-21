#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy
m,n=list(map(int,input().split()))
a=numpy.array([input().split() for i in range(m)],int)
M=numpy.min(a,axis=1)
print(numpy.max(M))

