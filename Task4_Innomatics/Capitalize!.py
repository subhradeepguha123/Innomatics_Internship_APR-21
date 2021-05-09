#!/usr/bin/env python
# coding: utf-8

# In[33]:


def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

