from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
    page_indicater = 1
    browser.get(f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&recruitPage={page_indicater}&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n")
    soup = BeautifulSoup(browser.page_source,"html.parser")
    job_box = soup.find("a", class_="track_event data_layer")
    next_box = soup.select("a[class=data_layer] > span")
    print(len(job_box), len(next_box))


    # page_pointor = 0
    # res = []
    # loop_indicator = 6
    # while loop_indicator>=6:
    #     browser.get(f"https://kr.indeed.com/jobs?q={keyword}&start={page_pointor*10}")
    #     soup = BeautifulSoup(browser.page_source,"html.parser")
    #     pagination = soup.find("nav", class_="css-jbuxu0")
    #     pagination_div = pagination.select("div") # box amount
    #     pagination_next = pagination.select("div > a.css-fnfhcj") # if this is 1 and pagination_div also less than 6 make break point

    #     if len(pagination_div)<=5 and len(pagination_next) ==0:
    #         return len(pagination_div)
    #     else:
    #         page_pointor = page_pointor + 1
    #         loop_indicator = len(pagination_div)
    #         res.append(len(pagination_div))

get_page_count("python")