# 📰 Fake News Detection (Python - Machine Learning Project)

**Project Overview:**

The project aims to build a Fake News Detection System using Python and Machine Learning techniques. It classifies news articles as Fake or Real using text processing and supervised learning algorithms.

**Multiple machine learning models were implemented and evaluated, including:**

Logistic Regression

Naive Bayes

Support Vector Machine (SVM)

Random Forest Classifier


The model achieves the highest accuracy using Logistic Regression with TF-IDF feature extraction.

**Features:**

📌 Text Preprocessing — Combines title and text, cleans and processes news articles.

📌 Feature Extraction — Uses TF-IDF Vectorization to convert text into numerical features.

📌 Model Comparison — Compares Logistic Regression, Naive Bayes, SVM, Random Forest, and LSTM models.

📌 Model Saving — Final pipeline model saved using pickle for reuse.

📌 Performance Metrics — Uses accuracy score and classification report to measure model effectiveness.

**Dataset Information:**

Dataset sourced from Fake and Real News datasets.

Labeled as:

1 → Real News
0 → Fake News

Dataset is shuffled, preprocessed, and split into 80% training and 20% testing.

**Technologies Used:**

Python

Libraries : pandas, numpy, scikit-learn, joblib, pickle (for model saving)

KAGGLE LINK - https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/data

DEPLOYMENT LINK - https://fake-news-detection-fyhg.onrender.com
