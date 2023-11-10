#dependencies: kivy (2.2.1), requests (2.31.0), virtualenv (20.24.5), keyboard(0.13.5), pprint

#setup importing
import os
from multiprocessing.connection import wait
from tkinter import FALSE
import requests
import pprint
import time
import keyboard
import kivy
import json

#kivy programming file importing
#import prolayoutguix



#Variable Assignment
####url setup
#local_ip_addr = "http://192.168.0.118"
#local_ip_port = "7777"
#local_ip_addr = "http://192.168.0.73"
#local_ip_port = "1077"
local_ip_addr = "http://localhost"
local_ip_port = "1026"
pro_api_url = local_ip_addr+":"+local_ip_port


####api variable setup
###192.168.0.73:1077/v1/doc/index.html
pro_api_active_look = pro_api_url+"/v1/look/current"
pro_api_looks = pro_api_url+"/v1/looks"
pro_api_looks = pro_api_url+"/v1/themes"

firstscreen = 0

####function
response = requests.get(pro_api_looks)
response.json()
print(response.json)
#json.load(response.content)
#json.part
#data = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
#dir(response)
#print(response.json())
#print(type(response.json))

####function okay so the thing is that the only object keys we have are groups and themes meaning that we have to make objects ourselves using bytes :(
#response = requests.get(pro_api_looks)
#response.content
#print(response.content)
#json.load(response.content)
#beans = response.json()
#print(beans)
#print("[n\\")
#print("Dict key-value are : ")
#tincan = beans.keys()
#print(tincan)

#import json

#my_bytes_value = b'[{\'Date\': \'2016-05-21T21:35:40Z\', \'CreationDate\': \'2012-05-05\', \'LogoType\': \'png\', \'Ref\': 164611595, \'Classe\': [\'Email addresses\', \'Passwords\'],\'Link\':\'http://some_link.com\'}]'

# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
#my_json = my_bytes_value.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
#data = json.loads(my_json)
#s = json.dumps(data, indent=4, sort_keys=True)
#print(s)

#dir(response.json())

#for group in print(response.content()["groups"]):
#    print(group)
#    break

####pretty conversion
#read_looks = pprint.pformat(response.json(), width = 1)


##try input().strip() instead of keyboard.is_pressed...
#print("input y to save to file")
#savelooks = input().strip
#if savelooks == "y":
#    with open("looks.txt", "a") as looks_file:
#        looks_file.write(read_looks)


#print("press y to write to file")
#while True:
#    try:
#        if keyboard.is_pressed("y"):
#            print("saving file")
#            with open("looks.txt", "a") as looks_file:
#                looks_file.write(read_looks)
#            break
#        else:
#            break
#    except:
#            break
#

