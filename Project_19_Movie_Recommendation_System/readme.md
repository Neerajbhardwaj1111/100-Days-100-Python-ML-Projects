# 🎬 Movie Recommendation System (Collaborative Filtering)

A command-line based movie recommendation system built using Collaborative Filtering (Content-Based) on the TMDB 5000 dataset. This system recommends movies based on cast, crew, genres, and keywords using TF-IDF vectorization and cosine similarity.

---

## 📁 Dataset

We use two datasets from [TMDB (The Movie Database)]:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 🚀 Features

- Combines cast, director, genres, and keywords to generate a unique feature vector for each movie.
- Uses `TfidfVectorizer` to transform text data into numerical vectors.
- Calculates cosine similarity between all movies.
- Provides a list of top N similar movies via CLI interface.

---

## 🧰 Tech Stack

- Python 3.7+
- pandas
- scikit-learn
- ast
- TMDB 5000 dataset (CSV files)

---
