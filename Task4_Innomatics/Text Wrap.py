#!/usr/bin/env python
# coding: utf-8

# In[25]:


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    dedented_text = textwrap.dedent(text=string) 
    result = wrapper.fill(text=dedented_text) 
    return result

