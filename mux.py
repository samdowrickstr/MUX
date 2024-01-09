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
from kivymd.uix.button import MDFloatingActionButton

KV = '''
ScreenManager:
    MDScreen:
        name: 'page1'
        MDFloatingActionButton:
            icon: 'arrow-right'
            pos_hint: {'center_x': 0.9, 'center_y': 0.1}
            on_release: app.root.current = 'page2'
        MDFloatingActionButton:
            icon: 'close'
            pos_hint: {'center_x': 0.1, 'center_y': 0.9}
            on_release: app.terminate()

    MDScreen:
        name: 'page2'
        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x': 0.1, 'center_y': 0.1}
            on_release: app.root.current = 'page1'
        MDFloatingActionButton:
            icon: 'close'
            pos_hint: {'center_x': 0.9, 'center_y': 0.9}
            on_release: app.terminate()
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def terminate(self):
        os._exit(0)

MyApp().run()
