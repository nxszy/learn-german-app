from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.config import Config
from os import listdir, path

Config.set('graphics', 'resizable', False)

for file in listdir("./client/kv_files"):
    f = path.join("./client/kv_files/", file)
    Builder.load_file(f)

class Login(MDScreen):
    pass

class Register(MDScreen):
    pass

class Menu(MDScreen):
    pass

class Learning(MDScreen):
    pass

class ConjugationHomeScreen(MDScreen):
    pass

class PastFormsHomeScreen(MDScreen):
    pass

class RectionHomeScreen(MDScreen):
    pass

class Tests(MDScreen):
    pass

class Profile(MDScreen):
    pass

class UserSettings(MDScreen):
    pass

class Manager(MDScreenManager):
    pass

class LearningManager(MDScreenManager):
    pass

class ProfileManager(MDScreenManager):
    pass

class app(MDApp):
    def build(self):
        Window.size = (420, 640)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Teal"
        self.title = "Gerb"
        sm = Manager()
    
        return sm
    
LabelBase.register(name="preah", fn_regular="./server/media/fonts/Preahvihear-Regular.ttf")

app().run()