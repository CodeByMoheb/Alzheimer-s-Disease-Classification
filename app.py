from flask import Flask, render_template, request, jsonify, make_response
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import pdfkit
import os
import sys

app = Flask(__name__)

# Configure pdfkit with wkhtmltopdf path
try:
    # Try different possible paths for wkhtmltopdf
    possible_paths = [
        'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe',
        'C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe',
        os.path.join(os.path.dirname(sys.executable), 'wkhtmltopdf.exe')
    ]
    
    wkhtmltopdf_path = None
    for path in possible_paths:
        if os.path.exists(path):
            wkhtmltopdf_path = path
            break
    
    if wkhtmltopdf_path is None:
        raise FileNotFoundError("wkhtmltopdf not found. Please install it from https://wkhtmltopdf.org/downloads.html")
    
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
except Exception as e:
    print(f"Warning: PDF generation may not work: {str(e)}")
    config = None

# Load the trained model
model = joblib.load('best_alzheimer_model.joblib')

# Feature names and their ranges
FEATURES = {
    'Age': {'min': 10, 'max': 100, 'unit': 'years'},
    'BMI': {'min': 15, 'max': 40, 'unit': 'kg/m²'},
    'PhysicalActivity': {'min': 1, 'max': 10, 'unit': 'scale'},
    'SleepQuality': {'min': 1, 'max': 10, 'unit': 'scale'},
    'SystolicBP': {'min': 90, 'max': 200, 'unit': 'mmHg'},
    'CholesterolTotal': {'min': 100, 'max': 300, 'unit': 'mg/dL'},
    'CholesterolHDL': {'min': 20, 'max': 100, 'unit': 'mg/dL'},
    'MMSE': {'min': 0, 'max': 30, 'unit': 'score'},
    'FunctionalAssessment': {'min': 1, 'max': 10, 'unit': 'scale'},
    'ADL': {'min': 1, 'max': 10, 'unit': 'scale'}
}

@app.route('/')
def home():
    return render_template('index.html', features=FEATURES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        patient_name = data.pop('patientName', 'Anonymous')
        
        # Convert to float and handle missing values
        features = []
        for feature in FEATURES.keys():
            value = data.get(feature, '')
            if value == '':
                return jsonify({'error': f'Missing value for {feature}'}), 400
            try:
                value = float(value)
                if value < FEATURES[feature]['min'] or value > FEATURES[feature]['max']:
                    return jsonify({'error': f'{feature} must be between {FEATURES[feature]["min"]} and {FEATURES[feature]["max"]}'}), 400
                features.append(value)
            except ValueError:
                return jsonify({'error': f'Invalid value for {feature}'}), 400
        
        # Make prediction
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]
        
        # Format results
        result = {
            'patient_name': patient_name,
            'prediction': 'Positive' if prediction == 1 else 'Negative',
            'confidence': f"{max(probability) * 100:.2f}%",
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'details': {
                feature: {
                    'value': features[i],
                    'unit': FEATURES[feature]['unit']
                } for i, feature in enumerate(FEATURES.keys())
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/print_report', methods=['POST'])
def print_report():
    try:
        if config is None:
            return jsonify({'error': 'PDF generation is not configured. Please install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html'}), 500
            
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # Add current year for the report
        data['current_year'] = datetime.now().year
        
        html = render_template('report.html', data=data)
        
        # PDF options for better rendering
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        try:
            # Generate PDF using pdfkit
            pdf = pdfkit.from_string(html, False, options=options, configuration=config)
        except Exception as e:
            print(f"PDF Generation Error: {str(e)}")
            return jsonify({'error': 'Failed to generate PDF. Please ensure wkhtmltopdf is properly installed.'}), 500
        
        # Create response
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=alzheimer_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        return response
    except Exception as e:
        print(f"Report Generation Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 