import extractLink

session = extractLink.FetchLink("https://www.youtube.com/@krishnaik06/videos")
links = session.browser_session()
print(links)
session.store_link("links.txt",links)

