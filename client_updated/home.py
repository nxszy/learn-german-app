from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivy.properties import StringProperty

import learningSet, learningMode

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

class ProfileHomeScreen(MDScreen):
    pass

class LearningHomeScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
    
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        print(item_text)
        if item_text != 'Learn':
           self.ids.screen_manager.get_screen('Learn').ids.learning_manager.current = 'learnMode'
        self.ids.screen_manager.current = item_text
