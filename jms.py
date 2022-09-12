import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

r = requests.get('https://m3u.52sf.ga/JMSTV-PHP.m3u')
# print(r.text)
import m3u8

playlist = m3u8.load('https://m3u.52sf.ga/JMSTV-PHP.m3u')
# print(playlist.segments)
# print(playlist.target_duration)
for index, segment in enumerate(playlist.segments):
   print(segment.title+',' + segment.uri)
#    break
