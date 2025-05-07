# 🧠 Alzheimer's Disease Classification System

## project demonstration video
https://youtu.be/IVfPNXIvBpY?si=Ct51ObT9cQ-Aqn28

<div align="center">
  <img src="web%20app%20screenshort/Screenshot%202025-05-04%20034022.png" alt="System Overview" width="800"/>
</div>

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [Installation Guide](#installation-guide)
- [Usage Instructions](#usage-instructions)
- [Model Details](#model-details)
- [Performance Metrics](#performance-metrics)
- [Contributing](#contributing)
- [License](#license)

  
## project demonstration video

https://youtu.be/IVfPNXIvBpY?si=Ct51ObT9cQ-Aqn28

## 🎯 Project Overview
This project implements an advanced machine learning system for early detection and risk assessment of Alzheimer's disease. The system combines state-of-the-art machine learning algorithms with a user-friendly web interface to provide accurate predictions and detailed patient reports.

### Problem Statement
Alzheimer's disease is a progressive neurodegenerative disorder that affects millions worldwide. Early detection is crucial for effective intervention and treatment planning. This system aims to assist healthcare professionals in making informed decisions by providing data-driven insights.

### Solution
Our solution leverages machine learning to analyze various health indicators and predict the likelihood of Alzheimer's disease. The system provides:
- Real-time risk assessment
- Detailed patient reports
- Feature importance analysis
- Visual data representation

## ✨ Key Features
- **Advanced ML Model**: Utilizes Random Forest algorithm with optimized hyperparameters
- **Web Interface**: Professional, hospital-style web application for easy data entry
- **Comprehensive Reports**: Detailed PDF reports with risk assessment and recommendations
- **Data Visualization**: Interactive charts and graphs for better understanding
- **Feature Analysis**: Identifies key factors contributing to the prediction
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🏗️ Technical Architecture

### Backend
- **Framework**: Flask (Python)
- **ML Library**: scikit-learn
- **Data Processing**: pandas, numpy
- **Report Generation**: pdfkit, wkhtmltopdf

### Frontend
- **UI Framework**: Bootstrap 5
- **Animations**: Animate.css
- **Responsive Design**: Mobile-first approach
- **Interactive Elements**: Dynamic form validation

### Data Processing Pipeline
1. Data Collection
2. Feature Engineering
3. Model Training
4. Prediction Generation
5. Report Creation

## 🚀 Installation Guide

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual Environment
- wkhtmltopdf

### Step-by-Step Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/CodeByMoheb/Alzheimer-s-Disease-Classification.git
   cd Alzheimer-s-Disease-Classification
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install wkhtmltopdf**
   - Download from: [wkhtmltopdf Downloads](https://wkhtmltopdf.org/downloads.html)
   - Follow installation instructions for your OS

## 💻 Usage Instructions

### Starting the Application
1. **Activate Virtual Environment**
   ```bash
   .venv\Scripts\activate  # On Windows
   ```

2. **Run the Flask Application**
   ```bash
   python app.py
   ```

3. **Access the Web Interface**
   - Open your browser
   - Navigate to: `http://localhost:5000`

### Using the System
1. Enter patient information in the assessment form
2. Submit the form for analysis
3. View the prediction results
4. Generate and download the detailed report

## 🔍 Model Details

### Features Used
- **Demographic Data**
  - Age
  - Gender
  - Education Level

- **Physical Health**
  - BMI
  - Physical Activity Level
  - Sleep Quality
  - Systolic Blood Pressure

- **Biochemical Markers**
  - Cholesterol Levels (Total, HDL)
  - Triglycerides

- **Cognitive Assessment**
  - MMSE Score
  - Functional Assessment
  - Activities of Daily Living (ADL)

### Model Architecture
- **Algorithm**: Random Forest Classifier
- **Hyperparameters**:
  - n_estimators: 200
  - max_depth: None
  - min_samples_split: 2
  - min_samples_leaf: 1

## 📊 Performance Metrics
- **Accuracy**: 95.2%
- **Precision**: 94.8%
- **Recall**: 95.5%
- **F1-Score**: 95.1%
- **ROC-AUC**: 0.98

## 🤝 Contributing
We welcome contributions to this project! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request



## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any questions or suggestions, please contact:
- Email: mohebullah.cse@gmail.com
- GitHub: [@CodeByMoheb](https://github.com/CodeByMoheb)

---

<div align="center">
  <p>Made with ❤️ by CodeByMoheb</p>
</div> 
