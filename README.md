# NLP-Based Resume Classification and Ranking System

## Project Overview

The **NLP-Based Resume Classification and Ranking System** is a cutting-edge solution aimed at automating the recruitment process. This system leverages advanced Natural Language Processing (NLP) techniques and robust machine learning algorithms to parse, classify, and rank resumes. By streamlining these tasks, the system ensures recruiters can efficiently identify the most suitable candidates for specific job roles.

---

## Objectives

- **Automate Resume Parsing:** Extract relevant information from resumes in PDF, DOCX, and plain text formats.
- **Classify Resumes:** Categorize resumes into one of 20 predefined job roles using advanced machine learning models.
- **Rank Resumes:** Rank resumes within each category based on their relevance and suitability for the job description.

---

## Features

- **Multi-Format Parsing:** Supports resume parsing for PDF, DOCX, and plain text files.
- **Advanced Text Preprocessing:** Tokenization, stopword removal, lemmatization, and TF-IDF vectorization.
- **Machine Learning Classification:** Includes models such as Logistic Regression, Random Forest, SVM, and XGBoost.
- **Ranking Mechanism:** Employs TF-IDF, cosine similarity, and optionally Sentence-BERT for ranking resumes.
- **Scalable and Modular Design:** Handles large datasets and is designed for extensibility.

---

## Technologies Used

- **Programming Language:** Python 3.7+
- **Libraries & Frameworks:** 
	- Scikit-learn: Machine learning algorithms.
	- NLTK: NLP preprocessing.
	- PDFMiner: Parsing PDF resumes.
	- python-docx: Parsing DOCX resumes.
	- Joblib: Model persistence.
	- Sentence-Transformers: Semantic similarity for ranking.
- **Tools:**
	- Git & GitHub: Version control.
	- Jupyter Notebook: For data analysis and visualization.

---

## Dataset Description

The dataset comprises **5,000 resumes** collected from diverse sources, each corresponding to one of **20 distinct job descriptions**. Resumes are provided in formats such as PDF and DOCX, containing sections like personal information, education, work experience, skills, and certifications.

### Data Collection

- **Sources:** Public repositories, job boards, and synthetic data generation.
- **Formats:** PDF, DOCX, and plain text files. **Job Descriptions:** Text files representing job requirements.
- **Categories:** 20 job roles ensuring diversity and relevance to real-world applications.

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

### Steps:
1. Clone the repository:
git clone https://github.com/kamal-kandula/NLP-Based-Resume-Classification-and-Ranking-System.git
cd NLP-Based-Resume-Classification-and-Ranking-System

2. Install dependencies:
pip install -r requirements.txt

## Usage

### 1. Data Preparation
- **Resumes:** Place all resume files in the data/resumes/ directory.
- **Job Descriptions:** Place all job description files in the data/job_descriptions/ directory.

### 2. Preprocess Data
Execute the preprocessing script to clean the data and extract features.
python src/preprocessing.py

**This script:**
- Parses resumes and job descriptions.
- Cleans and normalizes text data.
- Extracts TF-IDF features.

### 3. Train Classification Models
Train the classification models and evaluate their performance.
python src/classification.py

**This script:**
- Trains Logistic Regression, Random Forest, SVM, and XGBoost classifiers.
- Evaluates models using accuracy, precision, recall, and F1-score.
- Saves the best-performing model.

### 4. Rank Resumes
Rank resumes based on their relevance to job descriptions:
python src/ranking.py

**This script will:**
- Computes cosine similarity between resumes and job descriptions.
- Optionally uses Sentence-BERT for semantic ranking.
- Outputs results to results/ranking_scores.csv.

### 5. View Results
- **Classification Reports:** Stored in the results/ directory.
- **Ranking Scores:** Available in results/ranking_scores.csv.

- **README.md:** Project documentation.
- **requirements.txt:** List of Python dependencies.

---

## Future Work
- **Deep Learning Models:** Incorporate BERT and Sentence-BERT for advanced text classification and ranking.
- **Real-Time Interface:** Develop a web-based application for resume parsing and ranking.
- **Feedback Mechanisms:** Implement recruiter feedback loops to refine classification and ranking.
- **Advanced NLP Techniques:** Use Named Entity Recognition (NER) and Part-of-Speech (POS) tagging to enrich feature sets.
- **Scalability:** Optimize for large datasets and integrate with cloud-based storage and computation.

