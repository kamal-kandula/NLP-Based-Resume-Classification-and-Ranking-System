# NLP-Based Resume Classification and Ranking System

## Project Overview

The **NLP-Based Resume Classification and Ranking System** is an innovative solution designed to automate and enhance the recruitment process. By leveraging advanced Natural Language Processing (NLP) techniques and robust machine learning algorithms, this system efficiently parses, classifies, and ranks resumes, ensuring that recruiters can swiftly identify the most suitable candidates for specific job roles.

---

## Objectives

- **Automate Resume Parsing:** Efficiently extract relevant information from resumes in various formats (PDF, DOCX).
- **Classify Resumes:** Accurately categorize resumes into one of 20 predefined job roles using machine learning classifiers.
- **Rank Resumes:** Order resumes within each category based on their relevance and suitability for the job description.
- **Achieve High Accuracy:** Attain a classification accuracy of at least 74.4% and a ranking accuracy of 92.5%.

---

## Features

- **Multi-Format Support:** Handles resumes in PDF and DOCX formats.
- **Advanced Text Preprocessing:** Cleans and normalizes text data for optimal model performance.
- **Machine Learning Classification:** Utilizes Naive Bayes, Random Forest, and Gradient Boosting algorithms.
- **Effective Ranking Mechanism:** Employs TF-IDF and cosine similarity for accurate resume ranking.
- **Scalable Architecture:** Designed to handle large datasets with ease.
- **User-Friendly Repository Structure:** Organized for ease of navigation and maintenance.

---

## Technologies Used

- **Programming Language:** Python 3.7+
- **Libraries & Frameworks:**
  - [Scikit-learn](https://scikit-learn.org/)
  - [NLTK](https://www.nltk.org/)
  - [PDFMiner](https://github.com/pdfminer/pdfminer.six)
  - [python-docx](https://python-docx.readthedocs.io/)
  - [Joblib](https://joblib.readthedocs.io/)
- **Tools:**
  - Git & GitHub
  - Jupyter Notebook

---

## Dataset Description

The dataset comprises **2,208 resumes** collected from diverse sources, each corresponding to one of **20 distinct job descriptions**. Resumes are provided in formats such as PDF and DOCX, containing sections like personal information, education, work experience, skills, and certifications.

### Data Collection

- **Sources:** Public repositories, job portals, and synthetic data generation.
- **Formats:** PDF, DOCX, and plain text files.
- **Categories:** 20 job roles including Software Engineer, Data Scientist, Product Manager, etc.

---

## System Architecture

The system is divided into two main components:

1. **Classification Module:** Utilizes machine learning algorithms to categorize resumes into predefined job roles.
2. **Ranking Module:** Employs text similarity techniques to rank resumes within each category based on their relevance to the job description.

---

## Installation

### Prerequisites

- **Python 3.7+** installed on your machine.
- **Git** installed for version control.
- **pip** package manager.

## Usage

### 1. Data Preparation
Resumes: Place all resume files (PDF and DOCX) in the data/resumes/ directory.
Job Descriptions: Place all job description text files in the data/job_descriptions/ directory.

### 2. Preprocess Data
Execute the preprocessing script to clean the data and extract features.
python src/preprocessing.py

This script will:
Parse resumes and job descriptions.
Clean and normalize the text data.
Extract TF-IDF features.
Save the preprocessed data and vectorizers.

### 3. Train Classification Models
Train the classification models and evaluate their performance.
python src/classification.py

This script will:
Load preprocessed resume data.
Train Naive Bayes, Random Forest, and Gradient Boosting classifiers.
Evaluate models using accuracy, precision, recall, and F1-score.
Save the best-performing model (Random Forest).

### 4. Rank Resumes
Rank resumes based on their similarity to job descriptions.
python src/ranking.py

This script will:
Load preprocessed resumes and job descriptions.
Compute cosine similarity between resume and job vectors.
Rank resumes within each job category.
Save the ranking results to results/ranking_scores.csv.

### 5. View Results
Classification Reports: Located in the results/ directory as .txt files.
Ranking Scores: Located in results/ranking_scores.csv.

README.md: Project documentation.
requirements.txt: List of Python dependencies.

## Future Work
Deep Learning Models: Incorporate models like BERT for improved text understanding and classification.
Real-Time Processing: Develop a web application interface for real-time resume processing and ranking.
Feedback Loop: Implement mechanisms to refine rankings based on recruiter feedback and preferences.
Enhanced Feature Engineering: Explore additional NLP techniques such as named entity recognition (NER) and part-of-speech (POS) tagging to enrich feature sets.
Scalability Improvements: Optimize the system for handling larger datasets and integrating with cloud-based storage and computing resources.

