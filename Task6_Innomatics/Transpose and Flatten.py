#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
our_array = numpy.array([input().split() for y in range(int(input().split()[0]))], int)
print(numpy.transpose(our_array), our_array.flatten(), sep="\n")

