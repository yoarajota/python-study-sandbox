import warnings
warnings.simplefilter('ignore')
import numpy as np
import matplotlib.pyplot as plt

# 𝜎=11+𝑒−𝑥

## Quickly define the sigmoid function
def sigmoid(x):
    """Sigmoid function"""
    return 1.0 / (1.0 + np.exp(-x)) # ranges from (0, 1). When the input 𝑥 is negative, 𝜎 is close to 0. When 𝑥 is positive, 𝜎 is close to 1. At 𝑥=0, 𝜎=0.5

# Plot the sigmoid function
vals = np.linspace(-10, 10, num=100, dtype=np.float32)

print(vals)
# activation = sigmoid(vals)
# fig = plt.figure(figsize=(12,6))
# fig.suptitle('Sigmoid function')
# plt.plot(vals, activation)
# plt.grid(True, which='both')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.yticks()
# plt.ylim([-0.5, 1.5]);