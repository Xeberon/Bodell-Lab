#dependencies: kivy (2.2.1), requests (2.31.0), virtualenv (20.24.5), keyboard(0.13.5), pprint

#import Setup
from multiprocessing.connection import wait
import requests
import pprint
import time
import keyboard


#Variable Assignment
####url setup
local_ip_addr = "http://192.168.0.118"
local_ip_port = "7777"
pro_api_url = local_ip_addr+":"+local_ip_port

####api variable setup
pro_api_looks = pro_api_url+"/v1/looks"

####function
response = requests.get(pro_api_looks)
response.json()

####pretty conversion
read_looks = pprint.pformat(response.json(), width = 1)

print("press y to write to file")
while True:
    try:
        if keyboard.is_pressed("y"):
            print("saving file")
            with open("looks.txt", "a") as looks_file:
                looks_file.write(read_looks)
            break
        else:
            break
    except:
            break

