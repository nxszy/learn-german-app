from kivymd.uix.screen import MDScreen
from kivy.app import App

class ResultsScreen(MDScreen):
    
    def on_leave(self):

        app = App.get_running_app()
        home_screen = app.root.get_screen('home')
        bottom_nav = home_screen.ids.bottom_nav

        bottom_nav.opacity = 1