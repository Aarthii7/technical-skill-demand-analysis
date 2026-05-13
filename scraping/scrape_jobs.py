import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

urls = [
    "https://remoteok.com/remote-dev-jobs",
    "https://remoteok.com/remote-python-jobs",
    "https://remoteok.com/remote-data-jobs",
    "https://remoteok.com/remote-backend-jobs",
    "https://remoteok.com/remote-full-stack-jobs",
    "https://remoteok.com/remote-software-jobs",        
    "https://remoteok.com/remote-javascript-jobs",
    "https://remoteok.com/remote-react-jobs",
    "https://remoteok.com/remote-java-jobs",
    "https://remoteok.com/remote-api-jobs",
    "https://remoteok.com/remote-engineer-jobs",
    "https://remoteok.com/remote-cloud-jobs",
    "https://remoteok.com/remote-devops-jobs",
    "https://remoteok.com/remote-ai-jobs",
    "https://remoteok.com/remote-machine-learning-jobs",
    "https://remoteok.com/remote-security-jobs",
]

job_data_list = []

for url in urls:

    driver.get(url)

    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "job")

    print(f"Jobs found in {url}: {len(jobs)}")

    for job in jobs:

        try:

            role = job.get_attribute("data-search")

            company = job.get_attribute("data-company")

            tags = job.find_elements(By.CLASS_NAME, "tag")

            skills = [tag.text for tag in tags if tag.text.strip() != ""]

            job_data = {
                "Role": role,
                "Company": company,
                "Skills": ", ".join(skills)
            }

            job_data_list.append(job_data)

        except:
            pass

df = pd.DataFrame(job_data_list)

df.drop_duplicates(inplace=True)

print("\nTotal Rows:", len(df))

print(df.head())

df.to_csv("../data/real_jobs_data.csv", index=False)

driver.quit()