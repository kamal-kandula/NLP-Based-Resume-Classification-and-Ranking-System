# src/preprocessing.py

import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from utils import load_resumes, load_job_descriptions
import os

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words('english'))
STEMMER = SnowballStemmer('english')
LEMMATIZER = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize
    tokens = nltk.word_tokenize(text)
    # Remove stopwords and apply lemmatization
    tokens = [LEMMATIZER.lemmatize(word) for word in tokens if word not in STOPWORDS]
    return ' '.join(tokens)

def preprocess_resumes(resume_dir: str) -> pd.DataFrame:
    absolute_resume_dir = os.path.abspath(resume_dir)
    print(f"Attempting to load resumes from: {absolute_resume_dir}")
    texts, filenames = load_resumes(resume_dir)
    processed_texts = [preprocess_text(text) for text in texts]
    df = pd.DataFrame({'filename': filenames, 'text': processed_texts})
    return df

def preprocess_job_descriptions(jobs_csv_path: str) -> pd.DataFrame:
    """
    Preprocesses job descriptions from a CSV file.

    Args:
        jobs_csv_path (str): Path to the Jobs_Data.csv file.

    Returns:
        pd.DataFrame: DataFrame containing job_id and preprocessed text.
    """
    try:
        jobs_df = load_job_descriptions(jobs_csv_path)
        print(f"Preprocessed {len(jobs_df)} job descriptions.")
        return jobs_df
    except Exception as e:
        print(f"Error preprocessing job descriptions: {e}")
        raise e

def extract_features(texts: pd.Series, max_features: int = 5000) -> TfidfVectorizer:
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(texts)
    return vectorizer, X

def main():
    # Absolute Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    resume_dir = os.path.join(project_root, 'data', 'resumes')
    jobs_csv_path = os.path.join(project_root, 'data', 'Jobs_Data.csv')

    # Preprocess resumes
    resumes_df = preprocess_resumes(resume_dir)
    print(f"Preprocessed {len(resumes_df)} resumes.")

    # Assign labels (enhanced)
    resumes_df['label'] = resumes_df['filename'].apply(lambda x: x.split('_')[0] if '_' in x else 'Unknown')
    
    # Optionally, inspect a sample
    print("Sample labels:")
    print(resumes_df[['filename', 'label']].head())

    # Optionally, remove 'Unknown' labels or handle them appropriately
    # For example:
    # resumes_df = resumes_df[resumes_df['label'] != 'Unknown']

    # Preprocess job descriptions
    jobs_df = preprocess_job_descriptions(jobs_csv_path)
    print(f"Preprocessed {len(jobs_df)} job descriptions.")

    # Feature extraction for resumes
    vectorizer, X = extract_features(resumes_df['text'])
    job_vectorizer, X_jobs = extract_features(jobs_df['text'])

    # Ensure 'models/' directory exists
    models_dir = os.path.join(project_root, 'models')
    os.makedirs(models_dir, exist_ok=True)

    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Save the vectorizer and features
    joblib.dump(vectorizer, os.path.join(models_dir, 'tfidf_vectorizer.pkl'))
    print("Saved TF-IDF vectorizer.")

    # Save preprocessed data
    resumes_df.to_csv(os.path.join(data_dir, 'preprocessed_resumes.csv'), index=False)
    jobs_df.to_csv(os.path.join(data_dir, 'preprocessed_jobs.csv'), index=False)
    joblib.dump(X, os.path.join(models_dir, 'resume_features.pkl'))
    joblib.dump(X_jobs, os.path.join(models_dir, 'job_features.pkl'))
    print("Saved preprocessed features.")

if __name__ == "__main__":
    main()
