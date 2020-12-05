#!/usr/bin/env python
# coding: utf-8

# # Scraping basics for Selenium
# 
# If you feel comfortable with scraping, you're free to skip this notebook.

# ## Part 0: Imports
# 
# Import what you need to use Selenium, and start up a new Chrome to use for scraping. You might want to copy from the [Selenium snippets](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-snippets/) page.
# 
# **You only need to do `driver = webdriver.Chrome()` once,** every time you do it you'll open a new Chrome instance. You'll only need to run it again if you close the window (or want another Chrome, for some reason).

# In[280]:


from selenium import webdriver
driver = webdriver.Chrome()


# ## Part 1: Scraping by class
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-class.html, printing out the title, subhead, and byline.

# In[281]:



driver.get("http://jonathansoma.com/lede/static/by-class.html")


# In[282]:


headlines = driver.find_elements_by_class_name("title")
for headline in headlines:
    print(headline.text.strip())


# In[283]:


headlines = driver.find_elements_by_class_name("subhead")
for headline in headlines:
    print(headline.text.strip())


# In[284]:


headlines = driver.find_elements_by_class_name("byline")
for headline in headlines:
    print(headline.text.strip())


# ## Part 2: Scraping using tags
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-tag.html, printing out the title, subhead, and byline.

# In[285]:


driver.get("http://jonathansoma.com/lede/static/by-tag.html")


# In[286]:


headlines = driver.find_elements_by_tag_name("h1")
for headline in headlines:
    print(headline.text.strip())


# In[287]:


headlines = driver.find_elements_by_tag_name("h3")
for headline in headlines:
    print(headline.text.strip())


# In[288]:


headlines = driver.find_elements_by_tag_name("p")
for headline in headlines:
    print(headline.text.strip())


# ## Part 3: Scraping using a single tag
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-list.html, printing out the title, subhead, and byline.
# 
# > **This will be important for the next few:** if you scrape multiples, you have a list. Even though it's Seleninum, you can use things like `[0]`, `[1]`, `[-1]` etc just like you would for a normal list.

# In[289]:


driver.get("http://jonathansoma.com/lede/static/by-list.html")


# In[290]:


headlines = driver.find_elements_by_tag_name("p")
for headline in headlines:
    print(headline.text.strip())


# In[ ]:





# ## Part 4: Scraping a single table row
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, printing out the title, subhead, and byline.

# In[291]:


driver.get("http://jonathansoma.com/lede/static/single-table-row.html")


# In[292]:


headlines = driver.find_elements_by_tag_name("tr")
for headline in headlines:
    print(headline.text.strip())


# In[ ]:





# ## Part 5: Saving into a dictionary
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, saving the title, subhead, and byline into a single dictionary called `book`.
# 
# > Don't use pandas for this one!

# In[293]:


driver.get("http://jonathansoma.com/lede/static/single-table-row.html")


# In[294]:


headlines = driver.find_elements_by_tag_name("table")
for headline in headlines:
    print(headline.text.strip())


# In[ ]:





# ## Part 6: Scraping multiple table rows
# 
# Scrape the content at http://jonathansoma.com/lede/static/multiple-table-rows.html, printing out each title, subhead, and byline.
# 
# > You won't use pandas for this one, either!

# In[295]:


driver.get("http://jonathansoma.com/lede/static/multiple-table-rows.html")


# In[296]:


headlines = driver.find_elements_by_tag_name("tbody")
for headline in headlines:
    print(headline.text.strip())


# ## Part 7: Scraping an actual table
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a list of dictionaries.
# 
# > Don't use pandas here, either!

# In[297]:


driver.get(" http://jonathansoma.com/lede/static/the-actual-table.html")


# In[298]:


headlines = driver.find_elements_by_tag_name("tr")
for headline in headlines:
    print(headline.text.strip())


# In[ ]:





# In[ ]:





# ## Part 8: Scraping multiple table rows into a list of dictionaries
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a pandas DataFrame.
# 
# > There are two ways to do this one! One uses just pandas, the other one uses the result from Part 7.

# In[299]:


import pandas as pd
import numpy as np


# In[300]:


pip install lxml


# In[301]:


tables = pd.read_html("http://jonathansoma.com/lede/static/the-actual-table.html")
df = tables[0]


# In[302]:


df.columns = ['Topics', 'Lessons', 'Authors']


# In[303]:


df


# In[ ]:


df = [{"Topics": "How to Scrape Things", "How to Scrape Many Things", "The End of Scraping", "Lessons": "Some Supplemental Materials", "But Is It Even Possible?", "Lets All Use CSV Files", "Authors": "By Jonathan Soma", "By Sonathan Joma", "By Amos Nathanos"}]
df


# ## Part 9: Scraping into a file
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html and save it as `output.csv`

# In[305]:


from selenium import webdriver
driver = webdriver.Chrome()
import re 


# In[306]:


driver.get("http://jonathansoma.com/lede/static/the-actual-table.html")


# In[307]:


table = driver.find_element_by_xpath("/html/body/table")
print(table.text)


# In[ ]:




