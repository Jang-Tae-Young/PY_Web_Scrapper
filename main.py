import requests

indeed_results = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_results)

