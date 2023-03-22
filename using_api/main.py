# API client library
import googleapiclient.discovery
import requests
# API information
api_service_name = "youtube"
api_version = "v3"
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]
# API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
res = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&forUsername={id}&key={api}".format(api=DEVELOPER_KEY,id='krishnaik06'))
# Request execution
response = res.json()
print(response)

