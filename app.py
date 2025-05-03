from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('decision_tree_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Convert form data to numpy array
        features = [
            float(data['age']),
            int(data['gender']),
            int(data['ethnicity']),
            int(data['education_level']),
            float(data['bmi']),
            int(data['smoking']),
            float(data['alcohol_consumption']),
            float(data['physical_activity']),
            float(data['diet_quality']),
            int(data['memory_complaints']),
            int(data['behavioral_problems']),
            float(data['adl']),
            int(data['confusion']),
            int(data['disorientation']),
            int(data['personality_changes']),
            int(data['difficulty_completing_tasks']),
            int(data['forgetfulness'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]
        
        # Prepare response
        result = {
            'prediction': int(prediction),
            'probability': float(probability[1])  # Probability of having Alzheimer's
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 