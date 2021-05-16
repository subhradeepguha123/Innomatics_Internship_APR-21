#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy
m,n=list(map(int,input().split()))
a=numpy.array([input().split() for i in range(m)],int)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.around(numpy.std(a),decimals=11))

