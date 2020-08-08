import csv

def save_to_csv(in_jobs):

    file = open("jobs.csv",mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    
    for job in in_jobs:
        writer.writerow(list(job.values()))
    
    return

