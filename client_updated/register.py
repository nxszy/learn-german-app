from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.widget import Widget

class RegisterScreen(MDScreen):

    dialog = None
    
    def handle_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="You can now log in with provided credentials!",
                    halign="left",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="OK"),
                        style="text",
                        on_release=self.handle_button,
                    ),
                ),
            )
        self.dialog.open()

    def handle_button(self, instance):
        self.dialog.dismiss()
        self.manager.current = "login"