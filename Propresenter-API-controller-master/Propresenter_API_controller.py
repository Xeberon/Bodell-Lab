#made in Python 3.11
#dependencies: kivy (2.2.1), requests (2.31.0)

#setup importing
from http.client import InvalidURL
import sys
import time
import requests
import json

#Add requirements file

#Variable Assignment

class ipsetup:
    def addresssetup():
        #user input sets ip address
        ipaddr = input("Please enter your target machine ip address: ").strip()
        if len(ipaddr) == 0:
            local_ip_addr = "localhost"
        elif ipaddr == "0":
            local_ip_addr = "192.168.0.73"
        else:
            local_ip_addr = ipaddr
        return local_ip_addr
    def portsetup():
        #user input sets port
        ipport = input("Please enter your target machine ip Port: ").strip()
        if len(ipport) == 0:
            local_ip_port = "7777"
        else:
            local_ip_port = ipport
        return local_ip_port
    
#merges ip and port together for easy reference
local_ip_addr = ipsetup.addresssetup()
local_ip_port = ipsetup.portsetup()
pro_api_url = "http://"+local_ip_addr+":"+local_ip_port


def connectiontest():
#tests for connection
    try:
        requests.get(pro_api_url,timeout = 1)
    except (Exception):
        print("connection was refused")
        time.sleep(3)
        sys.exit()
    else:
        print("success")

connectiontest()

####api variable setup
pro_api_active_look = pro_api_url+"/v1/look/current"
pro_api_looks = pro_api_url+"/v1/looks"
pro_api_themes = pro_api_url+"/v1/themes"
pro_api_masks = pro_api_url+"/v1/masks"
pro_api_screens = pro_api_url+"/v1/status/screens"
pro_api_stage_screens = pro_api_url+"/v1/stage/screens"

pro_api_find_mouse = pro_api_url+"/v1/find_my_mouse"


firstscreen = 0

def grabmasks():
    #assume the data first
    maskscontent = requests.get(pro_api_masks).json()
    print(type(maskscontent))
    for maskshold in maskscontent:
        if type(maskshold) == dict:
            for key in maskshold:
                masks.uuid(maskshold[key])

class masks:
    #info that I need from masks is uuid, name, indexs
    def __init__(self, uuid, name, index):
        #init function to grab the data lol
        self.uuid = uuid
        self.name = name
        self.index = index
    

    
grabmasks()
    
print(grabmasks())

# #exports gethered data as usable variables
# numofscreens, screennames = popinfo.screensgather()
# print("25%")
# lookscontent, numoflook, looknames, lookindex = popinfo.looksgather()
# print("50%")
# #numofgthemes is a list because it contains the number of themes contained within each group. required to access the slides within each
# themescontent, numofthemes, numofgthemes = popinfo.themesgather()
# print("75%")
# numofmasks, masknames, maskindex = popinfo.masksgather()
# print("100%")

# print(fjfjfjfjf)

# requests.get(pro_api_find_mouse)
