# Imports
import os
import pyfiglet
import subprocess
from datetime import datetime
import pytz

now = datetime.now()
# Traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []
 
# Arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    print(i[2:-2])

# Banner

ascii_banner = pyfiglet.figlet_format("Spotify Downloader")
print(ascii_banner)

# London time

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

# Time from user executing the script

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Actual song/playlist download
song = input("URL: ")
os.system(f"spotdl {song}")
os.remove(".spotdl-cache")