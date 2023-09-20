#dependencies: kivy (2.2.1), requests (2.31.0), virtualenv (20.24.5), keyboard(0.13.5), pprint

#import Setup
import os
from multiprocessing.connection import wait
from tkinter import FALSE
import requests
import pprint
import time
import keyboard
import kivy

##kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#requirements
kivy.require("2.2.1")


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

#App Building

class ImportantInfoWidget(GridLayout):
    pass

class SplashScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="IP_ADDR"))
        self.ipaddr = TextInput(multiline=FALSE)
        self.add_widget(self.ipaddr)
        self.add_widget(Label(text="IP_PORT"))
        self.ipport = TextInput(password=FALSE, multiline=FALSE)
        self.add_widget(self.ipport)

class SplashConfig(App):
    def build(self):
        return SplashScreen()


if __name__ == "__main__":
    SplashConfig().run()

#class Pro_api_exe(App):
#    def build(self):
#        return Label(text="testing 1 2 3...")

#if __name__ == "__main__":
#    Pro_api_exe().run()



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
