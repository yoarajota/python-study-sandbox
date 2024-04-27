import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('./style.mplstyle')

# As in the lecture, you will use the motivating example of housing price prediction.
# This lab will use a simple data set with only two data points - a house with 1000 square feet(sqft) sold for $300,000 and a house with 2000 square feet sold for $500,000. These two points will constitute our data or training set. In this lab, the units of size are 1000 sqft and the units of price are 1000s of dollars.

# Size (1000 sqft)	Price (1000s of dollars)
# 1.0	300
# 2.0	500
# You would like to fit a linear regression model (shown above as the blue straight line) through these two points, so you can then predict price for other houses - say, a house with 1200 sqft.

# Please run the following code cell to create your x_train and y_train variables. The data is stored in one-dimensional NumPy arrays.

# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")