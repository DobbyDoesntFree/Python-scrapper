from tkinter import W
from extractor.wwr import extract_wwr_jobs
from extractor.indeed import extract_indeed_jobs

keyword = input("What do you want to search for?")

wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)
jobs = indeed + wwr

file=open(f"{keyword}.csv","w", encoding="utf-8") # create file 
file.write("Position,Company,Location,URL\n")
             

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
