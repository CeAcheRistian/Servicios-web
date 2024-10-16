from urllib import request

URL: str = 'http://localhost:8000/'

respone = request.urlopen(URL)
print(respone.read())