# src/utils.py

import os
import re
from typing import List
from pdfminer.high_level import extract_text
from docx import Document

def load_resumes(resume_dir: str) -> List[str]:
    resume_texts = []
    filenames = []
    for filename in os.listdir(resume_dir):
        file_path = os.path.join(resume_dir, filename)
        if filename.lower().endswith('.pdf'):
            try:
                text = extract_text(file_path)
                resume_texts.append(text)
                filenames.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        elif filename.lower().endswith('.docx'):
            try:
                doc = Document(file_path)
                text = '\n'.join([para.text for para in doc.paragraphs])
                resume_texts.append(text)
                filenames.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return resume_texts, filenames

def load_job_descriptions(job_dir: str) -> List[str]:
    job_texts = []
    filenames = []
    for filename in os.listdir(job_dir):
        file_path = os.path.join(job_dir, filename)
        if filename.lower().endswith('.txt'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    job_texts.append(text)
                    filenames.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return job_texts, filenames
