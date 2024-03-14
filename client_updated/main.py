from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from os import listdir, path

import login

for file in listdir("./client_updated/kv_files"):
    f = path.join("./client_updated/kv_files/", file)
    Builder.load_file(f)

class MainManager(MDScreenManager):
    pass

class App(MDApp):
    def build(self):
        Window.size = (420, 640)
        self.title = "Gerb"

        sm = MainManager()
        return sm

if __name__ == "__main__":
    App().run()