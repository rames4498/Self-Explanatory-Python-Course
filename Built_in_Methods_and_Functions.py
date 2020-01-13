#!/usr/bin/env python
# coding: utf-8

# Lets start with a simple variable

# my_string is a variable in the below example

# In[10]:


my_string="GUVI"        


# Here len() is an example of python inbuilt function

# In[11]:


len(my_string)        #len() length function shows the length of the string


# Here 'lower' is an inbuilt method i.e lower is an example of methods
Methods can be visualized with some shortcuts  'Dot notation' 
i.e at the end of the object name you are supposed to use  '.'  then if you are jupyter notebook  'press Tab'  button , then you can visualize the methods available for the Objectconsider the above example    (applicable for jupyter notebook)
step 1: my_string           #call the object
     2:   my_string.        #press dot after the object
     3:  my_string.         #press tab after my_string.
# In[15]:


my_string.index("V")       #here we are finding the index of "V" in my_string with the Method called "Index"


# ###### Built-in vs User defined Functions and Methods

# There is a long list of built-in functions/methods besides that , you can create your own too! Also, you will see that when you download, installing and importing different Python libraries, they will come with extra functions and methods as well. So there are indeed infinite possibilities.

# we will see some inbuilt functions and Methods before going to user defined functions and Methods

# Python functions work very simply. You call the function and specify the required arguments, then it will return the results. 

# ###### Some of the most commonly used Built-in functions of python are as follows 
print() function takes arguements inside the open brackets
# In[2]:


print("Hii Guvi")


# len()    As discussed earlier length function defines the length of the object which is provided as an atribute 

# In[4]:


len("Hii Guvi")                     # refer indexing and slicing in data structures ,
                                    #A string is called as sequential list 


# type()  type function returns the variable type

# In[5]:


type("Hii Guvi")                             #returns a string 


# In[8]:


min(5,3,2,5,378,2,6,5,6,3)                 #minimum value 


# In[9]:


max(5,6,3,2,7,8,4,9,5,33)                  #maximum value 


# In[13]:


a=(98,37,63,45,13,24,65,431,39)         


# In[14]:


sorted(a)                   #sorting a tuple
                            #sorting in ascending order by default


# In[15]:


sorted(a,reverse=True)     #sorting in descending order by enabling the attribute reverse as True
                           #(read the document by placing the curser inside the brackets then use SHIFT + TAB )


# In[16]:


sum(a)                     #sum() function to add all the elements of the structure 


# ###### Built-in String methods

# In[47]:


#consider a string assinged to a variable 
my_data=" i am learning python through Guvi's online course "


# In[48]:


my_data.strip() #if a string has whitespaces at the beginning and end of the string then it removes them 


# In[49]:


my_data.capitalize() # capitalizes the first letter of a string 


# In[50]:


my_data.count('i')   # counts the number of such occurrences of a string


# In[51]:


my_data.index('G')   # returns its reference position


# In[52]:


b=my_data.split()    # splitting a string returns the list


# In[53]:


b


# In[54]:


#' '.join(my_data.split())
' '.join(my_data.split())


# In[55]:


my_data.replace('python','java')    #replacing the given string with another string 


# ###### Built-in Methods in Python Lists

# In[63]:


#consider a simple list 
data=['Guvi',2019,'IITM',7.5,True]


# In[64]:


data.append('Chennai')


# In[65]:


data


# In[66]:


data.pop()


# In[68]:


data.count('IITM')


# In[69]:


data.index(7.5)


# In[70]:


data.insert(3,'Taramani')


# In[71]:


data


# ###### Built-in methods in Dictionaries

# In[76]:


my_dict = {'cricketer':'Sachin','score':18426,'Average':44.8,'is_batsman':True,'Teams':['India','Mumbai','Mumbai Indians']}


# In[77]:


my_dict.keys()


# In[78]:


my_dict.values()


# In[79]:


my_dict.items()


# In[ ]:




