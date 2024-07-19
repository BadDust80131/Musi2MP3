import requests
import json
from pytube import YouTube
import threading


# Input Musi Playlist Code
code = input("Input Musi Playlist Code: ")
# Get site as JSON data
response = requests.get("https://feelthemusi.com/api/v4/playlists/fetch/" + code)
# Saves response in JSON format
data = response.json()

# Converts data from JSON to dict format
parsed = json.loads(data['success']['data'])

# Function for downloading mp3 from video, gets passed videos from the parsed variable
def download(vid):
    link = YouTube("https://www.youtube.com/watch?v=" + vid["video_id"])
    # Only downloads audio rather than the full video
    video = link.streams.filter(only_audio=True).first()
    video.download(filename=f"{link.title}.mp3",output_path="C:/Users/PC/Downloads/Music/Music")

# Creates a thread for each mp3 in list then downloads them all asynchronously
# Variable needed to keep track of all threads
threads = []
for vid in parsed['data']:
    # For each video create a thread then start it, then add thread to thread list for keeping track of
    t = threading.Thread(target=download,args=(vid,))
    t.start()
    print("Starting:" + vid["video_name"])
    threads.append(t)
# Combines all threads then closes program
for t in threads:
    t.join()
exit()








# Old Code
# Prints only the required data
#print(parsed['data'][1]["video_id"])

# Loops through all songs in dict and downloads them
#for vid in parsed['data']:
#    link = YouTube("https://www.youtube.com/watch?v=" + vid["video_id"])
#    video = link.streams.filter(only_audio=True).first()
#    video.download(filename=f"{link.title}.mp3")