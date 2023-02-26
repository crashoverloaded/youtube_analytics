from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import time

#app = Flask(__name__)


def latest_fifty_videos(link):
    # initiating the webdriver using chromedriver
    browser = webdriver.Chrome()

    # maximizing the window of the chromedriver
    browser.maximize_window()

    # visiting this URL using `get` method in driver
    browser.get(link)
    time.sleep(1)

    # initiating the list which will store all the elements (50 elements for 50 vids)
    video_list = []

    try:
        while len(video_list) <=50:
            time.sleep(2)

            # It will store the contents which includes all elements regarding videos
            video_list = browser.find_elements(By.XPATH, "//a[@class='yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media']")
            time.sleep(2)

            # this will scroll to the bottom to load more videos
            browser.find_element(By.CLASS_NAME, "style-scope ytd-continuation-item-renderer").click()
            time.sleep(2)
            print("Total videos captured: ",len(video_list))
        return video_list[:50]
    except Exception as e:
        print("kuch gadbad h: ", e)
        browser.quit()
        pass

elements = latest_fifty_videos("https://www.youtube.com/@krishnaik06/videos")

file1 = open("links.txt","a")
for i in elements:

    # getting the links of videos for each element
    link = i.get_attribute("href")
    print(link)

    # storing all the elements in the file
    file1.write(link+"\n")
    print("OK")

file1.close()
