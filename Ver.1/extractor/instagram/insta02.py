
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

keyword01 = input("Input id you want : ")
keyword02 = input("Input pw you want : ")
service = Service(r"C:\Users\Luna\Desktop\Projects\Python Scrapper\Ver.1\chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/")
sleep(3)

id = driver.find_element(By.NAME, "username")
id.send_keys(keyword01)

pw = driver.find_element(By.NAME, "password")
pw.send_keys(keyword02)

sleep(3)

driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()

#pw = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()
