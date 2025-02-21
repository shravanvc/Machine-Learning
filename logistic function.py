import numpy as np 
def sigmoid(x): return 1 / (1 + np.exp(-x)) 
# Test the sigmoid function 
x = np.array([-2, -1, 0, 1, 2]) 
y = sigmoid(x) 
print("Input:", x) 
print("Sigmoid Output:", y)




