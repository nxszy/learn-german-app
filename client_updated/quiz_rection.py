from kivymd.uix.menu import MDDropdownMenu
from quiz_base import QuizBase

class QuizRection(QuizBase):

    menu = None
    tf_ids = ["inf", "pre", "cs"]
    points_per_screen = 3

    def on_enter(self):
        super().on_enter()
        self.create_menu()

    def create_menu(self):
        menu_items = [
            {
                "text": txt,
                "on_release": lambda x = txt: self.menu_callback(x)
            } for txt in ("Akkusativ", "Dativ")
        ]
        
        self.menu = MDDropdownMenu(
            caller = self.ids.cs, 
            items = menu_items,
            position = "center",
        )
    
    def menu_callback(self, txt):
        if self.menu:
            self.ids["cs"].text = txt
            self.menu.dismiss()