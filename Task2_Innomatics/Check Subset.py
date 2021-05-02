#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))

