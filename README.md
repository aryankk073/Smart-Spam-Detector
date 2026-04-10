# Smart-Spam-Detector
"A Machine Learning-powered text classifier built with Python to detect and filter Spam vs. Ham (safe) messages using TF-IDF Vectorization and Naive Bayes, featuring an interactive Gradio dashboard."

# Smart Text Classifier: Spam Detector 📧

A machine learning semester project that classifies emails and SMS messages as either Spam or Ham (Safe). 

## Core Concepts Covered
* **Natural Language Processing (NLP):** TF-IDF Vectorization
* **Algorithms Compared:** Logistic Regression vs. Naive Bayes
* **Deployment:** Interactive web dashboard using Gradio

## How to Run the Dashboard Locally
1. Clone this repository to your local machine.
2. Install the required dependencies by running:
   `pip install -r requirements.txt`
3. Launch the web application:
   `python app.py`
4. Open the local URL provided in your terminal to test the model.

## Project Structure
* `Spam_Detection_Training.ipynb`: Google Colab notebook containing data preprocessing and model training.
* `app.py`: The Gradio web interface script.
* `vectorizer.pkl`: The saved TF-IDF vocabulary dictionary.
* `model.pkl`: The trained Naive Bayes machine learning model.
* `spam.csv`: The dataset used for training.
