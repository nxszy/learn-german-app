from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from os import listdir, path

import welcome_screen, login, register, home, learning_mode, learning_set, quiz_conjugation, quiz_pastforms, quiz_rection, results

for file in listdir("./client_updated/kv_files"):
    f = path.join("./client_updated/kv_files/", file)
    Builder.load_file(f)

class MainManager(MDScreenManager):
    pass

class App(MDApp):
    def build(self):
        Window.size = (420, 640)
        self.title = "Gerb"
 
        mainSM = MainManager()
        
        return mainSM

if __name__ == "__main__":
    
    App().run()