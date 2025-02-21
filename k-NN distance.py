
import numpy as np 
def euclidean_distance(x1, x2): 
 return np.sqrt(np.sum((x1 - x2) ** 2))
 # Example dataset 
X_train = np.array([[1, 2], [3, 4], [5, 6]]) 
X_test = np.array([3, 3])
 # Compute distances 
distances = [euclidean_distance(x, X_test) for x in X_train]
print("Distances to test point:", distances)

