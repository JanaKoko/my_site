#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)
from flask import url_for, render_template, request, redirect


# In[2]:


@app.route('/')
def one():
    return render_template('form.html')


# In[3]:


@app.route('/questions')
def que():
    return render_template('qu.html')


# In[4]:


@app.route('/stats')
def stat():
    return render_template('stats.html')


# In[5]:


@app.route('/thanks')
def th():
    return render_template('thanks.html')


# In[ ]:


if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:




