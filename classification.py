# src/classification.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
import joblib

def load_data():
    resumes_df = pd.read_csv('../data/preprocessed_resumes.csv')
    X = joblib.load('../models/resume_features.pkl')
    y = resumes_df['label']
    return X, y

def train_naive_bayes(X_train, y_train):
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    return nb

def train_random_forest(X_train, y_train):
    rf = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    grid_rf = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_rf.fit(X_train, y_train)
    print(f"Best Random Forest Params: {grid_rf.best_params_}")
    return grid_rf.best_estimator_

def train_gradient_boosting(X_train, y_train):
    gb = GradientBoostingClassifier(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'learning_rate': [0.1, 0.05],
        'max_depth': [3, 5]
    }
    grid_gb = GridSearchCV(gb, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_gb.fit(X_train, y_train)
    print(f"Best Gradient Boosting Params: {grid_gb.best_params_}")
    return grid_gb.best_estimator_

def evaluate_model(model, X_test, y_test, model_name: str):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    with open(f'../results/{model_name}_classification_report.txt', 'w') as f:
        f.write(report)
    print(f"{model_name} Classification Report:\n{report}")

def main():
    # Load data
    X, y = load_data()

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train models
    print("Training Naive Bayes...")
    nb_model = train_naive_bayes(X_train, y_train)
    evaluate_model(nb_model, X_test, y_test, 'NaiveBayes')

    print("Training Random Forest...")
    rf_model = train_random_forest(X_train, y_train)
    evaluate_model(rf_model, X_test, y_test, 'RandomForest')

    print("Training Gradient Boosting...")
    gb_model = train_gradient_boosting(X_train, y_train)
    evaluate_model(gb_model, X_test, y_test, 'GradientBoosting')

if __name__ == "__main__":
    main()
