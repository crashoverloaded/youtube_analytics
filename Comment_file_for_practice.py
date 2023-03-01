comments = []
browser.find_element(By.CLASS_NAME, "style-scope ytd-continuation-item-renderer").click()
time.sleep(2)
no_of_comments = browser.find_element(By.XPATH,
                                      "//yt-formatted-string[@class='count-text style-scope ytd-comments-header-renderer']").text.split(
    " ")[0]

c = 1
time.sleep(2)
while len(comments) < int(no_of_comments):
    print(c)
    comments = browser.find_elements(By.XPATH, "//yt-formatted-string[@id='content-text']")
    print(len(comments))
    browser.find_element(By.XPATH, "(//div[@id='comment-content'])[last()]").location_once_scrolled_into_view
    for reply in browser.find_elements(By.XPATH,
                                       "//*[@id='replies']//paper-button[@class='style-scope ytd-button-renderer'][contains(.,'View')]"):
        reply.location_once_scrolled_into_view
        time.sleep(2)
        browser.execute_script("arguments[0].click()", reply)
        time.sleep(2)
        print(reply.text)
    c += 1
    time.sleep(3)

for i in comments:
    print(i.text)

print("OK")
browser.find_element(By.CLASS_NAME, "style-scope ytd-continuation-item-renderer").click()
print("ll")
time.sleep(2)
comments = browser.find_element("//div[@id='comment-content']")
print("dsa")
print(comments)
browser.execute_script(f"arguments[{comments}].scrollIntoView();")
time.sleep(5)
previous_height = browser.execute_script("return document.documentElement.scrollHeight")
# loop running while height is equal to actual height
while True:
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(2)
    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    if new_height == previous_height:
        break
    previous_height = new_height

    time.sleep(10)
    previous_height += 300
    if previous_height >= height:
        break

comments = browser.find_elements(By.XPATH,
                                 "//ytd-comment-thread-renderer[@class='style-scope ytd-item-section-renderer']")
print(len(comments))
for i in comments:
    print(i)