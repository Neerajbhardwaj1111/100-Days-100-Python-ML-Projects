import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits,on='title')

def parse_names(x):
    try:
        return " ".join([i['name'] for i in ast.literal_eval(x)])
    except:
        return ""

def get_director(x):
    try:
        for i in ast.literal_eval(x):
            if i['job'] == 'Director':
                return i['name']
    except:
        return ""
    return ""

movies['cast'] = movies['cast'].apply(parse_names)
movies['crew'] = movies['crew'].apply(get_director)
movies['keywords'] = movies['keywords'].apply(parse_names)
movies['genres'] = movies['genres'].apply(parse_names)


movies['combined'] = movies['cast'] + " " + movies['crew'] + " " + movies['keywords'] + " " + movies['genres']


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])

similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

title_index = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend_movies(title, n=5):
    if title not in title_index:
        return f"❌ Movie '{title}' not found."

    idx = title_index[title]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()


# CLI Interface
if __name__ == '__main__':
    print("🎬 Welcome to TMDB Collaborative Filtering Recommender (CLI)")
    while True:
        query = input("\n🔍 Enter a movie title (or type 'exit'): ").strip()
        if query.lower() == 'exit':
            print("👋 Goodbye!")
            break
        results = recommend_movies(query)
        if isinstance(results, str):
            print(results)
        else:
            print(f"\n✨ Top recommendations similar to '{query}':")
            for i, title in enumerate(results, 1):
                print(f"{i}. {title}")
