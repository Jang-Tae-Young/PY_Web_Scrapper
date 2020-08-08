# from indeed import get_jobs
import indeed
import stackoverflow
import save

indeed_jobs = indeed.get_jobs()
so_jobs = stackoverflow.get_jobs()

jobs = indeed_jobs + so_jobs

save.save_to_csv(jobs)


