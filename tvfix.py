import requests
header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
         'Baseurl':'http://live.tvfix.org'}
print(requests.get('http://live.tvfix.org/hls/jadehk.m3u8',headers=header).text)