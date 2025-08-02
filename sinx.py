# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 13:45:13 2025

@author: BCA-NEW-33
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Given data points (in radians)
x = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi])
y = np.array([0, 0.5, np.sqrt(2)/2, np.sqrt(3)/2, 1, np.sqrt(3)/2, np.sqrt(2)/2, 0.5, 0])

# Reshape for sklearn
x = x.reshape(-1, 1)

# Create polynomial features
poly = PolynomialFeatures(degree=5)
x_poly = poly.fit_transform(x)

# Fit linear regression on polynomial features
model = LinearRegression()
model.fit(x_poly, y)

# Generate smooth x values for plotting
x_smooth = np.linspace(0, np.pi, 100).reshape(-1, 1)
x_smooth_poly = poly.transform(x_smooth)
y_smooth = model.predict(x_smooth_poly)

# Plot (Non-blocking)
plt.scatter(x, y, color='red', label='Given Points')
plt.plot(x_smooth, y_smooth, label='Polynomial Regression Fit')
plt.title('Approximation of sin(x) using Polynomial Regression')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show(block=False)

# User input in degrees
for i in range(5):
    try:
        degrees = float(input(f"Attempt {i+1}/5 - Enter a value of x (in degrees, between 0 and 180): "))
        if 0 <= degrees <= 180:
            radians = np.deg2rad(degrees)  # Convert degrees to radians
            user_input_poly = poly.transform([[radians]])
            predicted_y = model.predict(user_input_poly)
            print(f"Predicted sin({degrees}°) ≈ {predicted_y[0]:.5f}")
            print(f"Actual sin({degrees}°) = {np.sin(radians):.5f}")
        else:
            print("Please enter a value between 0 and 180 degrees.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    print()  # Blank line between attempts
