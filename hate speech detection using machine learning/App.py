# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:17:25 2021

@author: Fekadu
"""

from flask import Flask, render_template, request
from Hate_speech import NaiveB,supportVect,logisticReg,KNN,RF,GB
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("material.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form['msg']
    al=request.form['ml']
    userText=''
    if al=='nb':
        userText=NaiveB(data)
    elif al=='svm':
        userText=supportVect(data)
    elif al=='lr':
        userText=logisticReg(data)
    elif al=='knn':
        userText=KNN(data)
    elif al=='rf':
        userText=RF(data)
    else:
        userText=GB(data)
    return render_template('material.html', msg="Your Post is "+str(userText)[1:-1])
if __name__ == "__main__":
    app.run(host='10.240.69.50',port=9030)
