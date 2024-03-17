from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from functools import partial

class LearningSet(MDScreen):

    buttonBox = None
    
    def on_enter(self, *args):

        box = MDBoxLayout(orientation="vertical", spacing="5dp")
        self.btnBox = box
        
        default_btn = MDButton(MDButtonText(text="Default",), id="0", style="elevated", size_hint=(1, None), height="300", on_release=partial(self.handle_set_button, 0),)
        box.add_widget(default_btn)

        self.ids['setList'].add_widget(box)

    def handle_set_button(self, instance, id):
        pass