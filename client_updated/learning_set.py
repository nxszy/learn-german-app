from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from functools import partial
import requests

class LearningSet(MDScreen):

    buttonBox = None
    
    def on_enter(self, *args):

        self.buttonBox = MDBoxLayout(orientation="vertical", spacing="5dp", size_hint=(1,1), pos_hint={"center_x":0.5, "top":1})
        
        default_btn = MDButton(MDButtonText(text="Default",pos_hint={"center_x":.5, "center_y":.5}), 
                               id="0", style="elevated", theme_width="Custom", 
                               size_hint=(None, None), width="300", pos_hint={"center_x":0.5, "top":.95}, 
                               on_release=partial(self.handle_set_button, 0),)
        
        default_btn_top10 = MDButton(MDButtonText(text="Top 10",pos_hint={"center_x":.5, "center_y":.5}), 
                               id="0", style="elevated", theme_width="Custom", 
                               size_hint=(None, None), width="300", pos_hint={"center_x":0.5, "top":.95}, 
                               on_release=partial(self.handle_set_button, 1),)
    
        self.buttonBox.add_widget(default_btn)
        self.buttonBox.add_widget(default_btn_top10)

        self.ids['set_list'].add_widget(self.buttonBox)

    def handle_set_button(self, id, instance):

        self.get_learning_set(id)
        self.manager.current = self.manager.mode

    def get_learning_set(self, id):
        self.manager.learningSet.clear()

        if self.manager.mode == "conjugation":

            match id:
                case 0:
                    verbs = requests.get('http://127.0.0.1:8000/verbs/conjugation').json()
                case 1:
                    verbs = requests.get('http://127.0.0.1:8000/verbs/conjugation').json()[:10]
            
            for i, verb in enumerate(verbs):
                self.manager.learningSet[i] = [verb['translation'], verb['infinitive'], 
                                        verb['sg_Ip_form'], verb['sg_IIp_form'], verb['sg_IIIp_form'],
                                        verb['pl_Ip_form'], verb['pl_IIp_form'], verb['pl_IIIp_form']]
        
        elif self.manager.mode == "past_forms":

            match id:
                case 0:
                    verbs = requests.get('http://127.0.0.1:8000/verbs/past-forms').json()
                case 1:
                    verbs = requests.get('http://127.0.0.1:8000/verbs/past-forms').json()[:10]

            for i, verb in enumerate(verbs):
                self.manager.learningSet[i] = [verb['translation'], verb['infinitive'], 
                                        verb['prateritum'], verb['partizip2']]
                    

    def on_leave(self):
        self.ids['set_list'].clear_widgets()