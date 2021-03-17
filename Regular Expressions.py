#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Find all the word in the string
import re
allinform = re.findall("inform","we need to inform him with the least information")
for i in allinform:
    print(i)


# In[6]:


#Search the word inform
import re
if re.search("inform","we need to inform him with the least information"):
 print('There is inform')


# In[9]:


#Generate an iterator
import re
str = 'we need to inform him with the latest information'
for i in re.finditer('inform',str):
    locttuple=i.span()
    print(locttuple)


# In[10]:


#Match words with particular pattern
import re
str = 'sat,hat,mat,pat'
allstr = re.findall('[shmp]at',str)
for i in allstr:
    print(i)


# In[11]:


#Match the string with range of characters
import re
str = 'sat,hat,mat,pat'
allstr = re.findall('[h-m]at',str)
for i in allstr:
    print(i)


# In[12]:


#When we use ^ symbol,everything excepts hat and mat will be printed
import re
str = 'sat,hat,mat,pat'
allstr = re.findall('[^h-m]at',str)
for i in allstr:
    print(i)


# In[17]:


#Replace a string
import re
food = "hat rat mat pat"
regex = re.compile("[r]at")
food = regex.sub("food",food)
print(food)


# In[ ]:





# In[19]:


#Explaining the backslash problem-to solve this problem I can make use of regular expressions
import re
randstr= "here is \\drogba"
print(randstr)


# In[2]:


import re
randstr= "here is \\drogba"
print(re.search(r"\\drogba",randstr))


# In[23]:


#Match a single character
import re
randstr='12345'
print('matches:',len(re.findall('\d{5}',randstr)))


# In[24]:


#Dealing with white space character
import re
randstr='''
keep the blue flag
flying high
chelsea
'''
print(randstr)


# In[4]:


#Remove the whitespace
import re
randstr='''
keep the blue flag
flying high
chelsea
'''
print(randstr)

regex = re.compile("\n")

randstr = regex.sub(" ", randstr)

print(randstr)

#Other white spaces
#\b: backspace
#\f:formfeed
#\r: carriage return
#\t:tab
#\v:vertical


# In[26]:


#Phone number verification
#\w[a-zA-z0-9]lower case 'w'will match anything inside the brackets
#\W[^a-zA-z0-9]uppercase 'W'will not match anything which is inside the brackets
phn='412-555-1212'
if re.search('\w{3}-\w{3}-\w{4}',phn):
#I can even use '\d'because they represent digits
    print("It is a phone number")


# In[27]:


#Full name is valid or not
import re
if re.search('\w{2,20}\s\w{2,20}',"kiara madisen"):
    print('Full name is valid')


# In[6]:


#E-mail verification
email ="sk@aol.com ms@.com @seo.com dc@.com"
print('email matches:',len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))


# In[40]:


#Web scraping

import urllib.request
from re import findall
url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"
response=urllib.request.urlopen(url)
html = response.read()
htmlstr = html.decode()
pdata = findall("\(\d{3}\) \d{3}-\d{4}",htmlstr)
for item in pdata:
    print(item)


# In[ ]:





# In[ ]:




