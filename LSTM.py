# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:34:06 2018

@author: Vasudev
"""
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler

Input = pd.read_csv('Input.csv')

for i in range(0, len(Input['Gold Price'])):
    Input['Gold Price'][i] = float(Input['Gold Price'][i].replace(',',''))
    Input['DJIA'][i] = float(Input['DJIA'][i].replace(',',''))

x_train = Input[['DJIA', 'Silver Price', 'Copper Price', 'US Dollar Index', 'VIX']]
y_train = Input[['Gold Price']]

scaler = MinMaxScaler(feature_range=(0, 0.95))
scaler_x = scaler.fit(x_train)
scaler_y = scaler.fit(y_train)
x_scaled = scaler_x.transform(x_train)
y_scaled = scaler_y.transform(y_train)

x_scaled = np.reshape(x_scaled, (x_scaled.shape[0], 1, x_scaled.shape[1]))


model = Sequential()

model.add(LSTM(5, activation='relu', input_dim=5))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_scaled, y_scaled, epochs=5, batch_size=32)

Test = pd.read_csv('Test Prices Daily.csv')

for i in range(0, len(Test['DJIA'])):
    Test['DJIA'][i] = float(Test['DJIA'][i].replace(',',''))

x_test = Test[['DJIA', 'Silver Price', 'Copper Price', 'US Dollar Index', 'VIX']]

scaler_x = scaler.fit(x_test)
x_scaled_test = scaler_x.transform(x_test)

x_scaled_test = np.reshape(x_scaled_test, (x_scaled_test.shape[0], 1, x_scaled_test.shape[1]))
prediction = model.predict(x_scaled_test, batch_size=128)

Gold_prices = prediction*(max(Input['Gold Price']) - min(Input['Gold Price'])) + min(Input['Gold Price'])
print(Gold_prices)