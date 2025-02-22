import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression  # Corrected import

# Sample data: house sizes (sq ft) and prices ($1000s)
X = np.array([500, 700, 1000, 1200, 1500]).reshape(-1, 1)
y = np.array([100, 150, 200, 250, 300])

# Train model
model = LinearRegression()  # Fixed the model instantiation
model.fit(X, y)

# Predict and plot
X_test = np.array([800, 1100, 1400]).reshape(-1, 1)
y_pred = model.predict(X_test)

# Plotting the results
plt.scatter(X, y, color='blue', label="Training Data")
plt.plot(X_test, y_pred, color='red', linestyle="dashed", label="Predictions")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.legend()
plt.show()

