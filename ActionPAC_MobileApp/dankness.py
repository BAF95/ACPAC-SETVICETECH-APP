from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import StringProperty

class PopupBttn(Button):
    def openPopup(self):
        print(self.name)
        Pop = TextPopup().open(self.text, self.name)


class TextPopup(Popup):
    bttnid = StringProperty()
    text = StringProperty()
    def open(self, text, id, **kwargs):
        super(TextPopup, self).open(**kwargs)
        self.ids.txtipt.text = text
        self.bttnid = id

    def setText(self):
        App.get_running_app().root.ids[self.bttnid].text = self.text

class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()