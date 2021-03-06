import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_number_of_pages():

    results    = requests.get(URL)
    soup       = BeautifulSoup(results.text,'html.parser')
    pagination = soup.find("div",{"class":"pagination"})
    links      = pagination.find_all('a')
    pages=[]
    
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]

    return max_page

def extract_job(html):

    title = html.find("h2",{"class":"title"}).find("a")["title"]
    
    company = html.find("span",{"class":"company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        company = company.strip()
    else:
        company = "None"
        
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title':title, 
        'company':company, 
        'location':location, 
        'link':f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_pages):
    jobs = []
    # print("last_pages:", last_pages)
    for page in range(last_pages):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup   = BeautifulSoup(result.text,'html.parser')
        job_results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for a_result in job_results:
            job = extract_job(a_result)
            jobs.append(job)

    return jobs

def get_jobs():
    indeed_max_page = get_number_of_pages()
    jobs = extract_jobs(indeed_max_page)

    return jobs
