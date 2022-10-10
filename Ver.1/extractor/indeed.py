from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source,"html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0")
    pagination_div = pagination.select("div")
    if len(pagination_div)== 0:
        return 1
    elif len(pagination_div)>=5:
        return 5
    else:
        return len(pagination_div)


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):

        browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
        url_req = f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}"
        browser.get(url_req)
        print("Requesting", url_req)
        soup = BeautifulSoup(browser.page_source,"html.parser")

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
        #for r in results:
        #    print (r)
        #    print ("-------------------------------------------")
            # use this for loop for return results one by one
            # extract text : use .string as span tag, use .text as div tag
    return results    
