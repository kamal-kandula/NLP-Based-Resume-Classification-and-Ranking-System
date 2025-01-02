from sklearn.metrics.pairwise import cosine_similarity
import joblib
from sentence_transformers import SentenceTransformer

class ResumeRanker:
    def __init__(self):
        # Load TF-IDF vectorizer and pre-trained Sentence-BERT model
        self.vectorizer = joblib.load("models/vectorizer.pkl")
        self.sbert_model = SentenceTransformer("all-mpnet-base-v2")

    def rank_resumes_tfidf(self, job_description, resumes):
        """Rank resumes using TF-IDF and cosine similarity."""
        corpus = [job_description] + resumes
        tfidf_matrix = self.vectorizer.transform(corpus)
        similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
        return similarity_scores.argsort()[::-1], similarity_scores.flatten()

    def rank_resumes_sbert(self, job_description, resumes):
        """Rank resumes using SBERT embeddings and cosine similarity."""
        embeddings = self.sbert_model.encode([job_description] + resumes)
        similarity_scores = cosine_similarity([embeddings[0]], embeddings[1:]).flatten()
        return similarity_scores.argsort()[::-1], similarity_scores

    def hybrid_ranking(self, job_description, resumes, classification_scores=None):
        """
        Hybrid ranking: combines SBERT and TF-IDF scores.
        Optionally incorporates classification scores.
        """
        # Compute TF-IDF and SBERT similarity scores
        _, tfidf_scores = self.rank_resumes_tfidf(job_description, resumes)
        _, sbert_scores = self.rank_resumes_sbert(job_description, resumes)

        # Normalize scores
        tfidf_scores = tfidf_scores / tfidf_scores.max()
        sbert_scores = sbert_scores / sbert_scores.max()

        # Combine scores
        combined_scores = 0.5 * tfidf_scores + 0.5 * sbert_scores
        if classification_scores is not None:
            classification_scores = classification_scores / classification_scores.max()
            combined_scores += 0.3 * classification_scores

        return combined_scores.argsort()[::-1], combined_scores