#!/usr/bin/env python
# coding: utf-8

# In[9]:


string = input()
line = input().split()
i, c = int(line[0]), line[1]
print(string[:i] + c + string[i+1:])

