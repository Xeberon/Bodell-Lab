
import kivy

#housekeeping imports
from tkinter import FALSE
#from Propresenter_API_controller import 

##kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix import boxlayout

#requirements
kivy.require("2.2.1")




#App Building

class ImportantInfoWidget(GridLayout):
    pass

class SplashScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        layout = boxlayout
        self.cols = 2
        self.add_widget(Label(text="IP_ADDR"))
        self.ipaddr = TextInput(multiline=FALSE)
        self.add_widget(self.ipaddr)
        self.add_widget(Label(text="IP_PORT"))
        self.ipport = TextInput(password=FALSE, multiline=FALSE)
        self.add_widget(self.ipport)
        self.add_widget = (Button(text="default"))
        self.add_widget = (Button(text="next"))
        

class SplashConfig(App):
    def build(self):
        return SplashScreen()


if __name__ == "__main__":
    SplashConfig().run()

class Pro_api_exe(App):
    def build(self):
        return Label(text="testing 1 2 3...")

if __name__ == "__main__":
    Pro_api_exe().run()

