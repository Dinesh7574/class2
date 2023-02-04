#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = 123
print (type(a))


# In[3]:


a=123
print(isinstance(a,int))


# In[5]:


a = "123"
print(isinstance(a,int))


# In[6]:


a =123
print(float(a)) #it is decimal


# In[9]:


a = 123
print(hex(a))


# In[10]:


a = 123
print(oct(a))


# In[12]:


a = '123'
print(int(a))


# In[13]:


a = 'test'
print(int(a))


# In[14]:


a = 'test'
print(str(a))


# In[18]:


a = 'test'
print(a.isdigit())


# In[19]:


a = '123'
print(a.isdigit())


# In[21]:


a = input()
print (a)
print(type(a))


# In[1]:


a = input()
print(max(a))
print(min(a))
print(sorted(a))
print(a.isdigit())



# In[2]:


a = "test"
print(a.isalpha()) #it is to check alphabet


# In[3]:


print(a.isalnum()) # it is to check alphabet or number


# In[4]:


print(a.isdigit()) # it is check it is digit


# In[10]:


a = ["dinesh","21","chennai"]
print(isinstance(a,list))


# In[11]:


a = [100,20,34,22]
print(type(a))


# In[12]:


a = [100,20,34,22.0]
print(sorted(a))


# In[14]:


a = [100,20,34,22.0]
print(min(a))
print(max(a))


# In[15]:


a = [100,20,34,22,"demo"] #list can hold str and float 
print(type(a))


# In[26]:


a = ["dinesh","21","chennai"]
print(a.index("dinesh"))


# In[27]:


a = ["dinesh","21","chennai"]
print(a.find("dinesh"))


# In[28]:


print(a[::-1])


# In[32]:


print(a[1:3])


# In[33]:


a = [10,20,30,40,50]


# In[34]:


a.append(100) #to add value in last position
print(a)


# In[35]:


a.insert(2,15) #to add particular value in that position
print(a)


# In[36]:


a.remove(15) #to delete particular value
print(a)


# In[37]:


del a[2]    #to delete particular value in that position
print(a)


# In[59]:


a = [["hello","hi"],["demo","try"]]
print(a[1])


# In[78]:


a = [["hello","hi"],["demo","try"]]
print(a[1][0])


# In[19]:


a = "viratkholi"
print(a.count(''))
print(a.index("i",5))


# In[ ]:





# In[ ]:




