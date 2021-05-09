#!/usr/bin/env python
# coding: utf-8

# In[45]:


import re
for _ in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')

