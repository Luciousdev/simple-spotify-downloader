import subprocess

def downloadSongs(url):
  print("test")
  try:
    result = subprocess.run(f"python -m spotdl {url}", shell=True, check=True, capture_output=True, text=True)
    print(result.stdout)        
    return 1
  except subprocess.CalledProcessError as e:
    return e.stderr
