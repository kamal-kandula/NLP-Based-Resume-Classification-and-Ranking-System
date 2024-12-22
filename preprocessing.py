# src/preprocessing.py

import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from utils import load_resumes, load_job_descriptions

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
    texts, filenames = load_resumes(resume_dir)
    processed_texts = [preprocess_text(text) for text in texts]
    df = pd.DataFrame({'filename': filenames, 'text': processed_texts})
    return df

def preprocess_job_descriptions(job_dir: str) -> pd.DataFrame:
    texts, filenames = load_job_descriptions(job_dir)
    processed_texts = [preprocess_text(text) for text in texts]
    df = pd.DataFrame({'job_id': filenames, 'text': processed_texts})
    return df

def extract_features(texts: pd.Series, max_features: int = 5000) -> TfidfVectorizer:
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(texts)
    return vectorizer, X

def main():
    # Paths
    resume_dir = '../data/resumes/'
    job_dir = '../data/job_descriptions/'

    # Preprocess resumes
    resumes_df = preprocess_resumes(resume_dir)
    print(f"Preprocessed {len(resumes_df)} resumes.")

    # Assuming you have labels for classification
    # For demonstration, let's create synthetic labels
    # In practice, you should have a separate file or metadata for labels
    # Example: Each resume filename starts with the job category, e.g., "SoftwareEngineer_resume1.pdf"
    resumes_df['label'] = resumes_df['filename'].apply(lambda x: x.split('_')[0])

    # Preprocess job descriptions
    jobs_df = preprocess_job_descriptions(job_dir)
    print(f"Preprocessed {len(jobs_df)} job descriptions.")

    # Feature extraction
    vectorizer, X = extract_features(resumes_df['text'])
    job_vectorizer, X_jobs = extract_features(jobs_df['text'])

    # Save the vectorizer
    joblib.dump(vectorizer, '../models/tfidf_vectorizer.pkl')
    print("Saved TF-IDF vectorizer.")

    # Save preprocessed data
    resumes_df.to_csv('../data/preprocessed_resumes.csv', index=False)
    jobs_df.to_csv('../data/preprocessed_jobs.csv', index=False)
    joblib.dump(X, '../models/resume_features.pkl')
    joblib.dump(X_jobs, '../models/job_features.pkl')
    print("Saved preprocessed features.")

if __name__ == "__main__":
    main()
