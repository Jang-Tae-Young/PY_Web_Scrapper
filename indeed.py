import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():

    results    = requests.get(URL)
    soup       = BeautifulSoup(results.text,'html.parser')
    pagination = soup.find("div",{"class":"pagination"})
    links      = pagination.find_all('a')
    pages=[]
    
    for link in links[:-1]:
        pages.append(int(link.string))
        # pages.append(link.find("span").string)
    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_pages):
    jobs = []
    page = 0
    # for page in range(last_pages):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup   = BeautifulSoup(result.text,'html.parser')
    job_results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for a_result in job_results:
        title = a_result.find("h2",{"class":"title"}).find('a')['title']
        # title = a_result.find("h2",{"class":"title"}).find('a').get('title')
        print(title)
        print("===================================")

        # print(jobtitle.title)
        # print(a_result.find("h2",{"class":"title"}).string )

    return jobs

