#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install rembg


# In[2]:


from rembg import remove


# In[3]:


from PIL import Image


# In[4]:


input_path ='Heath_Joker.jpg'


# In[5]:


output_path ='Heath_Joker1.png'


# In[6]:


input =Image.open(input_path)


# In[7]:


output =remove(input)


# In[8]:


output.save(output_path)


# In[ ]:




