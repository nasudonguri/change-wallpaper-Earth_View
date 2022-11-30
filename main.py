import urllib.request as req
import ctypes
import os, shutil, re, time

path = './img'
if os.path.isdir(path):
  shutil.rmtree(path)
os.makedirs(path)
with req.urlopen(
  req.Request(
    'https://earthview.withgoogle.com/',
    None,
    headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
  )
) as res:
  img = re.search(
    'https://www.gstatic.com/prettyearth/assets/full/(.*?).jpg',
    res.read().decode('utf-8')
  ).group()
  name = img.split('/')
  name = path+'/'+name[len(name)-1]
  req.urlretrieve(img, name)
  time.sleep(3)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(name), 0)