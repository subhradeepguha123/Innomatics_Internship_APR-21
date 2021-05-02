#!/usr/bin/env python
# coding: utf-8

# In[ ]:


_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))

