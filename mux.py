import os
import socket
import subprocess
from kivy.config import Config
Config.set('graphics', 'rotation', '90')
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
                            max: 245
                            value: 100  # Default value
                            on_value: app.adjust_brightness(self.value)

'''

class Example(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        self.current_brightness = self.read_brightness_value()
        
    def read_brightness_value(self):
        try:
            with open('brightness_setting.txt', 'r') as file:
                return int(file.read().strip())
        except Exception as e:
            print(f"Error reading brightness value: {e}")
            # Return default value if there's an error
            return 0
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.ethernet_content = "Ethernet IP Address: " + get_ip_address()

        root_widget = Builder.load_string(KV)
        slider_value = 245 - self.current_brightness
        root_widget.ids.brightness_slider.value = slider_value

        return root_widget


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
        # Invert the brightness value with 245 as the minimum
        inverted_brightness_value = 245 - int(value)
        self.current_brightness = inverted_brightness_value

        command = f'echo {self.current_brightness} > /sys/waveshare/rpi_backlight/brightness'
        
        try:
            subprocess.run(['sudo', 'bash', '-c', command], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error adjusting brightness: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Save brightness value to a file
        self.save_brightness_value(self.current_brightness)

    def save_brightness_value(self, value):
        try:
            with open('brightness_setting.txt', 'w') as file:
                file.write(str(value))
        except Exception as e:
            print(f"Error saving brightness value: {e}")


Example().run()

