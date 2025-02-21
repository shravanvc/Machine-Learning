import numpy as np

# Define the softmax function
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtract max(x) for numerical stability
    return exp_x / np.sum(exp_x)

# Example input
scores = np.array([2.0, 1.0, 0.1])

# Calculate softmax probabilities
probabilities = softmax(scores)

# Print the result
print("Softmax Probabilities:", probabilities)
