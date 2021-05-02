#!/usr/bin/env python
# coding: utf-8

# In[ ]:


k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))

