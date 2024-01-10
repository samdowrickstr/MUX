import os
import socket
from kivy.config import Config
Config.set('graphics', 'rotation', '90')
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'width', '1480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'resizable', '0')
Config.write()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
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

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'screen 1'
            MDLabel:
                text: 'Power tab content here'
                halign: 'center'

        Screen:
            name: 'screen 2'
            MDLabel:
                text: app.ethernet_content
                halign: 'center'

        Screen:
            name: 'screen 3'
            MDLabel:
                text: 'Serial tab content here'
                halign: 'center'

        Screen:
            name: 'screen 4'
            MDLabel:
                text: 'Settings tab content here'
                halign: 'center'

    MDBottomNavigation:
        id: bottom_navigation

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Power'
            icon: 'flash'
            on_tab_release: screen_manager.current = self.name

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Ethernet'
            icon: 'lan'
            on_tab_release: screen_manager.current = self.name

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Serial'
            icon: 'serial-port'
            on_tab_release: screen_manager.current = self.name

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Settings'
            icon: 'cog'
            on_tab_release: screen_manager.current = self.name
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.ethernet_content = "Ethernet IP Address: " + get_ip_address()
        return Builder.load_string(KV)

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

Example().run()
