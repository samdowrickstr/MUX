import os
from kivy.config import Config
Config.set('graphics', 'rotation', '90')
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'width', '1480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'resizable', '0')
Config.write()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons

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
                text: 'Ethernet tab content here'
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
        return Builder.load_string(KV)

Example().run()

