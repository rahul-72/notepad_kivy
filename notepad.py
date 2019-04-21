from kivy.app import App
from kivy.uix.actionbar import ActionBar
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView

class MyApp(App):
    title = 'Notepad'
    icon = 'static/icons/notepad.png'
    def build(self):
        return Notepad()


class Notepad(BoxLayout):
    def new_file(self):
        pass


    def open_file(self):
        return MyPopup_open_file().open()

    def save_file(self):
        pass


"""************************************************************************************************************"""

class MyPopup_open_file(Popup):
    def btn_cancel(self):
        pass

    def btn_open(self, path, filename):
        pass


"""***************************************************************************************************************"""
if __name__ == "__main__":
    MyApp().run()