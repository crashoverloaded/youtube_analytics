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

# Getting details of channel(stats) and "uploads" playlist ID
upload_playlist_ID = channel.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
channel_statistics = channel.json()['items'][0]['statistics']

# Building client
youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)

# Fetching latest 50 videos ID
videos = youtube.playlistItems().list(playlistId=upload_playlist_ID,part='snippet',maxResults=50).execute()

# creating a GET Link
baselink = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics"
for video in videos['items']:
    # videoID for each video
    video_id = video['snippet']['resourceId']['videoId']
    finalsentence = baselink +"&id="+str(video_id)
    baselink = finalsentence

# this is final GET link
final_get_link = finalsentence+"&key="+DEVELOPER_KEY

# Fetching results (videos stats , likes  , num of comments , etc.)
all_stats = requests.get(final_get_link).json()
print(all_stats)
for item in all_stats['items']:
    print(item['statistics'])
    print(item['snippet']['publishedAt'])
    print(item['snippet']['title'])
    print(item['snippet']['thumbnails']['default']['url'])

    
# comments parser
