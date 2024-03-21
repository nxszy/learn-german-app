from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from functools import partial
from kivymd.uix.widget import Widget
from kivymd.app import App

class QuizConjugation(MDScreen):

    dialog = None

    points = 0
    iter = NumericProperty(0)

    tf_ids = ["inf", "sg_I", "sg_II", "sg_III", "pl_I", "pl_II", "pl_III"]
    
    def on_pre_enter(self):
        
        app = App.get_running_app()
        home_screen = app.root.get_screen('home')
        bottom_nav = home_screen.ids.bottom_nav

        bottom_nav.opacity = 0

    def on_enter(self):
        self.iter = 0
        self.ids['progress_bar'].value = self.iter
        self.ids['progress_bar'].max = len(self.manager.learningSet)
        self.reset_screen()

    def check_content(self):

        if self.ids['check_text'].text == "Check":

            for i, id in enumerate(self.tf_ids):

                correct_form =  self.manager.learningSet[self.iter][i+1]
                
                if self.ids[id].text != correct_form:
                    self.ids[id].text = correct_form
                    self.ids[id].error = True
                else:
                    self.points += 1/7

            self.iter += 1
            self.ids['progress_bar'].value = self.iter
            
            if self.iter < len(self.manager.learningSet):
                self.ids['check_text'].text = "Next"
            else:
                self.ids['check_text'].text = "Results"
        
        elif self.ids['check_text'].text == "Next":
            self.reset_screen()

        elif self.ids['check_text'].text == "Results":

            max_points = len(self.manager.learningSet) * 7 

            percent = (round(self.points,1) / max_points)

            mess = self.manager.get_screen('resultsScreen').ids['message']
            if 0.0 <= percent < 0.5:
                mess.text = 'You can do better!'
            elif 0.5 <= percent < 0.65:
                mess.text = 'There\'s still \n room for improvment!'
            elif 0.65 <= percent < 0.85:
                mess.text = 'Great job! Keep learning!'
            else:
                mess.text = 'Congrats! You rock!'

            self.manager.get_screen('resultsScreen').ids['result'].text = f"You got \n {round(self.points,1)} / {max_points} \n That's {(round(self.points,1) / max_points)*100}%"
            self.manager.current = 'resultsScreen'
    
    def on_cancel_button(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Do you want to leave?",
                    halign="left",
                ),
                MDDialogSupportingText(
                    text="All progress will be lost.",
                    halign="left",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Leave",), on_release=partial(self.handle_dialog, 0)
                    ),
                    MDButton(
                        MDButtonText(text="Cancel",), on_release=partial(self.handle_dialog, 1)
                    ),
                ),
                size_hint=(0.85, None),
            )
        self.dialog.open()
    
    def handle_dialog(self, response, instance):

        if response == 0:            
            self.ids['progress_bar'].value = 0
            self.manager.current = 'learnMode'
        self.dialog.dismiss()

    def reset_screen(self):

        self.ids["r_word"].text = self.manager.learningSet[self.iter][0]

        for id in self.tf_ids:
            self.ids[id].error = False
            self.ids[id].text = ""
        
        self.ids['check_text'].text = "Check"