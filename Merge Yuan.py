# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:09:36 2018

@author: Vasu
"""

import pandas as pd

dataYuan = pd.read_csv('USD_CNH Historical Data.csv')
data = pd.read_csv('Input.csv')

dataYuan['Date'] = pd.to_datetime(dataYuan.Date)
data['Date'] = pd.to_datetime(data.Date)

dataYuannewFrame = dataYuan[['Date','Price']]

Data2 = pd.merge(dataYuannewFrame,data, on='Date')

Data2.columns = ['Date', 'USD/CNH', 'DJIA', 'Silver Price', 'Gold Price', 'Copper Price', 'US Dollar Index', 'VIX']
Data2.to_csv("Input_with_Yuan.csv", index=False)

TestYuan = pd.read_csv('USD_CNH Historical Data Test Daily.csv')
Test= pd.read_csv('Test Prices Daily.csv')

TestYuan['Date'] = pd.to_datetime(TestYuan.Date)
Test['Date']  = pd.to_datetime(Test.Date)

TestYuan = TestYuan[['Date','Price']]
Data3 = pd.merge(TestYuan,Test, on='Date')

Data3.columns = ['Date', 'USD/CNH', 'DJIA', 'Silver Price', 'Copper Price', 'US Dollar Index', 'VIX']
Data3.to_csv("Output.csv", index=False)