from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from os import listdir, path
from functools import partial
import requests
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView

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
        
        default_btn = MDRaisedButton(id="0", text="default", size_hint=(1, None), height="300", on_release=partial(self.handle_set_button, 0))
        box.add_widget(default_btn)

        self.ids['setList'].add_widget(box)
    
    def handle_set_button(self, id, instance):
        
        self.get_learning_set(id)
        # get request w zależności od pId z bazy - id guzika to pId w bazie

        self.manager.current = self.manager.learningChosen

    def on_leave(self):
        self.ids['setList'].remove_widget(self.btnBox)

    def get_learning_set(self, id):
        match id:
            case 0:
                verbs = requests.get('http://127.0.0.1:8000/conj/').json()
        
        for i, verb in enumerate(verbs):
            self.manager.learningSet[i] = [verb['translation'], verb['infinitive'], 
                                    verb['sg_Ip_form'], verb['sg_IIp_form'], verb['sg_IIIp_form'],
                                    verb['pl_Ip_form'], verb['pl_IIp_form'], verb['pl_IIIp_form']]

class ConjugationHomeScreen(MDScreen):

    dialog = None

    iter = 0

    btn_ids = ["inf", "sg_I", "sg_II", "sg_III", "pl_I", "pl_II", "pl_III"]

    def on_pre_enter(self):
        self.reset_screen()

    def check_content(self):

        c_btn = self.ids['conj_check_button']
        
        if c_btn.text == "Check":

            for i, id in enumerate(self.btn_ids):

                correct_form =  self.manager.learningSet[self.iter][i+1]
                
                if self.ids[id].text != correct_form:
                    self.ids[id].text = correct_form
                    self.ids[id].error = True
                else:
                    pass

            self.iter += 1
            
            if self.iter < len(self.manager.learningSet):
                c_btn.text = "Next"
            else:
                c_btn.text = "Results"
        
        elif c_btn.text == "Next":
            self.reset_screen()

        elif c_btn.text == "Results":
            self.manager.current = 'ResultsScreen'
    
    def on_cancel_button(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Do you want to leave?",
                text="All progress will be lost.",
                size_hint=(0.85, None),
                buttons=[
                    MDRaisedButton(
                        text="Leave", on_release=partial(self.handle_dialog, 0)
                    ),
                    MDRaisedButton(
                        text="Cancel", on_release=partial(self.handle_dialog, 1)
                    ),
                ],
            )
        self.dialog.open()
    
    def handle_dialog(self, response, instance):
        if response == 0:
            self.manager.current = "learningHome1"
        elif response == 1:
            self.reset_screen()
        self.dialog.dismiss()

    def reset_screen(self):

        self.ids["r_word"].text = self.manager.learningSet[self.iter][0]

        for id in self.btn_ids:
            self.ids[id].error = False
            self.ids[id].text = ""
        
        self.ids["conj_check_button"].text = "Check"
    

class PastFormsHomeScreen(MDScreen):
    pass

class RectionHomeScreen(MDScreen):
    pass

class ResultsScreen(MDScreen):
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
    learningSet = {}

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