# src/utils.py

import os
import pandas as pd

def load_resumes(resume_dir: str):
    """
    Loads resume texts and their filenames from the specified directory.

    Args:
        resume_dir (str): Path to the resumes directory.

    Returns:
        tuple: A tuple containing two lists:
            - texts (list): List of resume texts.
            - filenames (list): List of resume filenames.
    """
    texts = []
    filenames = []
    try:
        for filename in os.listdir(resume_dir):
            file_path = os.path.join(resume_dir, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    texts.append(text)
                    filenames.append(filename)
    except Exception as e:
        print(f"Error loading resumes: {e}")
        raise e
    return texts, filenames

def load_job_descriptions(jobs_csv_path: str):
    """
    Loads and combines job descriptions from a CSV file.

    Args:
        jobs_csv_path (str): Path to the Jobs_Data.csv file.

    Returns:
        pd.DataFrame: DataFrame containing job_id and combined text.
    """
    try:
        if os.path.isfile(jobs_csv_path):
            jobs_df = pd.read_csv(jobs_csv_path)
            # Combine relevant fields into a single text column
            jobs_df['text'] = jobs_df['title'].astype(str) + ' ' + \
                               jobs_df['responsibilities'].astype(str) + ' ' + \
                               jobs_df['requirements'].astype(str)
            return jobs_df[['job_id', 'text']]
        else:
            print(f"Jobs CSV file not found at {jobs_csv_path}")
            raise FileNotFoundError(f"Jobs CSV file not found at {jobs_csv_path}")
    except Exception as e:
        print(f"Error loading job descriptions: {e}")
        raise e
