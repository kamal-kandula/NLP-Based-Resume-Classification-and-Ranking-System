# src/validate_data.py

import os
import pandas as pd
import logging

def validate_data():
    # Determine the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Set up logging
    log_directory = os.path.join(script_dir, '..', 'logs')
    os.makedirs(log_directory, exist_ok=True)
    logging.basicConfig(
        filename=os.path.join(log_directory, 'validate_data.log'),
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

    # Define data directory
    data_directory = os.path.join(script_dir, '..', 'data')

    # Define paths to CSV files
    resumes_csv = os.path.join(data_directory, 'Resume_Data.csv')
    jobs_csv = os.path.join(data_directory, 'Jobs_Data.csv')

    try:
        logging.info("Loading Resume_Data.csv and Jobs_Data.csv")
        resumes_df = pd.read_csv(resumes_csv)
        jobs_df = pd.read_csv(jobs_csv)

        logging.info("Validating that all job_ids in resumes correspond to jobs")
        missing_job_ids = set(resumes_df['job_id']) - set(jobs_df['job_id'])
        if missing_job_ids:
            logging.warning(f"Found resumes with non-existent job_ids: {missing_job_ids}")
            print(f"Warning: Found resumes with non-existent job_ids: {missing_job_ids}")
        else:
            logging.info("All resumes have valid job_ids.")
            print("All resumes have valid job_ids.")

        logging.info("Checking for duplicate job_ids in Jobs_Data.csv")
        duplicate_job_ids = jobs_df[jobs_df.duplicated('job_id', keep=False)]
        if not duplicate_job_ids.empty:
            logging.warning(f"Found duplicate job_ids in Jobs_Data.csv:\n{duplicate_job_ids}")
            print(f"Warning: Found duplicate job_ids in Jobs_Data.csv.")
            print(duplicate_job_ids)
        else:
            logging.info("No duplicate job_ids found in Jobs_Data.csv.")
            print("No duplicate job_ids found in Jobs_Data.csv.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"An error occurred during validation: {e}")
        print(f"An error occurred during validation: {e}")

def main():
    validate_data()

if __name__ == "__main__":
    main()