from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from os import listdir, path
from functools import partial

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

class LearningHome1(MDScreen):
    
    def handle_button(self, id):
        print(id)
        match str(id):
            case "learn_Conj":
                self.manager.learningChosen = "conj"
            case "learn_Past":
                self.manager.learningChosen = "pastforms"
            case "learn_Rection":
                self.manager.learningChosen = "rection"

        if self.manager.learningChosen:
            self.manager.current = "learningHome2"
            
class LearningHome2(MDScreen):

    btnBox = None
    
    def on_enter(self, *args):

        box = BoxLayout(orientation="vertical", spacing="5dp")
        self.btnBox = box
        
        default_btn = MDRaisedButton(id="0", text="default", size_hint=(1, None), height="300", on_release=partial(self.handle_set_button))
        box.add_widget(default_btn)

        self.ids['setList'].add_widget(box)
    
    def handle_set_button(self, id):
        
        self.manager.verbsSet = [] # get request w zależności od pId z bazy - id guzika to pId w bazie

        self.manager.current = self.manager.learningChosen

    def on_leave(self):
        self.ids['setList'].remove_widget(self.btnBox)


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
    
    learningChosen = ""
    verbsSet = []

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