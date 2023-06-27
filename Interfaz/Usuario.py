from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window
from kivymd.uix.selectioncontrol import MDCheckbox
import requests

Window.size = (350, 580)

class Ui(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Pink'
        Builder.load_file("login.kv")

        return Ui()




if __name__ == "__main__":
    MainApp().run()

