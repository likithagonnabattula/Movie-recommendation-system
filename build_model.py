import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV
movies = pd.read_csv('movies.csv')

# Combine features into one 'tags' column
def clean(text):
    return text if isinstance(text, str) else ''

movies['tags'] = (
    movies['overview'].apply(clean) + ' ' +
    movies['genres'].apply(lambda x: x.replace('|', ' ') if isinstance(x, str) else '') + ' ' +
    movies['cast'].apply(clean) + ' ' +
    movies['director'].apply(clean) + ' ' +
    movies['keywords'].apply(clean)
)

movies['tags'] = movies['tags'].str.lower()

# Create new DataFrame with only what's needed
new_data = movies[['title', 'tags']].copy()

# Text vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_data['tags']).toarray()

# Cosine similarity matrix
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_data, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Enhanced movie_list.pkl and similarity.pkl saved!")
