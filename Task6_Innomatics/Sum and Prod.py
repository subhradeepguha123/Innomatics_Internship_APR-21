#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
S=numpy.sum(A,axis=0)
print(numpy.product(S,axis=0))

