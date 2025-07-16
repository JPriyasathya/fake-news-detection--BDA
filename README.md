**FAKE NEWS DETECTION**

**📚 Table of Contents**

Overview
Objective
Project Workflow
Components
Tech Stack

**🌟 Overview**

This project addresses misinformation by analyzing news articles and classifying them as real or fake. It includes:
Data preprocessing
Feature engineering
Model training
Performance evaluation

**🎯 Objective**

Build a reliable pipeline that:
Ingests raw news content
Extracts key features (e.g., TF-IDF, readability, metadata)
Trains classifiers (e.g., Logistic Regression, CNN)
Outputs a binary prediction (real vs. fake)

**🔄 Project Workflow**

Data Gathering & Cleaning – Import datasets and preprocess text.
Feature Engineering – Extract TF‑IDF vectors and custom numeric features.
Model Training – Train multiple classifiers (e.g., Logistic Regression, CNN).
Evaluation – Assess models using accuracy, precision, recall, etc.
Prediction – Input a new news article → output real/fake label.

**⚙️ Components**

Data Processing – Scripts/notebooks to clean and vectorize text.
Feature Engineering – Generation of TF‑IDF and numeric features.
Modeling – Code to train & compare models including:
Logistic Regression
CNN-based text classifier
Report – Detailed analysis in ACM-format PDF.

**💻 Tech Stack**

Language: Python
Libraries: scikit-learn, TensorFlow/Keras or PyTorch
Notebooks: Jupyter
Data: Curated news articles, labeled real vs. fake
Output: .pkl model files, evaluation metrics, visualizations

**DATASET LINK** - https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/data

**DEPLOYMENT LINK** - https://fake-news-detection-fyhg.onrender.com
