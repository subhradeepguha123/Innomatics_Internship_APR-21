#!/usr/bin/env python
# coding: utf-8

# In[37]:


import re
s = input()
for t in re.split(r",|\.", s):
    if t != '': print(t)

