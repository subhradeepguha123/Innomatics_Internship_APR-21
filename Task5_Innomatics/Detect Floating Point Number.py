#!/usr/bin/env python
# coding: utf-8

# In[36]:


import re
for _ in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)

