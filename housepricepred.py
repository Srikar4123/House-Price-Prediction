# Simple Linear Regression

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data into a variable
df = pd.read_csv('C:/Users/Dell/OneDrive/Desktop/ML Projects/Housing.csv')

# Displaying the dataset (i.e., first five rows using head method) 
df.head()

# Select the predictor attribute (x) and target attribute
(y) x = df[['area']]
y = df['price']

# Splitting the dataset into train and test data (70% train and 30% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)

# Simple Linear Model Creation 
model = LinearRegression()

# Train the model 
model.fit(x_train, y_train)

# Making Predictions
pred = model.predict(x_test)

# Evaluation of Model
err = mean_squared_error(y_test, pred) 
print(f'Mean Squared Error: {err}')

# Plotting the graph between Actual and Predicted Values
plt.scatter(y_test, pred, color='gold') 
plt.plot(x_test, pred, color='red', linewidth=1) 
plt.xlabel('Area (in sq.ft.)')
plt.ylabel('Price') 
plt.show()

# Multiple Linear Regression

# Displaying the dataset (i.e., first five rows using head method) 
df.head()
df.tail()

# Select the predictor attribute (x) and target attribute
x1 = df[['area','stories','bedrooms','bathrooms']]
y1 = df['price']

# Splitting the dataset into train and test data (70% train and 30% test)
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.3,random_state=50)

# Multiple Linear Model Creation 
model1 = LinearRegression()

# Train the model
model1.fit(x1_train, y1_train)

# Making Predictions
prediction = model1.predict(x1_test)

# Evaluation of Model
err = mean_squared_error(y1_test, prediction) 
print(f'Mean Squared Error: {err}')

# Plotting the graph between Actual and Predicted Values
plt.scatter(x_test, y_test, color='crimson',label='Actual')
plt.scatter(x_test, pred, color='green', label='Predicted')
plt.xlabel('Area (in sq.ft.)')
plt.ylabel('Price') 
plt.show()
