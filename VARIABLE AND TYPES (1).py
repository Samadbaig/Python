#!/usr/bin/env python
# coding: utf-8

# # Variables and its data type

# # A Python Variable is a reserved memory location to store values.

# # naming a variable is same as indentifers

# # No need to delecare a variable in python like c

# In[2]:


# variable assignment opertor (=) use to assign a value to the variable
a=10
b=5.5
c='abdul'


# In[3]:


#multiple assignment
a,b,c=1,2.2,'abdul'


# In[4]:


a=b=c='king'


# # storage location

# In[8]:


a=3
print(id(a))


# In[6]:


b=2
print(id(b))


# In[9]:


c=3
print(id(c)) #reuse of memory


# # Data type

# # every value in python has a data type sinces every thing is an object in python programming

# # NUMBERS

# # INTERGER, fLOTING POINT NUMBER AND COMPLEX NUMBERS FALL IN THIS CATEGORY THEY ARE DEFINE AS INT FLOT AND COMPLEX

# In[10]:


A=5
print(type(A))


# In[11]:


A=5.9
print(type(A))


# In[17]:


A=2+2j
print(type(A))


# In[ ]:




