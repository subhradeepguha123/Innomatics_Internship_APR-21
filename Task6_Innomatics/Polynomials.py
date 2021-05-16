#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy
a = list(map(float, input().split()))
#m = input()
print(numpy.polyval(a,float(input())))

