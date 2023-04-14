import requests
from bs4 import BeautifulSoup

def get_job_links(keyword):
    url = f'https://www.indeed.com/jobs?q={keyword}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_links = []
    for job in soup.find_all(class_='jobtitle'):
        link = job.find('a')['href']
        if link.startswith('/rc'):
            link = 'https://www.indeed.com' + link
        job_links.append(link)
    return job_links
