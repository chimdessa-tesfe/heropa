#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request, render_template, session, redirect, url_for, session
import numpy as np
import pickle
import pandas as pd
import datetime as dt
import bz2


# In[2]:


app = Flask(__name__)


# In[3]:


def conver_date(date):
    #WeekOfYear = dt.datetime.strptime(date, "%Y-%m-%d").weekofyear
    Year = dt.datetime.strptime(date, "%Y-%m-%d").year
    Month = dt.datetime.strptime(date, "%Y-%m-%d").month
    DayOfMonth = dt.datetime.strptime(date, "%Y-%m-%d").day
    return { "Year":Year, "Month": Month, "DayOfMonth":DayOfMonth}


# In[4]:


def one_hot(data):
    if data == "0":
        return 0
    elif data == 'a':
        return 2
    elif data == 'b':
        return 2
    elif data == 'c':
        return 3
    elif data == 'd':
        return 4


# In[7]:


def radio_to_binary(data):
    if data == 'on':
        return 1
    else:
        return 0


# In[6]:


@app.route('/home', methods=['GET', 'POST'])
def index():
    # # Create instance of the form.
    return render_template('home.html')


# In[8]:


@app.route('/prediction',methods=['POST'])
def prediction():

    feature_dict = {"SchoolHoliday": [int(request.form['school'])],
    "StoreType": [one_hot(request.form['store_type'])],
    "PromoOpen": [int(request.form['PromoOpen'])],
    "DayOfMonth": [conver_date(request.form['date'])['DayOfMonth']],
    "Year": [conver_date(request.form['date'])['Year']],
    "Month": [conver_date(request.form['date'])['Month']],
    "CompetionDistance": [int(request.form['competion_distance'])],
    "Assortment": [one_hot(request.form['assortment'])],
    "StateHoliday": [one_hot(request.form['state_holiday'])],
    "Store": [int(request.form['Store'])],
    "Promo": [radio_to_binary(request.form['promo'])],
    "Promo2": [radio_to_binary(request.form['promo2'])],
    "DayOfWeek": [int(request.form['day_of_week'])]
    }
    test_frame = pd.DataFrame.from_dict(feature_dict)
    prediction = model.predict(test_frame)
    return render_template('home.html', prediction_text='Prediction input $ {}'.format(prediction))
    #return render_template('prediction.html')


# In[9]:


@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


# In[10]:



@app.route('/about')
def about():
    return render_template('about.html')


# In[11]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




