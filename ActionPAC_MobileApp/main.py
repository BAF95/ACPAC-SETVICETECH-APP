# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.properties import StringProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    terms = ObjectProperty(None)
    termInput = ObjectProperty(StringProperty)

    def checkbox_click(self, instance, value, terms):


        if value == True:
            print(terms)
            self.ids.termInput.text = f'{terms}'

# class Screen_One(Screen):
#     pass
#
# class Screen_Two(Screen):
#     pass




class layout(App):
    def build(self):
        return MyGrid()






if __name__ == "__main__":
    layout().run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
