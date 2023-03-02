from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FetchLink:
    def __init__(self,link):
        self.link = link

    def browser_session(self):

        # initiating the webdriver using chromedriver
        browser = webdriver.Chrome()

        # maximizing the window of the chromedriver
        browser.maximize_window()

        # visiting this URL using `get` method in driver
        browser.get(self.link)
        time.sleep(2)

        # initiating the list which will store all the elements (50 elements for 50 videos)
        video_list = []
        try:
            while len(video_list) <= 50:
                # It will store the contents which includes all elements regarding videos
                video_list = browser.find_elements(By.XPATH,"//a[@class='yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media']")

                # this will scroll to the bottom to load more videos
                browser.find_element(By.CLASS_NAME, "style-scope ytd-continuation-item-renderer").click()
                time.sleep(2)
                print("Total videos captured: ", len(video_list))
            return [i.get_attribute("href") for i in video_list[:50]]
        except Exception as e:
            print("Error as follows: ", e)

    def store_link(self,filename,links):
        file1 = open(filename, "a")
        for i in links:
            # storing all the elements in the file
            file1.write(i + "\n")
        file1.close()