# Alzheimer's Disease Classification System

A machine learning-based web application for Alzheimer's disease risk assessment using medical parameters.

## Features

- Interactive web interface for patient assessment
- Real-time risk prediction using machine learning models
- Detailed PDF report generation
- Input validation and range checking
- Professional medical interface design

## Web Application Screenshots

### Home Page
![Home Page](E:\edge project 2025\Alzheimer-s-Disease-Classification\web app screenshort\Screenshot 2025-05-04 034022.png)
*The main assessment form with input fields for patient data*

### Assessment Form
![Assessment Form](sE:\edge project 2025\Alzheimer-s-Disease-Classification\web app screenshort\Screenshot 2025-05-04 034034.png)
*Detailed form with all medical parameters and their valid ranges*

### Results Page
![Results Page](E:\edge project 2025\Alzheimer-s-Disease-Classification\web app screenshort\Screenshot 2025-05-04 034043.png)
*Prediction results with confidence level and detailed patient information*

### PDF Report
![PDF Report](E:\edge project 2025\Alzheimer-s-Disease-Classification\web app screenshort\Screenshot 2025-05-04 034437.png)
*Professional PDF report with assessment results and patient details*

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd Alzheimer-s-Disease-Classification
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install wkhtmltopdf for PDF generation:
- Download from: https://wkhtmltopdf.org/downloads.html
- Install the Windows 64-bit version
- Use the default installation path

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Fill out the assessment form with patient data:
- Age (10-100 years)
- BMI (15-40 kg/m²)
- Physical Activity Level (1-10 scale)
- Sleep Quality (1-10 scale)
- Systolic Blood Pressure (90-200 mmHg)
- Total Cholesterol (100-300 mg/dL)
- HDL Cholesterol (20-100 mg/dL)
- MMSE Score (0-30)
- Functional Assessment (1-10 scale)
- ADL Score (1-10 scale)

4. Click "Assess Risk" to get the prediction

5. Click "Print Report" to generate a PDF report

## Model Information

The system uses a Random Forest classifier trained on medical data to predict Alzheimer's disease risk. The model considers various medical parameters and provides a confidence level for the prediction.

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- pandas
- numpy
- joblib
- pdfkit
- wkhtmltopdf

## License

This project is licensed under the MIT License - see the LICENSE file for details.
