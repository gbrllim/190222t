#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


from flask import request, render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")

        model = joblib.load("DBSReg")
        pred = model.predict([[float(rates)]])
        s1 = "The predicted DBS share price based on Linear Regression Model is $" + str(pred[0][0])
        
        model = joblib.load("DBSDT")
        pred = model.predict([[float(rates)]])
        s2 = "The predicted DBS share price based on Decision Tree Model is $" + str(pred[0])
        
        model = joblib.load("DBSNN")
        pred = model.predict([[float(rates)]])
        s3 = "The predicted DBS share price based on the Neural Network Model is $" + str(pred[0])
        
        return(render_template("index.html",result1=s1,result2=s2,result3=s3))
    else:
        return(render_template("index.html",result1="No Input",result2="No Input",result3="No Input"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




