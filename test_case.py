#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from transaction import Transaction


# In[2]:


trx = Transaction()


# In[3]:


trx.add_item("Ayam Goreng",2,20000)
trx.add_item("Pasta Gigi",3,15000)
trx.check_order()


# In[4]:


trx.delete_item("Pasta Gigi")
trx.check_order()


# In[5]:


trx.reset_transaction()
trx.check_order()


# In[6]:


trx.add_item("Ayam Goreng",2,20000)
trx.add_item("Pasta Gigi",3,15000)
trx.add_item("Mainan Mobil",1,20000)
trx.add_item("Mi Instan",5,3000)
trx.check_order()


# In[7]:


trx.print_total()


# In[ ]:




