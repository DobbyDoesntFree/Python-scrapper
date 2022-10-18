from ssl import Options
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

keyword = input("Input keyword you want : ")
service = Service(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get(f"https://www.instagram.com/explore/tags/{keyword}/")

#browser = webdriver.Chrome(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
 
sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
divs = soup.find_all("div", class_="_aagv")
for img in divs:
    print(img.find("img")['src'])


