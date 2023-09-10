import requests 
import time
req= requests.get("https://flights-api.buraky.workers.dev/")
#Status Code
print("Status code is ",req.status_code)
#Full Text
print("Full text")
print(req.text)

#print(req.content)
#Header Type
print("Header Type:")
print(req.headers['content-type'])