from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen, MDScreen
from kivymd.uix.screenmanager import MDScreenManager

KV = '''
MDScreenManager:
    MDScreen:
        name: 'page1'

        MDLabel:
            text: 'Page 1'
            halign: 'center'

        MDFloatingActionButton:
            icon: 'arrow-right'
            pos_hint: {'center_x': 0.9, 'center_y': 0.1}
            on_release: root.current = 'page2'

    MDScreen:
        name: 'page2'

        MDLabel:
            text: 'Page 2'
            halign: 'center'

        MDFloatingActionButton:
            icon: 'arrow-left'
            pos_hint: {'center_x': 0.1, 'center_y': 0.1}
            on_release: root.current = 'page1'
'''

class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

MyApp().run()
