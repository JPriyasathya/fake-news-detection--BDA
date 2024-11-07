from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model from the pickle file
model_path = 'models/model_pipeline.pkl'
with open(model_path, 'rb') as file:
    model_pipeline = pickle.load(file)

# Define the home route that displays the dashboard
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route that receives user input and returns the prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the user input from the form
        content = request.form['content']
        
        # Make a prediction using the loaded model
        prediction = model_pipeline.predict([content])[0]
        
        # Convert the prediction to a readable label
        prediction_label = 'Fake' if prediction == 0 else 'Real'
        
        return render_template('index.html', prediction_label=prediction_label, content=content)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
