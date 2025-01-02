import pandas as pd
from faker import Faker
import random

def generate_resumes(num_resumes=100):
    """Generate synthetic resume data."""
    fake = Faker()
    roles = [
        "Data Scientist", "Software Engineer", "Product Manager", "Data Analyst",
        "Project Manager", "Business Analyst", "DevOps Engineer", "UX/UI Designer",
        "Digital Marketing Specialist", "Human Resources Manager", "Finance Manager",
        "Operations Manager", "Machine Learning Engineer", "Quality Assurance Engineer",
        "Technical Writer", "Customer Success Manager", "Network Administrator",
        "Web Developer", "Cloud Solutions Architect", "Graphic Designer"
    ]
    resumes = []

    for _ in range(num_resumes):
        role = random.choice(roles)
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        summary = fake.sentence(nb_words=20)
        skills = ", ".join(fake.words(nb=5))
        experience = f"{fake.job()} at {fake.company()} ({fake.date()} - {fake.date()})"
        education = f"{fake.degree()} from {fake.university()} ({fake.year()})"

        resume_text = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Professional Summary: {summary}\n"
            f"Skills: {skills}\n"
            f"Experience: {experience}\n"
            f"Education: {education}\n"
        )
        resumes.append({"Resume_Text": resume_text, "Category": role})

    return pd.DataFrame(resumes)

# Generate synthetic resumes
num_resumes = 5000  # Adjust this number to your requirement
resume_data = generate_resumes(num_resumes)

# Save to CSV
resume_data.to_csv("data/Resume_Data.csv", index=False)
print(f"{num_resumes} synthetic resumes saved to 'data/Resume_Data.csv'")
