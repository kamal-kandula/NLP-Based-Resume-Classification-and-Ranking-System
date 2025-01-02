import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from preprocessing import NLPPreprocessor

# Load dataset
data = pd.read_csv("data/Resume_Data.csv")

# Preprocess text
preprocessor = NLPPreprocessor()
data["Processed_Text"] = data["Resume_Text"].apply(preprocessor.preprocess_text)

# Split data into training and test sets
X = data["Processed_Text"]
y = data["Category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Save vectorizer for later use
joblib.dump(vectorizer, "models/vectorizer.pkl")

# Define models to train
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
    "Support Vector Machine": SVC(kernel="linear", probability=True, random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", random_state=42),
}

# Train each model and evaluate performance
best_model = None
best_accuracy = 0

for model_name, model in models.items():
    print(f"\nTraining {model_name}...")
    model.fit(X_train_vec, y_train)
    
    # Save model
    model_file = f"models/{model_name.replace(' ', '_')}_model.pkl"
    joblib.dump(model, model_file)
    print(f"Saved {model_name} to {model_file}")

    # Evaluate the model
    y_pred = model.predict(X_test_vec)
    print(f"Classification Report for {model_name}:\n")
    print(classification_report(y_test, y_pred))

    # Track the best model
    accuracy = model.score(X_test_vec, y_test)
    if accuracy > best_accuracy:
        best_model = model
        best_accuracy = accuracy

# Save the best-performing model as the primary classification model
joblib.dump(best_model, "models/classification_model.pkl")
print(f"\nBest model saved as 'classification_model.pkl' with accuracy: {best_accuracy:.4f}")