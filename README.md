# 🎬 Movie Recommendation System

A **content-based movie recommender system** built using Natural Language Processing and cosine similarity. Users can enter the name of a movie and get 5 similar movie recommendations — all through a clean, interactive **Streamlit interface**.

> ⚡ Built for learning, showcasing ML + UI skills, and impressing interviewers!

---

## 🚀 Demo

![App Screenshot](https://user-images.githubusercontent.com/your-demo-image-url)

Try it on **Streamlit Cloud**: [🔗 Live Demo](https://your-streamlit-link-if-hosted)

---

## 📌 Features

- 🔍 Movie name correction using fuzzy matching (`difflib`)
- 🧠 Intelligent suggestions using **cosine similarity**
- 🎨 Beautiful UI built with **Streamlit**
- 📚 NLP-based feature engineering (title, overview, genre, etc.)
- ✅ Runs completely **offline** using preprocessed `.pkl` files

---

## 🛠️ Tech Stack

| Tool         | Usage                        |
|--------------|------------------------------|
| 🐍 Python     | Core language                |
| 🧪 pandas     | Data preprocessing           |
| 🤖 scikit-learn | TF-IDF & Cosine similarity |
| 🧠 NLP        | Feature engineering          |
| 🎈 Streamlit  | Frontend/UI                  |
| 📁 Google Colab | Data preprocessing (optional) |

---

## 🧩 How It Works

1. User enters a movie title (e.g., `"Inception"`)
2. The app finds the **closest match** from the dataset using `get_close_matches()`
3. It calculates **cosine similarity** between that movie and others
4. Displays the **top 5 most si**
