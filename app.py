import gradio as gr
import pickle

# Load the saved vectorizer and model
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def predict_spam(email_text):
    # Transform the input text into numerical features
    text_vectorized = vectorizer.transform([email_text])
    
    # Predict using the loaded model
    prediction = model.predict(text_vectorized)
    
    # Return the result
    if prediction[0] == 1:
        return "🚨 SPAM DETECTED"
    else:
        return "✅ SAFE (HAM)"

# Build the Gradio interface
interface = gr.Interface(
    fn=predict_spam, 
    inputs=gr.Textbox(lines=5, placeholder="Paste the email or SMS text here..."), 
    outputs=gr.Textbox(label="Prediction Result"),
    title="Smart Text Classifier: Spam Detector",
    description="A Machine Learning project using Naive Bayes and TF-IDF to classify text messages."
)

if __name__ == "__main__":
    interface.launch()