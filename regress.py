import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your stock market dataset from a local CSV file
file_path = 'BAJAJFINSV.csv'
df = pd.read_csv(file_path)

# Choose the independent and dependent variables
X = df['Prev Close'].values
Y = df['Close'].values

# Calculate the mean of X and Y
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Calculate the slope (m) and intercept (b) manually
numerator = np.sum((X - mean_X) * (Y - mean_Y))
denominator = np.sum((X - mean_X) ** 2)
m = numerator / denominator
b = (mean_Y - m * mean_X) 

# Print the coefficients
print('Intercept (b):', b)
print('Slope (m):', m)

# Make predictions on the test set
Y_pred = b + m * X

# Visualize the regression line and scatter plot
plt.scatter(X, Y, color='black', label='Actual Data')
plt.plot(X, Y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('Previous Close Price')
plt.ylabel('Closing Price')
plt.title('Simple Linear Regression for Bajaj Finance Stock')
plt.legend()
plt.show()
