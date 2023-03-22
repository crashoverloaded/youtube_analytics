import requests
import googleapiclient.discovery

# API information
api_service_name = "youtube"
api_version = "v3"

# API Key
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]

# GET Request for Channel ID through username
res = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&forUsername={id}&key={api}".format(api=DEVELOPER_KEY,id='krishnaik06'))

# Getting details
upload_playlist_ID = res.json()['items'][0]['contentDetails']
statistics = res.json()['items'][0]['statistics']

# Building client
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)
print(statistics)

