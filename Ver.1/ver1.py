from requests import get
from bs4 import BeautifulSoup
from extractor.wwr import extract_jobs
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source,"html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0")
    pagination_div = pagination.select("div")
    if len(pagination_div)== 0:
        return 1
    else:
        return len(pagination_div)

print(get_page_count("nextjs"))

def extract_indeed_jobs(keyword):
    browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source,"html.parser")
    results = []
    job_list = soup.find('ul', class_="jobsearch-ResultsList css-0")
    jobs = job_list.find_all('li', recursive=False)
    #Use recursive to select li directly related with
    for j in jobs:
        zone = j.find("div", class_="mosaic-zone")
        if zone == None: 
            # Filtering box dosen't include job info (has class name mosaic-zone)
            # j.find will return None in case of dosen't exists
            # h2 = j.find("h2", class_="jobTitle") -- by this method, need aditional code for extract anchor
            # use select to save code (able to CSS selector)
            anchor = j.select_one("h2 a") # for just get one element (not list), use select_one
            title = anchor['aria-label']
            link = anchor['href']
            company = j.find("span", class_="companyName")
            location = j.find("div", class_="companyLocation")
            job_data = {'link': f"https://kr.indeed.com{link}",'company':company.string, 'location':location.text, 'position':title}
            results.append(job_data)
    for r in results:
        print (r)
        print ("-------------------------------------------")
    # extract text : use .string as span tag, use .text as div tag




    
