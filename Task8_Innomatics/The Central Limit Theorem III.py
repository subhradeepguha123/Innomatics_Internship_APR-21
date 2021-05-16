#!/usr/bin/env python
# coding: utf-8

# In[12]:


samples = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float (input())

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))

