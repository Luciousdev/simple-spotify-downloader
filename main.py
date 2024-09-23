import eel
from src.scripts.downloadsongs import downloadSongs

eel.init("src/web")

@eel.expose
def startDownload(userInput):
  result = downloadSongs(userInput)
  return result

def start_eel():
  eel.start("index.html", size=(1280, 720))

if __name__ == "__main__":
  start_eel()
