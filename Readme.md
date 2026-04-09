# 🎬 Movie Recommendation System

## 📌 Description
This project is a Movie Recommendation System developed as part of a PRML (Pattern Recognition and Machine Learning) course project. The system recommends movies using Machine Learning techniques based on user preferences and movie similarity.

The system implements:
- Collaborative Filtering (User-Based)
- Content-Based Filtering (Movie-Based)

It also integrates the TMDB API to fetch movie posters and enhance the user interface.


## ⚙️ Requirements

Make sure you have the following installed:

- Python 3.x
- pandas
- numpy
- scikit-learn
- scipy
- streamlit
- requests

### Install all dependencies using:

- pip install -r requirements.txt


## ▶️ How to Run the Project

1. Open terminal or command prompt

2. Navigate to the project folder: cd movie-recommendation

3. Run the Streamlit app:

4. Open the browser and go to: http://localhost:8501


## 📊 Features

- 🔍 Search movies by name  
- 🎯 Movie-based recommendations (Content-Based Filtering)  
- 👤 User-based recommendations (Collaborative Filtering)  
- 🎬 Movie posters using TMDB API  
- ⚡ Fast performance using caching  
- 🎨 Clean and modern UI (card-based layout)  


## 📁 Dataset

The project uses the MovieLens Small Dataset.

Files used:
- movies.csv  
- ratings.csv  
- links.csv  


## 🧠 Techniques Used

- Collaborative Filtering (Cosine Similarity)
- Content-Based Filtering (CountVectorizer)
- User-Movie Matrix Construction
- Data Preprocessing using pandas
- API Integration (TMDB)
- Caching for performance optimization


## 📓 Notebook

A Jupyter Notebook (`model.ipynb`) is included to demonstrate:
- Data loading  
- Preprocessing  
- Model building  
- Basic testing  


## 📂 Project Structure

movie-recommendation/
│
├── app.py
├── requirements.txt
│
├── data/
│ ├── movies.csv
│ ├── ratings.csv
│ ├── links.csv
│
├── src/
│ ├── preprocessing.py
│ ├── model.py
│ ├── recommend.py
│ ├── utils.py
│
├── notebook/
│ └── model.ipynb


## 📌 Notes

- Internet connection is required for fetching movie posters  
- Some movies may show placeholder images if posters are unavailable  
- The system is designed for educational purposes only  

---