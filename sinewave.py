#Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y axis with Sine
# Function for Plotting Sine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.sin(x)

# Plotting Sine Graph
plt.plot(x, y, color='green')
plt.show()

#This is a test