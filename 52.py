

# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the ranges.
x = np.arange(-5, 5, 0.1)
y = 2 * x**2 + 3 * x + 1

# Create the plot.
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 2x^2 + 3x + 1')

# Display the plot.
plt.show()