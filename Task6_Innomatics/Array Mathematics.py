#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy
n,m=list(map(int,input().split()))
mat1=numpy.array([input().split() for i in range(n)],int)
mat2=numpy.array([input().split() for i in range(n)],int)
print(mat1+mat2)
print(mat1-mat2)
print(mat1*mat2)
print(mat1//mat2)
print(mat1%mat2)
print(mat1**mat2)

