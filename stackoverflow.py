import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"
# &pg=2

def get_number_of_pages():

    results    = requests.get(URL)
    soup       = BeautifulSoup(results.text,'html.parser')
    pagination = soup.find("div",{"class":"s-pagination"})
    links      = pagination.find_all('span')
    pages=[]

    return int(links[-2].string)


def extract_job(html):
    title = html.find("a",{"class":"s-link"})["title"]
    company, location = html.find("h3",{
        "class":"fc-black-700 fs-body1 mb4"
        }).find_all(
            "span",recursive = False)

    if company:
        company = company.get_text(strip = True)
    else:
        company = None

    if location:
        location = location.get_text(strip = True)
    else:
        location = None

    link = html.find("a",{"class":"s-link"})["href"]
    return {
        'title':title, 
        'company':company, 
        'location':location, 
        'link':f"https://stackoverflow.com{link}"
    }


def extract_jobs(last_pages):
    jobs = []
    # last_pages = 5
    for page in range(last_pages):
        print(f"Scrapping page {page}/{last_pages}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup   = BeautifulSoup(result.text,'html.parser')
        job_results = soup.find_all("div",{"class":"-job"})

        for a_result in job_results:
            job = extract_job(a_result)
            jobs.append(job)

    return jobs



def get_jobs():
    numpage = get_number_of_pages()
    jobs    = extract_jobs(numpage)

    return jobs