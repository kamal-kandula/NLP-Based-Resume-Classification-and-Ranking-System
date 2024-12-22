# src/ranking.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def load_data():
    resumes_df = pd.read_csv('../data/preprocessed_resumes.csv')
    jobs_df = pd.read_csv('../data/preprocessed_jobs.csv')
    resume_features = joblib.load('../models/resume_features.pkl')
    job_features = joblib.load('../models/job_features.pkl')
    return resumes_df, jobs_df, resume_features, job_features

def load_model():
    vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')
    return vectorizer

def rank_resumes(resumes_df, jobs_df, resume_features, job_features):
    ranking_results = []
    for idx, job in jobs_df.iterrows():
        job_id = job['job_id']
        job_vector = job_features[idx]
        # Compute cosine similarity
        similarities = cosine_similarity(resume_features, job_vector)
        # Get similarity scores
        scores = similarities.flatten()
        # Create a DataFrame for sorting
        temp_df = resumes_df.copy()
        temp_df['similarity'] = scores
        # Sort resumes by similarity
        ranked_df = temp_df.sort_values(by='similarity', ascending=False)
        ranked_df['rank'] = range(1, len(ranked_df) + 1)
        # Add job_id to the results
        ranked_df['job_id'] = job_id
        # Select relevant columns
        ranked_df = ranked_df[['job_id', 'filename', 'similarity', 'rank']]
        ranking_results.append(ranked_df)
        print(f"Ranked resumes for {job_id}")
    # Concatenate all results
    final_ranking = pd.concat(ranking_results, ignore_index=True)
    return final_ranking

def main():
    # Load data and models
    resumes_df, jobs_df, resume_features, job_features = load_data()
    ranking = rank_resumes(resumes_df, jobs_df, resume_features, job_features)
    # Save ranking results
    ranking.to_csv('../results/ranking_scores.csv', index=False)
    print("Saved ranking scores.")

if __name__ == "__main__":
    main()
