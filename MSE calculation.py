import numpy as np

# Define the mse function
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Example data
y_actual = np.array([1, 2, 3, 4, 5])  # Actual values
y_predicted = np.array([1.1, 1.9, 3.2, 3.8, 5.1])  # Predicted values

# Calculate MSE
error = mse(y_actual, y_predicted)

# Print the result
print("Mean Squared Error:", error)
