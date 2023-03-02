# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
keyFile = open('config.py', 'r')
DEVELOPER_KEY = keyFile.readlines()[0].rstrip().split("=")[1]
# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
# Request body
request = youtube.search().list(
        part="id,snippet",
        type='video',
        q="Spider-Man",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1
)
# Request execution
response = request.execute()
print(response)
