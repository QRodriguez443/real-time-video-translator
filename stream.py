from pytube import YouTube

# Retrieve URL of video if user is currently on the relevant page
url = "https://"
youtube = YouTube(url)
video = youtube.streams.first()
streaming_url = video.url