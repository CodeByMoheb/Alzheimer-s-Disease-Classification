# Alzheimer's Disease Classification Project

## Project Overview
This project implements a machine learning model for Alzheimer's disease prediction using patient health data. The system includes a Flask web application for risk assessment and prediction.

## Features
- Machine learning model for Alzheimer's disease prediction
- Web-based risk assessment interface
- Detailed patient reports
- Feature importance analysis
- Model performance visualization

## Screenshots

### Web Application Interface
![Web App Screenshot 1](web%20app%20screenshort/Screenshot%202025-05-04%20034022.png)
![Web App Screenshot 2](web%20app%20screenshort/Screenshot%202025-05-04%20034034.png)
![Web App Screenshot 3](web%20app%20screenshort/Screenshot%202025-05-04%20034043.png)
![Web App Screenshot 4](web%20app%20screenshort/Screenshot%202025-05-04%20034437.png)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/CodeByMoheb/Alzheimer-s-Disease-Classification.git
cd Alzheimer-s-Disease-Classification
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install wkhtmltopdf for report generation:
- Download from: https://wkhtmltopdf.org/downloads.html
- Install the downloaded executable

## Usage
1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter patient information and get predictions

## Model Details
The project uses a Random Forest classifier trained on the following features:
- Age
- BMI
- Physical Activity Level
- Sleep Quality
- Systolic Blood Pressure
- Cholesterol Levels
- MMSE Score
- Functional Assessment
- Activities of Daily Living (ADL)

## License
This project is licensed under the MIT License - see the LICENSE file for details. 