# 🚨 Smart Spam Detector: Interactive Web App

## 📖 Overview
This project implements a Machine Learning-based text classifier to detect whether an SMS or email is **Spam** or **Ham** (Safe). 

Instead of just running a background script, this project features a **fully interactive web dashboard** where users can paste custom text and receive real-time predictions. The model leverages Natural Language Processing (NLP) techniques, specifically TF-IDF vectorization, and is powered by a Naive Bayes classifier optimized for text data.

## ✨ Key Features
* **Interactive UI:** Built using Gradio, allowing non-technical users to test the model seamlessly.
* **Algorithm Comparison:** Evaluated both Logistic Regression and Multinomial Naive Bayes (Naive Bayes was selected for the final deployment due to higher precision).
* **NLP Pipeline:** Utilizes Scikit-Learn's `TfidfVectorizer` to convert raw text into mathematical features by penalizing common words and highlighting unique keywords.
* **Modular Design:** The training phase (Jupyter Notebook) is strictly separated from the deployment phase (`app.py`), using `pickle` to transfer the trained models.

## 🗂️ Project Structure
* `app.py`: The main Python script that runs the Gradio web dashboard.
* `Spam_Detection_Training.ipynb`: The Google Colab notebook containing data cleaning, exploratory analysis, and model training.
* `vectorizer.pkl`: The saved TF-IDF vocabulary dictionary.
* `model.pkl`: The trained Naive Bayes machine learning model.
* `requirements.txt`: List of dependencies needed to run the app.
* `spam.csv`: The dataset used to train the model.

## 🚀 How to Run Locally

**1. Clone the Repository**
```bash
git clone [https://github.com/aryankk073/Smart-Spam-Detector.git](https://github.com/aryankk073/Smart-Spam-Detector.git)
cd Smart-Spam-Detector
