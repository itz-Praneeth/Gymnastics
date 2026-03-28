import yt-dlp
import os

# List of YouTube gymnastics competition videos
video_urls = [
    "https://www.youtube.com/watch?v=XXXXXXXXX",  # replace with real URLs
    "https://www.youtube.com/watch?v=XXXXXXXXX",
]

output_folder = "dataset/raw_videos"
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    'format': 'mp4',
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'quiet': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_urls)

print("✅ Videos downloaded!")
