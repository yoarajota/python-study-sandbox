import numpy as np
import matplotlib.pyplot as plt
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl

x_train = np.array([1.0, 2.0])           #(size in 1000 square feet)
y_train = np.array([300.0, 500.0])           #(price in 1000s of dollars)

# The term 'cost' in this assignment might be a little confusing since the data is housing cost. Here, cost is a measure how well our model is predicting the target price of the house. The term 'price' is used for housing data.
# The equation for cost with one variable is:

# J(w,b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2
# where:
# f_{w,b}(x^{(i)}) = wx^{(i)} + b

# f_{w,b}(x^{(i)})  is our prediction for example using parameters w, b.
# (f_{w,b}(x^{(i)}) -y^{(i)})^2 is the squared difference between the target value and the prediction.
# These differences are summed over all the 2m examples and divided by 2m to produce the cost, J(w,b).

# Note, in lecture summation ranges are typically from 1 to m, while code will be from 0 to m-1.

# # # # # # # # # # # # # # # # # # # # # 

# The code below calculates cost by looping over each example. In each loop:

# f_wb, a prediction is calculated
# the difference between the target and the prediction is calculated and squared.
# this is added to the total cost.

def compute_cost(x, y, w, b): 
    """
    Computes the cost function for linear regression.
    
    Args:
      x (ndarray (m,)): Data, m examples 
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters  
    
    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    # number of training examples
    m = x.shape[0] 
    
    cost_sum = 0 
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum = cost_sum + cost  
    total_cost = (1 / (2 * m)) * cost_sum  

    return total_cost

# Your goal is to find a model f_{w,b}(x) = wx + b, with parameters w,b, which will accurately predict house values given an input x. The cost is a measure of how accurate the model is on the training data.

print(compute_cost(x_train, y_train, 200, 400))

# plt_intuition(x_train,y_train)

# plt.show()

# # The plot contains a few points that are worth mentioning. 
# # Cost is minimized when w = 200, which matches results from the previous lab
# # Because the difference between the target and pediction is squared in the cost equation, the cost increases rapidly when w is either too large or too small.
# # Using the w and b selected by minimizing cost results in a line which is a perfect fit to the data.

# # Cost Function Visualization- 3D
# # You can see how cost varies with respect to both w and b by plotting in 3D or using a contour plot.
# # It is worth noting that some of the plotting in this course can become quite involved. The plotting routines are provided and while it can be instructive to read through the code to become familiar with the methods, it is not needed to complete the course successfully. The routines are in lab_utils_uni.py in the local directory.

# x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
# y_train = np.array([250, 300, 480,  430,   630, 730,])

# plt.close('all') 
# fig, ax, dyn_items = plt_stationary(x_train, y_train)
# updater = plt_update_onclick(fig, ax, x_train, y_train, dyn_items)

# plt.show()

# # Convex Cost surface
# # The fact that the cost function squares the loss ensures that the 'error surface' is convex like a soup bowl. It will always have a minimum that can be reached by following the gradient in all dimensions. In the previous plot, because the  w and b dimensions scale differently, this is not easy to recognize. The following plot, where w and b are symmetric, was shown in lecture:

# soup_bowl()