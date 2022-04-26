import requests

defaulturl = r'http://192.168.0.110:8080/wuyeApi'
path = '/login'
params = {'username' : '13000000000','password' : '123456'}

resp = requests.get(url=defaulturl,params=params)
resp.encoding = 'utf-8'
print(resp.text)
# print(resp.status_code)
# print(resp.url)
# print(resp.json)
# print(resp.headers)
# print(resp.content)
# print(resp.encoding)

resp = requests.post(url=defaulturl+path,data=params)

# print(resp.text)