import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Defined the URL of the job search platform (Indeed)
url = 'https://www.indeed.com/jobs?q=software+developer&l=New+York'

# Sent an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract job listings
job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

# Prepare a list to store job data
jobs = []

# Extract data from each job listing
for job in job_listings:
    title = job.find('h2', class_='title').text.strip()
    company = job.find('span', class_='company').text.strip()
    location = job.find('div', class_='location').text.strip()
    description = job.find('div', class_='summary').text.strip()
    
    jobs.append([title, company, location, description])

# Save the job data to a CSV file
filename = f'jobs_{datetime.now().strftime("%Y-%m-%d_%H%M%S")}.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location', 'Description'])
    writer.writerows(jobs)

print(f'Job data saved to {filename}')
