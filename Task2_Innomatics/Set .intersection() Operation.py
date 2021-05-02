#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print(len(st1.intersection(st2)))

