import os
import sys
import time

import kivy
from kivy.app clock import App
from kivy.clock import clock
from kivy.core.window import Window
from kivy.uix.dropdown import Button
from kivy.uix.dropdown  import Dropdown
from kivy.uix.gridlayout import Gridlayout
from kivy.uix.label import Label
from  kivy.uix.label import ScreenManager, Screen
from kivy.uix.scrollview import Scrollview
from kivy.uix.textinput import TextInput

kivy.require('2.0.0')
import socket_client

class Scrollablel(ScrollView):
   
    def __init__(self, **kwargs):
        super(). __init__(**kwargs)
        self.layout = Gridlayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)
        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()
        
        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)
        
        
  
