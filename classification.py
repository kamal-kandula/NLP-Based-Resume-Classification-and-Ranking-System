import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report
import joblib
import os
from imblearn.over_sampling import RandomOverSampler


def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    preprocessed_resumes_path = os.path.join(project_root, 'data', 'preprocessed_resumes.csv')
    resume_features_path = os.path.join(project_root, 'models', 'resume_features.pkl')

    # Check if files exist
    if not os.path.exists(preprocessed_resumes_path):
        print(f"Error: File not found: {preprocessed_resumes_path}")
        exit(1)
    if not os.path.exists(resume_features_path):
        print(f"Error: File not found: {resume_features_path}")
        exit(1)

    # Load data
    resumes_df = pd.read_csv(preprocessed_resumes_path)
    X = joblib.load(resume_features_path)
    y = resumes_df['label']

    # Handle single-class scenario
    if len(y.unique()) == 1:
        print("Only one class detected in the dataset. Adding synthetic classes for testing.")
        # Add synthetic labels for testing
        import numpy as np
        np.random.seed(42)
        y = np.random.choice(['Class1', 'Class2'], size=len(y))
    
    print(f"Data loaded successfully: {X.shape[0]} samples, {X.shape[1]} features, {len(y)} labels.")
    print(f"Label distribution after synthetic augmentation:\n{pd.Series(y).value_counts()}")
    return X, y


def train_naive_bayes(X_train, y_train):
    print("Training Naive Bayes...")
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    print("Naive Bayes training completed.")
    return nb


def train_random_forest(X_train, y_train):
    print("Training Random Forest...")
    rf = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    grid_rf = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_rf.fit(X_train, y_train)
    print(f"Random Forest training completed. Best params: {grid_rf.best_params_}")
    return grid_rf.best_estimator_


def train_gradient_boosting(X_train, y_train):
    print("Training Gradient Boosting...")
    gb = GradientBoostingClassifier(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'learning_rate': [0.1, 0.05],
        'max_depth': [3, 5]
    }
    grid_gb = GridSearchCV(gb, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    try:
        grid_gb.fit(X_train, y_train)
        print(f"Gradient Boosting training completed. Best params: {grid_gb.best_params_}")
        return grid_gb.best_estimator_
    except ValueError as e:
        print(f"Error during Gradient Boosting training: {e}")
        return None


def evaluate_model(model, X_test, y_test, model_name: str):
    print(f"Evaluating {model_name}...")
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    
    # Define project root and results directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    results_dir = os.path.join(project_root, 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    # Construct the report file path
    report_path = os.path.join(results_dir, f'{model_name}_classification_report.txt')
    
    # Save the report
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"{model_name} Classification Report:\n{report}")
    print(f"Classification report saved to {report_path}")


def balance_dataset(X_train, y_train):
    print("Balancing dataset...")
    oversampler = RandomOverSampler(random_state=42)
    X_train_balanced, y_train_balanced = oversampler.fit_resample(X_train, y_train)
    print("Dataset balanced. New class distribution:")
    print(pd.Series(y_train_balanced).value_counts())
    return X_train_balanced, y_train_balanced

def main():
    # Load data
    X, y = load_data()
    
    # Inspect label distribution
    print("Initial label distribution:")
    print(pd.Series(y).value_counts())
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Data split completed: {X_train.shape[0]} training samples, {X_test.shape[0]} test samples.")

    # Balance the dataset for training
    X_train, y_train = balance_dataset(X_train, y_train)

    # Train and evaluate models
    nb_model = train_naive_bayes(X_train, y_train)
    evaluate_model(nb_model, X_test, y_test, 'NaiveBayes')

    rf_model = train_random_forest(X_train, y_train)
    evaluate_model(rf_model, X_test, y_test, 'RandomForest')

    gb_model = train_gradient_boosting(X_train, y_train)
    if gb_model:
        evaluate_model(gb_model, X_test, y_test, 'GradientBoosting')
    else:
        print("Gradient Boosting model training encountered an issue and was skipped.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
