from kivy.app import App
from kivy.uix.actionbar import ActionBar
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView,FileChooserIconView
import os
from kivy.properties import ObjectProperty

class MyApp(App):
    title = 'Notepad'
    icon = 'static/icons/notepad.png'
    def build(self):
        return Notepad()


class Notepad(BoxLayout):
    data = ObjectProperty(None)

    def new_file(self):
        pass


    def open_file(self):
        return MyPopup_open_file().open()

    def save_file(self):
        pass


"""************************************************************************************************************"""

class MyPopup_open_file(Popup):
    def btn_cancel(self):
        self.dismiss()

    def btn_open(self, path, filename):
        self.f = open(os.path.join(path, filename[0]), 'r+')
        self.data_open = self.f.read()
        Notepad.data = self.data_open
        print(Notepad.data)
        self.f.close()
        self.dismiss()



"""***************************************************************************************************************"""
if __name__ == "__main__":
    MyApp().run()