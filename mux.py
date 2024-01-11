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
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.button import MDFloatingActionButton
from kivy.clock import Clock
from datetime import datetime


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

class SquareCard(MDCard):
    def __init__(self, **kwargs):
        super(SquareCard, self).__init__(**kwargs)
        self.size_hint = (None, 0.5)
        self.bind(size=self.update_size)  # Bind size to update_size method
        self.elevation = dp(0)
        self.soft_shadow_cl = [0, 0, 0, .05]
        self.radius = dp(10)
        self.md_bg_color = "darkgrey"
        self.unfocus_color = "darkgrey"
        self.focus_color = "grey"
        self.ripple_behavior = True
    def update_size(self, instance, value):
        self.width = self.height  # Set width equal to height
        
KV = '''
BoxLayout:
    orientation: 'vertical'
    
    MDTopAppBar:
        id: time_label
        md_bg_color: app.theme_cls.primary_color
        elevation: 0
        right_action_items: [['git', lambda x: app.on_git_button_press()], ['power', lambda x: app.on_power_button_press()]]

    MDBottomNavigation:
        id: bottom_navigation
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Power'
            icon: 'flash'

            BoxLayout:
                orientation: 'vertical'
                padding: "5dp"

                ScrollView:
                    do_scroll_y: False
                    size_hint: 1, 1
                    adaptive_width: True
                    MDGridLayout:
                        rows: 1
                        row_force_default: False
                        size_hint: 1, 1
                        spacing: dp(15)
                        padding: dp(15)
                        adaptive_width: True

                        SquareCard:
                            on_release: app.show_dialog()
                            MDLabel:
                                text: "Power 1"
                                halign: "center"
                        SquareCard:
                            on_release: app.show_dialog()
                            MDLabel:
                                text: "Power 2"
                                halign: "center"
                        SquareCard:
                            on_release: app.show_dialog()
                            MDLabel:
                                text: "Power 3"
                                halign: "center"
                        SquareCard:
                            on_release: app.show_dialog()
                            MDLabel:
                                text: "Power 4"
                                halign: "center"
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
                            on_release: app.show_dialog()
                        SquareCard:
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
                    elevation: 0
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
                    elevation: 0
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
                    elevation: 0

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
                        on_release=self.close_dialog  # Bind close_dialog method
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog  # Bind close_dialog method
                    ),
                ],
                items=[MDChip(text=f"Chip {i}") for i in range(5)]
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()  # This will close the dialog

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

    def on_power_button_press(self, *args):
        try:
            subprocess.run(['sudo', 'shutdown', 'now'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to reboot: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def on_git_button_press(self, *args):
        try:
            subprocess.run(['git', '-C', '/home/sam/mux', 'pull'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to reboot: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        self.root.ids.time_label.title = datetime.now().strftime('%H:%M:%S')
Example().run()

