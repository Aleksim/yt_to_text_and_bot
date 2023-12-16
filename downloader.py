from pytube import YouTube
import os


def download_audio_from_youtube(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f"Audio downloaded and saved as {new_file}")
    return new_file

