from requests import get
from bs4 import BeautifulSoup

# The function below dosen't use selenium

def extract_wwr_jobs(keywords):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keywords}")
    if response.status_code !=200:
        print ("Can't reach the server")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                try:
                    company = anchor.find_all('span', class_="company")[0].string.replace(",", " ")
                except:
                    company = "No data"
                try:
                    kind = anchor.find_all('span', class_="company")[1].string.replace(",", " ")
                except:
                    kind = "No data"
                try:
                    region = anchor.find_all('span', class_="company")[2].string.replace(",", " ")
                except:
                    region = "No data"
                    
                title = anchor.find('span', class_='title').string.replace(",", " ")

                job_data = {"company":company, "location":region, "position":title, "link":f"https://weworkremotely.com/{link}"}
                results.append(job_data)      
    return results

print(extract_wwr_jobs("react"))

