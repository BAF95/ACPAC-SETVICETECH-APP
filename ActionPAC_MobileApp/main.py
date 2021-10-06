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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.properties import *
import os
from datetime import datetime
import csv

class MainWindow(Screen):
    pass



class FirstWindow(Screen):
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
class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):

    def Submitmore(self):
        startlist = [self.ids.Start1, self.ids.Start2, self.ids.Start3, self.ids.Start4,
                     self.ids.Start5]
        techlist = [self.ids.Tech1, self.ids.Tech2, self.ids.Tech3, self.ids.Tech4,
                     self.ids.Tech5]
        datelist = [self.ids.Date1, self.ids.Date2, self.ids.Date3, self.ids.Date4,
                    self.ids.Date5]
        stoplist = [self.ids.Stop1, self.ids.Stop2, self.ids.Stop3, self.ids.Stop4,
                    self.ids.Stop5]
        startam1list = [self.ids.StartAM1.active, self.ids.StartAM2.active, self.ids.StartAM3.active,
                        self.ids.StartAM4.active, self.ids.StartAM5.active]
        stopam1list = [self.ids.StopAM1.active, self.ids.StopAM2.active, self.ids.StopAM3.active,
                       self.ids.StopAM4.active, self.ids.StopAM5.active]
        hrslist = [self.ids.Hrs1, self.ids.Hrs2, self.ids.Hrs3, self.ids.Hrs4, self.ids.Hrs5]
        othrslist = [self.ids.OThrs1, self.ids.OThrs2, self.ids.OThrs3, self.ids.OThrs4, self.ids.OThrs5]

        date = datetime.now()
        now = date.strftime("%m-%d")
        details = ["Date", "Tech", "Start", "StartAM?", "Stop", "StopAM?", "HRS", "OT HRS"]
        rows = []
        for i in range(0,5):
            rowlist = []
            rowlist.append(datelist[i].text)
            rowlist.append(techlist[i].text)
            rowlist.append(startlist[i].text)
            if startam1list[i] == True:
                rowlist.append("AM")
            else:
                rowlist.append("PM")
            rowlist.append(stoplist[i].text)
            if stopam1list[i] == True:
                rowlist.append("AM")
            else:
                rowlist.append("PM")
            rowlist.append(hrslist[i].text)
            rowlist.append(othrslist[i].text)
            rows.append(rowlist)

        try:


            with open(f"{now}.csv", "a") as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(details)

                # write multiple rows
                writer.writerows(rows)
            for i in range(0,5):
                datelist[i].text = ""
                techlist[i].text = ""
                startlist[i].text = ""
                stoplist[i].text = ""
                hrslist[i].text = ""
                othrslist[i].text = ""



        except:
            os.mkdir(f"{now}.csv")
            with open(f"{now}.csv", "a") as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(details)

                # write multiple rows
                writer.writerows(rows)
            for i in range(0,5):
                datelist[i].text = ""
                techlist[i].text = ""
                startlist[i].text = ""
                stoplist[i].text = ""
                hrslist[i].text = ""
                othrslist[i].text = ""





    def CalcHours(self):
        startlist = [self.ids.Start1.text, self.ids.Start2.text, self.ids.Start3.text, self.ids.Start4.text, self.ids.Start5.text]
        stoplist = [self.ids.Stop1.text, self.ids.Stop2.text, self.ids.Stop3.text, self.ids.Stop4.text, self.ids.Stop5.text]
        startam1list = [self.ids.StartAM1.active, self.ids.StartAM2.active, self.ids.StartAM3.active,self.ids.StartAM4.active,self.ids.StartAM5.active]
        stopam1list = [self.ids.StopAM1.active, self.ids.StopAM2.active, self.ids.StopAM3.active,self.ids.StopAM4.active,self.ids.StopAM5.active]
        hrslist = [self.ids.Hrs1, self.ids.Hrs2, self.ids.Hrs3, self.ids.Hrs4, self.ids.Hrs5]
        othrslist = [self.ids.OThrs1, self.ids.OThrs2, self.ids.OThrs3, self.ids.OThrs4, self.ids.OThrs5]

        for i in range(0, 5):
            print(i)
            start = startlist[i]
            stop = stoplist[i]
            if start == '':
                i += 1

            elif stop =='':
                i += 1

            else:

                # converts start/stop to int
                start = int(start)
                stop = int(stop)

                final = 0

                if startam1list[i] == True:

                    if stopam1list[i] == False:
                        count = 0
                        while start < 12:
                            start += 1
                            count += 1
                        if stop != 12:
                            final = final + count + stop
                        else:
                            final = count


                        if final > 8:
                            print("Should be 8 + OT")
                            hrslist[i].text = "8"
                            final -= 8
                            othrslist[i].text = f"{final}"
                            i+=1
                            print(i)
                        else:
                            hrslist[i].text = f"{final}"
                            othrslist[i].text = ""
                            i+=1
                    else:
                        final = stop - start

                        hrslist[i].text = f"{final}"
                        othrslist[i].text = ""
                        i+=1

                else:
                    if start == 12:
                        if stop > 8:
                            hrslist[i].text = "8"
                            stop -= 8
                            othrslist[i].text = f"{stop}"
                            i+=1
                        else:
                            hrslist[i].text = f"{stop}"
                            othrslist[i].text = ""
                            i+=1
                    else:
                        final = stop-start
                        if final > 8:
                            hrslist[i].text = "8"
                            final -= 8
                            othrslist[i].text = f"{final}"
                            i+=1
                        else:
                            hrslist[i].text = f"{final}"
                            othrslist[i].text = ""
                            i+=1









    def checkbox_click(self, instance, value, time):
        if value == True:
            print(time)
        else:
            print("PM")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("layout.kv")




class ACPAC(App):
    def build(self):
        return kv






if __name__ == "__main__":
    ACPAC().run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
