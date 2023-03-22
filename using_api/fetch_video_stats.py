import googleapiclient.discovery
import requests
# API information
api_service_name = "youtube"
api_version = "v3"
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]

youtube = googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)
video_id="6I2m7VtGLU4"
r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={api}".format(api=DEVELOPER_KEY,id=video_id))
print(r.json())
