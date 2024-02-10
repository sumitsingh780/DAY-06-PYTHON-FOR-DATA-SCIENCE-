#!/usr/bin/env python
# coding: utf-8

# # DAY 06 OF 100 DAY MACHINE LEARNING CHALLENGE

# # PLOTLY LIBRARY 

# In[1]:


pip install plotly


# In[2]:


x = [2,3,4,5,6,7,8]
y = [9,8,7,6,5,3,2]


# In[4]:


import matplotlib.pyplot as plt 
import seaborn as sns


# # same graph in matplotlib

# In[7]:


plt.plot(x,y)
plt.title ("line graph")
plt.show()


# # same graph in seaborn 

# In[10]:


fig = sns.lineplot(x = x ,y = y, color = 'r')
plt.show()


# # same graph using plotly library 

# In[21]:


import plotly.express as px
x = [2,3,4,9,6,7,8]
y = [9,8,2,6,5,8,2]
fig = px.line(x = x,y = y , title = " line graph")
fig.show()


# In[14]:


import plotly.graph_objects as go


# In[19]:


fig = go.Figure(go.Scatter(x=x,y = y))
fig.show ()


# # ADDING TITLE 

# In[25]:


x = [2,3,4,5,6,7,8]
y = [9,8,2,6,5,5,2]
fig =go.Figure(go.Scatter(x=x,y=y))
fig.update_layout(title =" line graph ", xaxis_title = " this is x axis", yaxis_title = " this is y axis")
fig.show()


# In[26]:


x1 ,y1 = [3,4,5,6,7],[9,8,7,6,5]
x2,y2 = [ 9,3,6,8,9],[4,5,7,8,9]
x3,y3 = [ 7,3,6,9,9],[2,5,1,8,4]


# In[27]:


fig = go.Figure()


# In[30]:


fig.add_trace(go.Scatter(x = x1 , y = y1))
fig.add_trace(go.Scatter(x = x2 , y = y2))
fig.add_trace(go.Scatter(x = x3 , y = y3))
fig.update_layout(title =" line graph ", xaxis_title = " this is x axis", yaxis_title = " this is y axis")


# # BUBBLE CHART 

# In[36]:


x =[2,5,7,9]
y= [7,6,5,4]
fig = go.Figure(go.Scatter(x=x,y=y,mode = "markers", marker_size = [50,30,40,20]))
fig.update_layout(title =" Line Graph ", xaxis_title = " This is X Axis", yaxis_title = " This is Y Axis")
fig.show()


# In[ ]:




