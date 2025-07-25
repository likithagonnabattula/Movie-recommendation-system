import pickle
import numpy as np

# Example similarity matrix (4x4) for 4 movies
similarity = np.array([
    [1.0, 0.8, 0.6, 0.5],
    [0.8, 1.0, 0.7, 0.4],
    [0.6, 0.7, 1.0, 0.3],
    [0.5, 0.4, 0.3, 1.0]
])

# Save similarity.pkl
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)
