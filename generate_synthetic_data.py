# src/generate_synthetic_data.py

import pandas as pd
from faker import Faker
import random
import uuid

fake = Faker()

# Predefined lists for more diverse data generation
JOB_TITLES = [
    'Software Engineer', 'Data Scientist', 'Product Manager', 'Business Analyst',
    'DevOps Engineer', 'UX/UI Designer', 'Machine Learning Engineer',
    'Quality Assurance Engineer', 'Technical Support Specialist', 'Database Administrator',
    'Cybersecurity Analyst', 'Network Engineer', 'Mobile App Developer',
    'Cloud Solutions Architect', 'Full Stack Developer', 'AI Researcher',
    'System Administrator', 'IT Project Manager', 'Business Intelligence Analyst',
    'Frontend Developer', 'Backend Developer', 'Data Engineer', 'Scrum Master',
    'Technical Writer', 'Salesforce Developer', 'Big Data Analyst'
]

DEPARTMENTS = [
    'Engineering', 'Data Science', 'Product', 'Business Intelligence', 'Quality Assurance',
    'IT Support', 'Human Resources', 'Marketing', 'Sales', 'Customer Success',
    'Research and Development', 'Cybersecurity', 'Operations', 'Finance', 'Legal',
    'Design', 'DevOps', 'Network Administration', 'Mobile Development', 'Cloud Services'
]

SKILLS = [
    'Python', 'Java', 'SQL', 'Machine Learning', 'NLP', 'Data Visualization', 'C++',
    'R', 'TensorFlow', 'Keras', 'React', 'Angular', 'Django', 'Flask', 'AWS',
    'Azure', 'Docker', 'Kubernetes', 'Git', 'Jenkins', 'Scrum', 'Agile Methodologies',
    'Public Speaking', 'Project Management', 'Communication', 'Leadership',
    'Problem Solving', 'Time Management', 'Critical Thinking', 'Attention to Detail',
    'Adobe Photoshop', 'Adobe Illustrator', 'Figma', 'User Research', 'A/B Testing',
    'Tableau', 'Power BI', 'NoSQL', 'Linux', 'Windows Server', 'Network Security',
    'Penetration Testing', 'API Development', 'Microservices', 'Blockchain',
    'IoT Development', 'Robotic Process Automation', 'E-commerce Platforms',
    'SEO Optimization', 'Content Management Systems'
]

EDUCATION_DEGREES = [
    'B.Sc.', 'M.Sc.', 'B.A.', 'MBA', 'Ph.D.', 'B.Tech', 'M.Tech', 'BBA',
    'MFA', 'B.E.', 'M.E.', 'BCom', 'MCom', 'BA in Economics', 'MA in Psychology'
]

EDUCATION_MAJORS = [
    'Computer Science', 'Data Science', 'Business Administration', 'Electrical Engineering',
    'Mechanical Engineering', 'Information Technology', 'Finance', 'Marketing',
    'Psychology', 'Economics', 'Graphic Design', 'Mechanical Engineering',
    'Biomedical Engineering', 'Civil Engineering', 'Chemical Engineering',
    'Industrial Engineering', 'Environmental Science', 'Statistics', 'Mathematics',
    'Physics', 'Chemistry', 'Biology', 'Linguistics', 'Sociology', 'Political Science'
]

EMPLOYMENT_TYPES = [
    'Full-time', 'Part-time', 'Contract', 'Internship', 'Temporary', 'Freelance',
    'Remote', 'On-site', 'Hybrid'
]

LOCATIONS = [
    'New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Seattle',
    'Austin', 'Denver', 'Atlanta', 'Miami', 'Dallas', 'Washington D.C.', 'Boston',
    'Houston', 'Phoenix', 'Philadelphia', 'San Diego', 'Portland', 'San Jose',
    'Orlando'
]

RESPONSIBILITIES_TEMPLATES = [
    'Develop and maintain {title} applications using {skills}.',
    'Collaborate with cross-functional teams to define, design, and ship new features.',
    'Ensure the performance, quality, and responsiveness of applications.',
    'Identify and correct bottlenecks and fix bugs.',
    'Help maintain code quality, organization, and automatization.',
    'Participate in code reviews and contribute to team knowledge sharing.',
    'Implement security and data protection measures.',
    'Continuously discover, evaluate, and implement new technologies to maximize development efficiency.',
    'Translate user requirements into technical specifications.',
    'Design and implement scalable software solutions.'
]

REQUIREMENTS_TEMPLATES = [
    'Bachelor’s degree in {major} or related field.',
    'Proven experience as a {title} or similar role.',
    'Familiarity with {skills}.',
    'Strong problem-solving skills and attention to detail.',
    'Excellent verbal and written communication skills.',
    'Ability to work independently and in a team environment.',
    'Experience with Agile methodologies.',
    'Knowledge of software design and programming principles.',
    'Proven experience with {skills}.',
    'Strong understanding of databases and data structures.'
]

def generate_resume():
    # Select random attributes
    title = random.choice(JOB_TITLES)
    department = random.choice(DEPARTMENTS)
    skills = random.sample(SKILLS, 6)
    degree = random.choice(EDUCATION_DEGREES)
    major = random.choice(EDUCATION_MAJORS)
    employment_type = random.choice(EMPLOYMENT_TYPES)
    location = random.choice(LOCATIONS)
    
    # Generate education and experience details
    education = f"{degree} in {major} from {fake.university()}"
    experience = f"{random.randint(1, 10)} years at {fake.company()} as {title}"
    
    resume = {
        'resume_id': str(uuid.uuid4()),
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'education': education,
        'experience': experience,
        'skills': ', '.join(skills),
        'additional_info': fake.text(max_nb_chars=200),
        'job_id': random.randint(100, 150)  # Adjust range as needed
    }
    return resume

def generate_job_description():
    # Select random attributes
    title = random.choice(JOB_TITLES)
    department = random.choice(DEPARTMENTS)
    employment_type = random.choice(EMPLOYMENT_TYPES)
    location = random.choice(LOCATIONS)
    
    # Generate responsibilities and requirements
    responsibilities = ' '.join(random.choices(RESPONSIBILITIES_TEMPLATES, k=3)).format(
        title=title,
        skills=', '.join(random.sample(SKILLS, 3))
    )
    requirements = ' '.join(random.choices(REQUIREMENTS_TEMPLATES, k=2)).format(
        major=random.choice(EDUCATION_MAJORS),
        title=title,
        skills=', '.join(random.sample(SKILLS, 2))
    )
    
    job = {
        'job_id': random.randint(100, 150),  # Ensure job_id consistency
        'title': title,
        'department': department,
        'responsibilities': responsibilities,
        'requirements': requirements,
        'location': location,
        'employment_type': employment_type
    }
    return job

def generate_resumes(num_resumes: int) -> pd.DataFrame:
    resumes = [generate_resume() for _ in range(num_resumes)]
    return pd.DataFrame(resumes)

def generate_jobs(num_jobs: int) -> pd.DataFrame:
    jobs = [generate_job_description() for _ in range(num_jobs)]
    # Ensure unique job_ids
    jobs_df = pd.DataFrame(jobs).drop_duplicates(subset=['job_id']).reset_index(drop=True)
    return jobs_df

def main():
    # Parameters
    NUM_RESUMES = 5000  # Increased number for more data
    NUM_JOBS = 50        # Increased number of job descriptions
    
    # Generate data
    print("Generating synthetic resumes...")
    resumes_df = generate_resumes(NUM_RESUMES)
    print(f"Generated {len(resumes_df)} synthetic resumes.")
    
    print("Generating synthetic job descriptions...")
    jobs_df = generate_jobs(NUM_JOBS)
    print(f"Generated {len(jobs_df)} synthetic job descriptions.")
    
    # Save to CSV
    resumes_df.to_csv('../data/Resume_Data.csv', index=False)
    jobs_df.to_csv('../data/Job_Desc_Data.csv', index=False)
    print("Saved synthetic data to data/ directory.")

if __name__ == "__main__":
    main()
