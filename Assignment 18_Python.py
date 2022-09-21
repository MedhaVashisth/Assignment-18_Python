#!/usr/bin/env python
# coding: utf-8

# In[7]:


def hours():
    print('Open 9-5 daily')


# In[9]:


import zoo
zoo.hours()


# In[5]:


from google.colab import files
uploaded = files.upload()


# In[10]:


import zoo as menagerie
menagerie.hours()


# In[11]:


plain = {'a': 1, 'b': 2, 'c': 3}


# In[12]:


plain


# In[16]:


from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy 
OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# In[18]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']


# In[ ]:




