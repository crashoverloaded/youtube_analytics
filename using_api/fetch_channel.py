import googleapiclient.discovery
import requests
# API information
api_service_name = "youtube"
api_version = "v3"
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]

youtube = googleapiclient.discovery.build('youtube','v3',developerKey=DEVELOPER_KEY)
id1 = "UCNU_lfiiWBdtULKOw6X0Dig"
id2 = "UUNU_lfiiWBdtULKOw6X0Dig"
#res = youtube.channels().list(id=id1,part="contentDetails").execute()
r = youtube.playlistItems().list(playlistId=id2,part='snippet',maxResults=50).execute()
for i in r['items']:
    print(i['snippet'])


