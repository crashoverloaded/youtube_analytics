import requests
import googleapiclient.discovery

# API information
api_service_name = "youtube"
api_version = "v3"

# API Key
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]

# GET Request for Channel ID through username
channel = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&forUsername={id}&key={api}".format(api=DEVELOPER_KEY,id='krishnaik06'))
print(channel.json()['items'][0])
# Getting details of channel(stats) and "uploads" playlist ID
upload_playlist_ID = channel.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
channel_statistics = channel.json()['items'][0]['statistics']

# Building client
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)

# Fetching latest 50 videos Information
videos = youtube.playlistItems().list(playlistId=upload_playlist_ID,part='snippet',maxResults=50).execute()

video_stats = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id1}&id={id2}&key={api}".format(api=DEVELOPER_KEY,id1='6I2m7VtGLU4',id2='gbJn2Ls2QsI'))
print(video_stats.json())

count=1
basesentence = "https://www.googleapis.com/youtube/v3/videos?part=statistics"
for video in videos['items']:
    video_id = video['snippet']['resourceId']['videoId']
    finalsentence = basesentence+"&id="+str(video_id)
    basesentence=finalsentence

final_get_link = finalsentence+"&key="+DEVELOPER_KEY
print(requests.get(final_get_link).json())
"""
# Parsing through every video
for video in videos['items']:
    video_id = video['snippet']['resourceId']['videoId']
    video_stats = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={api}".format(api=DEVELOPER_KEY,id=video_id))
    print(video_stats.json()['items'][0])
    print(video_stats.json()['items'][0]['statistics'])
"""
# comments parser
