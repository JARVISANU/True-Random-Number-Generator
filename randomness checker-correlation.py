#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot
import numpy as np
f = open(r"C:\Users\Anusha\Documents\Arduino\mini testuuuu.txt", "r")
k=[]
for line in f:
    k.append(line.strip())
k.remove('')

x = [k[i:i + 8] for i in range(0, len(k), 8)] 
k = list(map(int, k))
r=[]
for i in range(0,len(x)):
    r.append(str("".join(x[i])))
for i in range(0,len(x)):
    r[i]=int(r[i],2)


x = np.array(r[:1758])
y = np.array(r[1758:])
print("without processing",np.corrcoef(x,y))

pyplot.scatter(r[:1758], r[1758:])
pyplot.show()

for i in range(3516):
    if r[i] == 255:
        r[i] =r[ 3516-i]
print("with processing",np.corrcoef(r[:1758],r[1758:]))
pyplot.scatter(r[:1758], r[1758:])
pyplot.show()


# In[3]:


hahahahhahahahahahahhahahaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


# In[ ]:


tata anusaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
later thank meeeeeeeee with big treatttttttttttttttt and more netttttttttttttttttttttttt and more foooooooooooooood and one more bday gifttttttttttttttttttttttttt tatataaaaaaaaaaaaaaa aaaaaaaa   venuna serupu tharen
podi elame uninstall pantiy
elathayim kolapity poren waitshut up

