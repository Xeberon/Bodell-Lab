#dependencies: kivy (2.2.1), requests (2.31.0), virtualenv (20.24.5), pprint

import requests
import pprint
import time
pro_api_url = "http://192.168.0.118:7777"
pro_api_looks = pro_api_url+"/v1/looks"

#function
response = requests.get(pro_api_looks)
response.json()
#print(response.json())
#time.sleep(1)

with open("looks.txt", "a") as f:
    read_looks = pprint.pformat(response.json(), width = 1)
    time.sleep(1)
    #pprint.isreadable(read_looks)
    #print(response.json, file=f)
    f.write(read_looks)
