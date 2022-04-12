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
         
     def update_chat_history(self, message):
         self.chat_history.text += '\n' + message 
         self.layout.height = self.chat_history.texture_size[1] + 15
         self.chat_history.height = self.chat_history.texture_size[1]
         self.chat_history.text_size = (self.chat_history.width * 0.98, None)
         self.scroll_to(self.scroll_to_point)
         
      def update_chat_history_layout(self, _=None):
         self.layout.height = self.chat_history.texture_size[1] + 15
         self.chat_history.height = self.chat_history.texture_size[1]
         self.chat_history.text_size = (self.chat_history.width * 0.98, None)
         

class ConnectPage(GridLayout):
   
   def __init__(self, **Kwargs):
       super(). __init__(*kwargs)
       if os.path.isfile('prev_details.txt', 'r') as f:
          with open('prev_details.txt', 'r') as f:
               d = f.read().split(",")
               prev = {'ip: d[0], 'port': d}
   else:
        prev = {'ip': '', 'port': d[1], 'username': d[2]}
   self.cols = 2
   self.add_widget(label(text="IP: "))
   self.ip = TextInput(text=pev['ip'], multiline-False)
   self.add_widget(self.ip)
   self.add_widget(Label(text="Port: "))
   self.port = TextInput(text=prev['port'], multiline=False)
   self.add_widget(self.port)
   self.add_widget(Label(text="Username: "))
   self.username = TextInput(text=prev['username'], multiline=False)
   self.add_widget(self.username)
   self.join = Button(text="Join")
   self.join.bind(on_press=self.join_button)
   self.add_widget(Label())
   self.add_widget(self.join)   
                                            
def join_button(self, instance):
    port = self.port.text
    ip = self.ip.text  
    username = self.username.text
    with open('prev_details.text', 'w') as f:
         f.write(f'{ip},{port},{username}')
    info = f'Trying to join {ip}:{port} as {username}'
    chat_app.info_page.update_info(info)
    chat_app.screen_manager.current = "Info"
    Clock.schedule_once(self.connect, 1)  
                       
def connect(self, _):
    port = int(self.port.text)
    ip = self.ip.text
    username = self.username.text
    if not socket_client.connect(ip, port, username, show_error):
       return
    else:
        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'Chat'
                       
                       
class InfoPage(GridLayout):
                       
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign='center', valign='middle', font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)     
                       
                       
                       
