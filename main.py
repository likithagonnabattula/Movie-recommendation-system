import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV file
movies = pd.read_csv('movies.csv')

# Combine overview and genres into one field
movies['tags'] = movies['overview'] + ' ' + movies['genres'].str.replace('|', ' ')
movies['tags'] = movies['tags'].fillna('').str.lower()

# Feature extraction
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Recommend function
def recommend(movie):
    movie = movie.lower()
    movie_index = movies[movies['title'].str.lower() == movie].index
    if len(movie_index) == 0:
        print("❌ Movie not found.")
        return
    movie_index = movie_index[0]
    distances = list(enumerate(similarity[movie_index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]

    print(f"\n🎬 Top 5 recommendations for '{movies.iloc[movie_index].title}':")
    for i in distances:
        print("-", movies.iloc[i[0]].title)

# Main loop
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a movie title (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        recommend(user_input)
