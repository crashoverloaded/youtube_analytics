from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
file = open("links.txt", "r")
likes_count = []
title_list = []
views_list=[]
upload_time = []
for link in file:
  browser.get(link)
  time.sleep(2)
  try:

    # PART (i) - GETTING LIKES
    # path for the like element of the website
    xpath = ".//span[@class='yt-core-attributed-string yt-core-attributed-string--white-space-no-wrap']"
    like_element = browser.find_elements(By.XPATH,xpath)
    # this above variable like_element is a list containing many elements , but we just need to extract like element from it
    like = like_element[4].text
    likes_count.append(like)
    print(like)
    time.sleep(2)
    # PART (ii) - GETTING title of video

    # this xpath contains elements like title , no. of views and upload time
    # Hence we will extract all info one by one
    xpath = ".//yt-formatted-string[@class='style-scope ytd-watch-metadata']"
    title_element = browser.find_elements(By.XPATH, xpath)
    title=title_element[1].text
    views=title_element[3].text.split(" ")[0]
    upload = title_element[3].text.split(" ")[2]+title_element[3].text.split(" ")[3]+title_element[3].text.split(" ")[4]
    print(title)
    print(views)
    print(upload)
    title_list.append(title)
    views_list.append(views)
    upload_time.append(upload)

    # thumbnail image
    thumbnail = browser.find_element(By.XPATH, "//link[@rel='image_src']")
    print(thumbnail.get_attribute("href"))
    time.sleep(5)
  except Exception as e:
    print(e)
    pass

