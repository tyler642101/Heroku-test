import requests

URL = "https://www.googleapis.com/youtube/v3/search"

key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"

param1 = "snippet"

param2 = "cats"

param3 = "10"

param4 = "viewCount"

param5 = "video"

param6 = "true"

PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'order':param4, 'type':param5, 'videoEmbeddable':param6}

r = requests.get(url=URL, params=PARAMS)

data = r.json()

for record in data['items']:
    print(record['id']['videoId'])