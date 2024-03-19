from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationbar import MDNavigationBar
from kivymd.app import App

class QuizManager(MDScreenManager):

    learningSet = {}

class QuizHomeScreen(MDScreen):

    def on_pre_enter(self):
        
        app = App.get_running_app()
        home_screen = app.root.get_screen('home')
        bottom_nav = home_screen.ids.bottom_nav

        bottom_nav.opacity = 0