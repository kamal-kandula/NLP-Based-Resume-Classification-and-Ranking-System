import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def load_model():
    # Resolve paths dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vectorizer_path = os.path.join(script_dir, '../models/tfidf_vectorizer.pkl')

    # Check if file exists
    if not os.path.exists(vectorizer_path):
        raise FileNotFoundError(f"File not found: {vectorizer_path}")

    # Load vectorizer
    vectorizer = joblib.load(vectorizer_path)
    return vectorizer

def load_resumes(resumes_df, resumes_folder):
    # Read content of each file into a new column
    resume_texts = []
    for filename in resumes_df['filename']:
        file_path = os.path.join(resumes_folder, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                resume_texts.append(f.read())
        else:
            raise FileNotFoundError(f"Resume file not found: {file_path}")

    # Add the resume text content to the DataFrame
    resumes_df['resume_text'] = resume_texts
    return resumes_df

def load_data():
    # Resolve paths dynamically
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    resumes_path = os.path.join(project_root, 'data', 'preprocessed_resumes.csv')
    jobs_path = os.path.join(project_root, 'data', 'preprocessed_jobs.csv')
    resumes_folder = os.path.join(project_root, 'data', 'resumes')

    # Check if files exist
    if not os.path.exists(resumes_path):
        raise FileNotFoundError(f"File not found: {resumes_path}")
    if not os.path.exists(jobs_path):
        raise FileNotFoundError(f"File not found: {jobs_path}")
    if not os.path.exists(resumes_folder):
        raise FileNotFoundError(f"Resumes folder not found: {resumes_folder}")

    # Load datasets
    resumes_df = pd.read_csv(resumes_path)
    jobs_df = pd.read_csv(jobs_path)

    # Load resume content
    resumes_df = load_resumes(resumes_df, resumes_folder)

    # Load the vectorizer
    vectorizer = load_model()

    # Transform resumes and jobs using the same vectorizer
    resume_features = vectorizer.transform(resumes_df['resume_text'])
    job_features = vectorizer.transform(jobs_df['text'])

    return resumes_df, jobs_df, resume_features, job_features

def rank_resumes(resumes_df, jobs_df, resume_features, job_features):
    ranking_results = []

    for idx, job in jobs_df.iterrows():
        job_id = job['job_id']

        # Ensure job_vector is correctly reshaped
        job_vector = job_features[idx].reshape(1, -1)

        # Validate dimensions
        if resume_features.shape[1] != job_vector.shape[1]:
            raise ValueError(f"Dimension mismatch: Resume features ({resume_features.shape[1]}) vs Job features ({job_vector.shape[1]})")

        # Compute cosine similarity
        similarities = cosine_similarity(resume_features, job_vector)
        scores = similarities.flatten()

        # Prepare ranking DataFrame
        temp_df = resumes_df.copy()
        temp_df['similarity'] = scores
        ranked_df = temp_df.sort_values(by='similarity', ascending=False)
        ranked_df['rank'] = range(1, len(ranked_df) + 1)
        ranked_df['job_id'] = job_id
        ranked_df = ranked_df[['job_id', 'filename', 'similarity', 'rank']]

        ranking_results.append(ranked_df)
        print(f"Ranked resumes for job_id: {job_id}")

    final_ranking = pd.concat(ranking_results, ignore_index=True)
    return final_ranking

def main():
    try:
        # Load data and models
        resumes_df, jobs_df, resume_features, job_features = load_data()

        # Rank resumes
        ranking = rank_resumes(resumes_df, jobs_df, resume_features, job_features)

        # Save ranking results
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(script_dir, '../results')
        os.makedirs(results_dir, exist_ok=True)
        ranking_path = os.path.join(results_dir, 'ranking_scores.csv')
        ranking.to_csv(ranking_path, index=False)

        print(f"Saved ranking scores to {ranking_path}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
