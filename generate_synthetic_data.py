# src/generate_synthetic_data.py

import os
import pandas as pd
from faker import Faker
import random
import uuid
import logging

# Initialize Faker
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

# Predefined list of universities
UNIVERSITIES = [
    'Harvard University', 'Stanford University', 'Massachusetts Institute of Technology',
    'University of California, Berkeley', 'Princeton University', 'Yale University',
    'Columbia University', 'University of Oxford', 'University of Cambridge',
    'California Institute of Technology', 'University of Chicago', 'ETH Zurich',
    'Imperial College London', 'University of Toronto', 'University of Michigan',
    'National University of Singapore', 'Tsinghua University', 'Peking University',
    'University of Edinburgh', 'University of Tokyo', 'University of Florida'
]

# Configure logging
script_dir = os.path.dirname(os.path.abspath(__file__))
log_directory = os.path.join(script_dir, '..', 'logs')
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_directory, 'generate_synthetic_data.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Ensure the data and resumes directories exist
data_directory = os.path.join(script_dir, '..', 'data')
resumes_directory = os.path.join(data_directory, 'resumes')
os.makedirs(resumes_directory, exist_ok=True)

def generate_resume(job_ids: list):
    """
    Generates a single synthetic resume and saves a dummy resume file.
    """
    # Select random attributes
    title = random.choice(JOB_TITLES)
    department = random.choice(DEPARTMENTS)
    skills = random.sample(SKILLS, 6)
    degree = random.choice(EDUCATION_DEGREES)
    major = random.choice(EDUCATION_MAJORS)
    employment_type = random.choice(EMPLOYMENT_TYPES)
    location = random.choice(LOCATIONS)
    
    # Generate multiple education entries
    education_entries = []
    num_educations = random.choice([1, 2])
    for _ in range(num_educations):
        university = random.choice(UNIVERSITIES)
        edu = f"{degree} in {major} from {university} ({random.randint(2005, 2020)})"
        education_entries.append(edu)
    education = '; '.join(education_entries)
    
    # Generate multiple experience entries
    experience_entries = []
    num_experiences = random.choice([1, 2, 3])
    for _ in range(num_experiences):
        exp = f"{random.randint(1, 5)} years at {fake.company()} as {random.choice(JOB_TITLES)} ({fake.paragraph(nb_sentences=3)})"
        experience_entries.append(exp)
    experience = '; '.join(experience_entries)
    
    # Generate certifications
    certifications = '; '.join([
        fake.word(ext_word_list=['Certified', 'Certified in', 'Certification in', 'Diploma in']) + ' ' + fake.word()
        for _ in range(random.randint(0, 3))
    ])
    
    # Generate languages
    languages = ', '.join(random.sample(
        ['English', 'Spanish', 'Mandarin', 'French', 'German', 'Japanese', 'Hindi', 'Arabic'],
        k=random.randint(1, 3)
    ))
    
    # Generate a unique resume ID
    resume_id = str(uuid.uuid4())
    
    # Create resume data dictionary
    resume = {
        'resume_id': resume_id,
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'education': education,
        'experience': experience,
        'skills': ', '.join(skills),
        'certifications': certifications,
        'languages': languages,
        'additional_info': fake.text(max_nb_chars=200),
        'job_id': random.choice(job_ids)
    }

    # Generate and save a dummy resume file
    resume_content = f"""
    Resume ID: {resume['resume_id']}
    Name: {resume['name']}
    Email: {resume['email']}
    Phone: {resume['phone']}
    
    Education:
    {resume['education']}
    
    Experience:
    {resume['experience']}
    
    Skills:
    {resume['skills']}
    
    Certifications:
    {resume['certifications']}
    
    Languages:
    {resume['languages']}
    
    Additional Information:
    {resume['additional_info']}
    """

    resume_filename = f"{resume_id}.txt"
    resume_path = os.path.join(resumes_directory, resume_filename)

    with open(resume_path, 'w', encoding='utf-8') as f:
        f.write(resume_content.strip())

    return resume

def generate_job_description():
    """
    Generates a single synthetic job description.
    """
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
    
    # Generate a unique job ID
    job_id = random.randint(100, 9999)  # Adjust range as needed to avoid collisions
    
    # Create job description dictionary
    job = {
        'job_id': job_id,
        'title': title,
        'department': department,
        'responsibilities': responsibilities,
        'requirements': requirements,
        'location': location,
        'employment_type': employment_type
    }
    return job

def generate_resumes(num_resumes: int, job_ids: list) -> pd.DataFrame:
    """
    Generates a specified number of synthetic resumes.
    """
    resumes = [generate_resume(job_ids) for _ in range(num_resumes)]
    return pd.DataFrame(resumes)

def generate_jobs(num_jobs: int) -> pd.DataFrame:
    """
    Generates a specified number of synthetic job descriptions.
    """
    jobs = []
    job_ids = set()
    while len(jobs) < num_jobs:
        job = generate_job_description()
        if job['job_id'] not in job_ids:
            jobs.append(job)
            job_ids.add(job['job_id'])
    jobs_df = pd.DataFrame(jobs).reset_index(drop=True)
    return jobs_df

def main():
    # Parameters
    NUM_RESUMES = 5000  # Adjust the number as needed
    NUM_JOBS = 50        # Adjust the number as needed
    
    try:
        # Generate job descriptions first to obtain unique job_ids
        logging.info("Generating synthetic job descriptions...")
        jobs_df = generate_jobs(NUM_JOBS)
        job_ids = jobs_df['job_id'].tolist()
        logging.info(f"Generated {len(jobs_df)} synthetic job descriptions.")
        print(f"Generated {len(jobs_df)} synthetic job descriptions.")
        
        # Generate resumes with job_ids from the generated jobs
        logging.info("Generating synthetic resumes...")
        resumes_df = generate_resumes(NUM_RESUMES, job_ids)
        logging.info(f"Generated {len(resumes_df)} synthetic resumes.")
        print(f"Generated {len(resumes_df)} synthetic resumes.")
        
        # Save to CSV
        resumes_csv_path = os.path.join(data_directory, 'Resume_Data.csv')
        jobs_csv_path = os.path.join(data_directory, 'Jobs_Data.csv')
        resumes_df.to_csv(resumes_csv_path, index=False)
        jobs_df.to_csv(jobs_csv_path, index=False)
        logging.info("Saved synthetic data to data/ directory.")
        print("Saved synthetic data to data/ directory.")
        
    except Exception as e:
        logging.error(f"Error during synthetic data generation: {e}")
        print(f"An error occurred during synthetic data generation: {e}")

if __name__ == "__main__":
    main()
