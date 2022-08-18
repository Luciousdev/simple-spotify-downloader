import os
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Spotify Downloader")
print(ascii_banner)
song = input("URL: ")
os.system(f"spotdl {song}")
os.remove(".spotdl-cache")