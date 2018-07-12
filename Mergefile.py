# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 21:32:43 2018

@author: Vasu
"""

import pandas as pd

dataDJ = pd.read_csv('Dow Jones Daily.csv')
dataAg = pd.read_csv('Silver Daily.csv')
dataGold = pd.read_csv('Gold daily.csv')
dataCopper = pd.read_csv('Copper Daily.csv')
dataUS_Dollar = pd.read_csv('US Dollar Index daily.csv')
dataVIX = pd.read_csv('CBOE Volatility Daily.csv')

dataDJ['Date'] = pd.to_datetime(dataDJ.Date)
dataAg['Date'] = pd.to_datetime(dataAg.Date)
dataGold['Date'] = pd.to_datetime(dataGold.Date)
dataCopper['Date'] = pd.to_datetime(dataCopper.Date)
dataUS_Dollar['Date'] = pd.to_datetime(dataUS_Dollar.Date)
dataVIX['Date'] = pd.to_datetime(dataVIX.Date)

DJnewFrame = dataDJ[['Date','Price']]
AgnewFrame = dataAg[['Date','Price']]
GoldnewFrame = dataGold[['Date','Price']]
CoppernewFrame = dataCopper[['Date', 'Price']]
US_DollarnewFrame = dataUS_Dollar[['Date', 'Price']]
VIXnewFrame = dataVIX[['Date','Price']]

# joins the data on the same date
df_merge = pd.merge(DJnewFrame,AgnewFrame, on='Date')
df_merge2 = pd.merge(df_merge, GoldnewFrame, on = 'Date')
df_merge3 = pd.merge(df_merge2, CoppernewFrame, on = 'Date')
df_merge4 = pd.merge(df_merge3, US_DollarnewFrame, on = 'Date')
final = pd.merge(df_merge4, VIXnewFrame, on = 'Date')

final.columns = ['Date', 'DJIA', 'Silver Price', 'Gold Price', 'Copper Price', 'US Dollar Index', 'VIX']
final.to_csv("Input.csv", index=False)

#------------------Test Prices--------------------------------------
TestDJ = pd.read_csv('Dow Jones Test Daily.csv')
TestSilver = pd.read_csv('Silver Test Daily.csv')
TestCopper = pd.read_csv('Copper Daily Test.csv')
TestUS_Dollar = pd.read_csv('US Dollar Index Daily Test.csv')
TestVIX = pd.read_csv('Vix Test Daily.csv')

TestDJ['Date'] = pd.to_datetime(TestDJ.Date)
TestSilver['Date'] = pd.to_datetime(TestSilver.Date)
TestCopper['Date'] = pd.to_datetime(TestCopper.Date)
TestUS_Dollar['Date'] = pd.to_datetime(TestUS_Dollar.Date)
TestVIX['Date'] = pd.to_datetime(TestVIX.Date)

TestDJnewFrame = TestDJ[['Date','Price']]
TestSilvernewFrame = TestSilver[['Date', 'Price']]
TestCoppernewFrame = TestCopper[['Date','Price']]
TestUS_DollarnewFrame = TestUS_Dollar[['Date','Price']]
TestVIXnewFrame = TestVIX[['Date','Price']]

Test_merge = pd.merge(TestDJnewFrame, TestSilvernewFrame, on = 'Date')
Test_merge1 = pd.merge(Test_merge, TestCoppernewFrame, on = 'Date')
Test_merge2 = pd.merge(Test_merge1, TestUS_DollarnewFrame, on = 'Date')
Final_Test = pd.merge(Test_merge2, TestVIXnewFrame, on = 'Date')

Final_Test.columns = ['Date', 'DJIA', 'Silver Price', 'Copper Price', 'US Dollar Index', 'VIX']
Final_Test.to_csv("Test Prices Daily.csv", index=False)