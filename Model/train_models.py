import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Selected 10 key features for Alzheimer's prediction
SELECTED_FEATURES = [
    'Age',
    'BMI',
    'PhysicalActivity',
    'SleepQuality',
    'SystolicBP',
    'CholesterolTotal',
    'CholesterolHDL',
    'MMSE',  # Mini-Mental State Examination
    'FunctionalAssessment',
    'ADL'  # Activities of Daily Living
]

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Select only the features we want to use
    X = df[SELECTED_FEATURES]
    y = df['Diagnosis']  # Assuming 'Diagnosis' is the target column
    
    # Handle missing values
    X = X.fillna(X.mean())
    
    return X, y

def train_models(X, y):
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=40, shuffle=True
    )
    
    # Define parameter grids
    param_grids = {
        'Decision Tree': {'max_depth': [3, 5, 7, None]},
        'Random Forest': {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 7, None]},
        'K-Nearest Neighbors': {'n_neighbors': [3, 5, 7]}
    }
    
    # Define models
    models = {
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'K-Nearest Neighbors': KNeighborsClassifier()
    }
    
    best_model = None
    best_accuracy = 0
    best_model_name = ""
    
    # Train and evaluate each model
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Perform grid search
        grid_search = GridSearchCV(
            model,
            param_grids[name],
            cv=5,
            scoring='f1',
            n_jobs=-1
        )
        
        # Fit the model
        grid_search.fit(X_train, y_train)
        
        # Get best model
        best_model_current = grid_search.best_estimator_
        
        # Make predictions
        y_pred = best_model_current.predict(X_test)
        
        # Evaluate
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        print(f"\n{name} Results:")
        print(f"Best Parameters: {grid_search.best_params_}")
        print(f"Accuracy: {accuracy:.4f}")
        print("\nClassification Report:")
        print(report)
        
        # Plot confusion matrix
        plot_confusion_matrix(y_test, y_pred, name)
        
        # Update best model if current model is better
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = best_model_current
            best_model_name = name
    
    return best_model, best_accuracy, best_model_name, X_test, y_test

def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix - {model_name}')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig(f'confusion_matrix_{model_name.lower().replace(" ", "_")}.png')
    plt.close()

def plot_feature_importance(model, feature_names, model_name):
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.figure(figsize=(10, 6))
        plt.title(f'Feature Importances - {model_name}')
        plt.bar(range(len(importances)), importances[indices])
        plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
        plt.tight_layout()
        plt.savefig(f'feature_importance_{model_name.lower().replace(" ", "_")}.png')
        plt.close()

def main():
    try:
        # Load and preprocess the data
        print("Loading data...")
        X, y = load_and_preprocess_data(r'E:\edge project 2025\Alzheimer-s-Disease-Classification\alzheimers_disease_data.csv')
        
        # Train models and get the best one
        best_model, best_accuracy, best_model_name, X_test, y_test = train_models(X, y)
        
        # Save the best model
        print(f"\nSaving best model ({best_model_name}) with accuracy: {best_accuracy:.4f}")
        joblib.dump(best_model, 'best_alzheimer_model.joblib')
        
        # Plot feature importance for the best model if it's a tree-based model
        if best_model_name in ['Decision Tree', 'Random Forest']:
            plot_feature_importance(best_model, SELECTED_FEATURES, best_model_name)
        
        print("Model saved successfully as 'best_alzheimer_model.joblib'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 