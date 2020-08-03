from indeed import extract_indeed_pages, extract_indeed_jobs

indeed_max_page = extract_indeed_pages()
jobs = extract_indeed_jobs(indeed_max_page)

# print(jobs)

# for n in range(max_page):
    # print(f"start={n*50}")




