import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()
file = open("links.txt", "r")
likes_count = []
title_list = []
views_list=[]
upload_time = []
image = 1

try:
  os.makedirs("Thumbnails")
except:
  print("Directory Thumbnails present !!")
  pass
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
    title_list.append(title)
    views_list.append(views)
    upload_time.append(upload)

    # Part (iii) - Getting Thumbnail images and saving in a folder
    # thumbnail image
    thumbnail_element = browser.find_element(By.XPATH, "//link[@rel='image_src']")
    thumbnail_link = thumbnail_element.get_attribute("href")
    # Downloading the thumbnail using urllib
    urllib.request.urlretrieve(thumbnail_link,"./Thumbnails/thumbnail"+str(image)+".png")
    image+=1
    time.sleep(2)
   # THis is for scrolling -> browser.find_element(By.CLASS_NAME, "style-scope ytd-continuation-item-renderer").click()

    # Part (iv) - Comments

    comment_section = browser.find_element(By.XPATH,"//*[@id='comments'][last()]")
    browser.execute_script("arguments[0].scrollIntoView();",comment_section)
    time.sleep(3)
    last_height = browser.execute_script('return document.documentElement.scrollHeight')
    while True:
      browser.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")
      time.sleep(2)
      new_height = browser.execute_script('return document.documentElement.scrollHeight')
      if new_height == last_height:
        break
      last_height = new_height

    browser.execute_script("window.scrollTo(0,'document.documentElement.scrollHeight');")
    try:
      comment = browser.find_elements(By.XPATH,"//*[@id='content-text']")
      author = browser.find_elements(By.XPATH,"//*[@id='author-text']")
      for i in range(len(comment)):
        print(comment[i].text,author[i].text)
    except:
      print("gadbad")
      pass
  except Exception as e:
    print(e)
    pass

