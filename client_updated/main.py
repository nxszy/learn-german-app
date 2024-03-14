from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from os import listdir, path

import welcome_screen, login, register

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
        sm.add_widget(welcome_screen.WelcomeScreen())
        sm.add_widget(login.LoginScreen())
        sm.add_widget(register.RegisterScreen())
        return sm

if __name__ == "__main__":
    
    App().run()