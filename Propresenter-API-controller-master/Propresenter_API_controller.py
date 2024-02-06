#made in Python 3.11
#dependencies: kivy (2.2.1), requests (2.31.0)

#setup importing
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
        if ipaddr == "0":
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
        mouser = requests.get(pro_api_url,timeout = 5)
    except:
        print("connection was refused")
        time.sleep(3)
        sys.exit()
    else:
        requests.get(pro_api_url+"/v1/find_my_mouse",timeout = 5)

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

class popinfo:
    #populate screens data - Specifically gathers number of screens and subtracts any stage screens. Then assigns number and name in variable
    def screensgather():
        stagescreens = requests.get(pro_api_stage_screens, timeout = 5)
        stagescreenscontent = stagescreens.json()
        numofstagescreens = len(stagescreenscontent)
        allscreens = requests.get(pro_api_screens, timeout = 5)
        screenscontent = allscreens.json()
        numofscreens = len(screenscontent)
        actualscreennum = numofscreens - numofstagescreens
        loop = 0
        screennames = []
        for x in range(actualscreennum):
            layer1 = screenscontent[loop]
            layer2 = layer1["id"]
            data1 = layer2["name"]
            screennames.append(data1)
            loop += 1
        return numofscreens, screennames

        
    #populate the looks data
    def looksgather():
        alllooks = requests.get(pro_api_looks, timeout = 0.1)
        lookscontent = alllooks.json()
        numoflook = len(lookscontent)
        loop = 0
        looknames = []
        lookindex = []
        for x in lookscontent:
            layer1 = lookscontent[loop]
            layer2 = layer1["id"]
            data1 = layer2["name"]
            data2 = layer2["index"]
            looknames.append(data1)
            lookindex.append(data2)
            loop += 1
        
        return lookscontent, numoflook, looknames, lookindex
    
    #populate the themes data
    def themesgather():
        allthemes = requests.get(pro_api_themes, timeout = 0.1)
        themescontent = allthemes.json()
        #getting the number of themes - its a bit wonky becuase of the difference between themes and groups of themes (folder vs folder of folders)(it can also go indefinitely?)
        layer1 = themescontent["themes"]
        themesnum = len(layer1)
        layer2 = themescontent["groups"]
        loop = 0
        layeredlen = []
        for x in layer2:
            layer3 = layer2[loop]
            if layer3["groups"] == []:
                insidethegroup = len(layer3["themes"])
                layeredlen.append(insidethegroup)
            else:
                insideinsidethegroup = layer3["groups"]
                circuits = 0
                for x in insideinsidethegroup:
                    insideinsidethegroup[circuits]
                    if layer3["groups"] == []:
                        insidethegroup = len(layer3["themes"])
                        layeredlen.append(insidethegroup)
                        circuits += 1
                    else:print("I give up")
            loop += 1
        numofthemes = themesnum
        numofgthemes = layeredlen
        
        return themescontent, numofthemes, numofgthemes
    
    #populate the masks data
    def masksgather():
        allmasks = requests.get(pro_api_masks, timeout = 0.1)
        maskscontent = allmasks.json()
        numofmasks = len(maskscontent)
        loop = 0
        masknames = []
        maskindex = []
        for x in maskscontent:
            layer1 = maskscontent[loop]
            data1 = layer1["name"]
            data2 = layer1["index"]
            masknames.append(data1)
            maskindex.append(data2)
            loop += 1
        return numofmasks, masknames, maskindex

#exports gethered data as usable variables
numofscreens, screennames = popinfo.screensgather()
print("25%")
lookscontent, numoflook, looknames, lookindex = popinfo.looksgather()
print("50%")
#numofgthemes is a list because it contains the number of themes contained within each group. required to access the slides within each
themescontent, numofthemes, numofgthemes = popinfo.themesgather()
print("75%")
numofmasks, masknames, maskindex = popinfo.masksgather()
print("100%")

print(fjfjfjfjf)

requests.get(pro_api_find_mouse)
