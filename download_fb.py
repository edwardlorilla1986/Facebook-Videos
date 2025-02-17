import yt_dlp
import sys

def download_facebook_video(url, output_path="downloads", cookies_file="cookies.txt"):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'cookies': cookies_file  # Pass Facebook cookies
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_fb.py <Facebook Video URL>")
        sys.exit(1)

    fb_video_url = sys.argv[1]
    download_facebook_video(fb_video_url)
