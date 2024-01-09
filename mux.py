import os
import socket
from kivy.config import Config
Config.set('graphics', 'rotation', '0')
Config.set('graphics', 'borderless', '0')
Config.set('graphics', 'width', '1480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'resizable', '1')
Config.write()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons

def get_ip_address():
    try:
        # Create a socket to connect to an Internet host
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # Connect the socket to a remote server
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
    except:
        return 'No IP Found'

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDBottomNavigation:
        id: bottom_navigation

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Power'
            icon: 'flash'

            MDLabel:
                text: 'Power tab content here'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Ethernet'
            icon: 'lan'

            MDLabel:
                text: app.ethernet_content
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Serial'
            icon: 'serial-port'

            MDLabel:
                text: 'Serial tab content here'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Settings'
            icon: 'cog'

            MDLabel:
                text: 'Settings tab content here'
                halign: 'center'
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.ethernet_content = "Ethernet IP Address: " + get_ip_address()
        return Builder.load_string(KV)

Example().run()
