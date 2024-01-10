import os
import socket

from kivy.config import Config
Config.set('graphics', 'rotation', '0')
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'width', '1480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'resizable', '0')
Config.write()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.chip import MDChip
from kivymd.uix.slider import MDSlider

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
    MDBottomNavigation:
        id: bottom_navigation
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Power'
            icon: 'flash'

            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: 'Power tab content here'
                    halign: 'center'

                MDCard:
                    size_hint: None, None
                    size: "280dp", "40dp"
                    pos_hint: {"center_x": 0.5}
                    elevation: 10
                    MDFlatButton:
                        text: "Open Dialog"
                        on_release: app.show_dialog()
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Ethernet'
            icon: 'lan'

            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: 'Power tab content here'
                    halign: 'center'

                MDCard:
                    size_hint: None, None
                    size: "280dp", "40dp"
                    pos_hint: {"center_x": 0.5}
                    elevation: 10
                    MDFlatButton:
                        text: "Open Dialog"
                        on_release: app.show_dialog()
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Serial'
            icon: 'serial-port'

            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: 'Power tab content here'
                    halign: 'center'

                MDCard:
                    size_hint: None, None
                    size: "280dp", "40dp"
                    pos_hint: {"center_x": 0.5}
                    elevation: 10
                    MDFlatButton:
                        text: "Open Dialog"
                        on_release: app.show_dialog()
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Settings'
            icon: 'cog'

            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: 'Settings tab content here'
                    halign: 'center'

                MDCard:
                    size_hint: None, None
                    size: "280dp", "120dp"
                    pos_hint: {"center_x": 0.5}
                    elevation: 10

                    BoxLayout:
                        orientation: 'vertical'
                        padding: "10dp"

                        MDLabel:
                            text: 'Adjust Brightness'
                            halign: 'center'

                        MDSlider:
                            id: brightness_slider
                            min: 0
                            max: 255
                            value: 100  # Default value
                            on_value: app.adjust_brightness(self.value)

'''

class Example(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.ethernet_content = "Ethernet IP Address: " + get_ip_address()
        return Builder.load_string(KV)

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Choose an Option",
                type="simple",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
                items=[MDChip(text=f"Chip {i}") for i in range(5)]
            )
        self.dialog.open()

    def adjust_brightness(self, value):
        # Adjust the screen brightness
        brightness_value = int(value)
        try:
            with open('/sys/waveshare/rpi_backlight/brightness', 'w') as file:
                file.write(f'{brightness_value}')
        except Exception as e:
            print(f"Error adjusting brightness: {e}")

Example().run()

