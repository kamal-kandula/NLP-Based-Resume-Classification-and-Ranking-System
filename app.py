import streamlit as st
import joblib
from src.preprocessing import NLPPreprocessor
from src.ranking import ResumeRanker

# Load pre-trained models
clf = joblib.load('models/classification_model.pkl')
ranker = ResumeRanker()

st.title("NLP-Based Resume Classification and Ranking")

uploaded_files = st.file_uploader("Upload Resumes (TXT format)", accept_multiple_files=True)
job_desc = st.text_area("Enter Job Description")

if st.button("Process"):
    preprocessor = NLPPreprocessor()
    resumes = [preprocessor.preprocess_text(file.read().decode("utf-8")) for file in uploaded_files]
    classifications = [clf.predict(ranker.vectorizer.transform([resume]))[0] for resume in resumes]
    ranked_indices = ranker.rank_resumes(job_desc, resumes)

    st.write("### Classification Results:")
    for i, classification in enumerate(classifications):
        st.write(f"Resume {i + 1}: {classification}")

    st.write("### Ranked Resumes:")
    for rank, idx in enumerate(ranked_indices, 1):
        st.write(f"Rank {rank}: Resume {idx + 1}")