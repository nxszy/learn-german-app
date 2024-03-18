from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from functools import partial

class LearningSet(MDScreen):

    buttonBox = None
    
    def on_enter(self, *args):

        self.buttonBox = MDBoxLayout(orientation="vertical", spacing="5dp", size_hint=(.9,.9), pos_hint={"center_x":0.5, "top":1})
        
        default_btn = MDButton(MDButtonText(text="Default",pos_hint={"center_x":.5, "center_y":.5}), 
                               id="0", style="elevated", theme_width="Custom", 
                               size_hint=(None, None), width="300", pos_hint={"center_x":0.5, "top":.95}, 
                               on_release=partial(self.handle_set_button, 0),)
    
        self.buttonBox.add_widget(default_btn)

        self.ids['set_list'].add_widget(self.buttonBox)

    def handle_set_button(self, instance, id):

        self.manager.current = 'quizHome'
        self.manager.get_screen('quizHome').ids.quiz_manager.current = self.manager.mode

    def on_leave(self):
        self.ids['set_list'].clear_widgets()