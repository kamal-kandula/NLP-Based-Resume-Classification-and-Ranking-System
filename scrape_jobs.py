import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_job_descriptions(url, role):
    """Scrape job descriptions from a job board."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    job_descriptions = []

    job_cards = soup.find_all("div", class_="job_seen_beacon")
    for job in job_cards:
        title = job.find("h2", class_="jobTitle").get_text(strip=True)
        company = job.find("span", class_="companyName").get_text(strip=True)
        description = job.find("div", class_="job-snippet").get_text(strip=True)
        job_descriptions.append({"Job_Description": description, "Category": role})

    return pd.DataFrame(job_descriptions)

roles = {
    "Data Scientist": "https://www.indeed.com/jobs?q=Data+Scientist",
    "Software Engineer": "https://www.indeed.com/jobs?q=Software+Engineer",
    "Product Manager": "https://www.indeed.com/jobs?q=Product+Manager",
    "Data Analyst": "https://www.indeed.com/jobs?q=Data+Analyst",
    "Project Manager": "https://www.indeed.com/jobs?q=Project+Manager",
    "Business Analyst": "https://www.indeed.com/jobs?q=Business+Analyst",
    "DevOps Engineer": "https://www.indeed.com/jobs?q=DevOps+Engineer",
    "UX/UI Designer": "https://www.indeed.com/jobs?q=UX+UI+Designer",
    "Digital Marketing Specialist": "https://www.indeed.com/jobs?q=Digital+Marketing+Specialist",
    "Human Resources Manager": "https://www.indeed.com/jobs?q=Human+Resources+Manager",
    "Finance Manager": "https://www.indeed.com/jobs?q=Finance+Manager",
    "Operations Manager": "https://www.indeed.com/jobs?q=Operations+Manager",
    "Machine Learning Engineer": "https://www.indeed.com/jobs?q=Machine+Learning+Engineer",
    "Quality Assurance Engineer": "https://www.indeed.com/jobs?q=Quality+Assurance+Engineer",
    "Technical Writer": "https://www.indeed.com/jobs?q=Technical+Writer",
    "Customer Success Manager": "https://www.indeed.com/jobs?q=Customer+Success+Manager",
    "Network Administrator": "https://www.indeed.com/jobs?q=Network+Administrator",
    "Web Developer": "https://www.indeed.com/jobs?q=Web+Developer",
    "Cloud Solutions Architect": "https://www.indeed.com/jobs?q=Cloud+Solutions+Architect",
    "Graphic Designer": "https://www.indeed.com/jobs?q=Graphic+Designer"
}

all_jobs = []

for role, url in roles.items():
    jobs = scrape_job_descriptions(url, role)
    all_jobs.append(jobs)

job_data = pd.concat(all_jobs, ignore_index=True)
job_data.to_csv("data/Job_Descriptions.csv", index=False)
print("Job descriptions saved to 'data/Job_Descriptions.csv'")