#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy
n=int(input())
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print(numpy.dot(a,b))

