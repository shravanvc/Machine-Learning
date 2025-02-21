import numpy as np

# Generate dummy data
X = np.array([1, 2, 3, 4, 5]) 
Y = np.array([2, 4, 6, 8, 10])  # Y = 2X (Linear relationship)

# Compute slope (m) and intercept (b) using least squares method
m = (np.mean(X * Y) - np.mean(X) * np.mean(Y)) / (np.mean(X**2) - np.mean(X)**2)
b = np.mean(Y) - m * np.mean(X)

# Predict values Y_pred = m * X + b
Y_pred = m * X + b

# Print results
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")
print(f"Predicted Y values: {Y_pred}")
