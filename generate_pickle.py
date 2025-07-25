import pandas as pd
import pickle

# Sample movie list DataFrame (add your actual data if you have it)
movie_data = pd.DataFrame({
    'title': ['Inception', 'Interstellar', 'The Dark Knight', 'The Prestige'],
    'movie_id': [0, 1, 2, 3]
})

# Save as a valid pickle file
with open('movie_list.pkl', 'wb') as f:
    pickle.dump(movie_data, f)

print("✅ movie_list.pkl created successfully!")
