#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q-2 Nested Lists

if __name__ == '__main__':
    list= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([score, name])
        list.sort()
        a = [i for i in list if i[0] != list[0][0]]
        b = [j for j in a if j[0] == a[0][0]]
        b.sort(key=lambda x: x[1])
    for i in range(len(b)):
        print(b[i][1])

