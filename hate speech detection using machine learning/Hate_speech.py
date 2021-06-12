# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:55:55 2021

@author: Fekadu
"""
import pickle
def NaiveB(data):
    nb = pickle.load(open('nb.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
def supportVect(data):
    nb = pickle.load(open('svm.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
#Logistic regression  classsification
def logisticReg(data):
    nb = pickle.load(open('lr.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
#KNN classification
def KNN(data):
    nb = pickle.load(open('knn.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
#decision Treee classification
def DT(data):
    nb = pickle.load(open('dt.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
#Random forest classification for 
def RF(data):
    nb = pickle.load(open('rf.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
#Gradient Boosting
def GB(data):
    nb = pickle.load(open('gb.sav', 'rb'))
    data.lower()
    data=[data]
    pr=nb.predict(data)
    return pr
