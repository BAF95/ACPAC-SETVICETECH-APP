# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Imports Dependancies
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
from kivy.graphics import *
import os
from jnius import autoclass
from datetime import datetime
import csv
import time
from fpdf import FPDF
import pandas as pd

# sets path for picture saving (initializing)
PATH = '.'
# sets absolute path for OS to save files
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
app_folder = os.path.dirname(os.path.abspath(__file__))
#camera out put directory
PATH = "/storage/emulated/0/DCIM"

# saves both picture output and pdf out put as pic_root/root
Environment = autoclass('android.os.Environment')
if Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED:
                #root = Environment.getExternalStorageDirectory().getAbsolutePath()
    pic_root = Environment.getExternalStoragePublicDirectory (Environment.DIRECTORY_PICTURES).getAbsolutePath() + '/'
title = 'ActionPac Service Report'
if Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED:
                #root = Environment.getExternalStorageDirectory().getAbsolutePath()
    root = Environment.getExternalStoragePublicDirectory (Environment.DIRECTORY_DOCUMENTS).getAbsolutePath() + '/'
    
#sets title for pdf
title = 'ActionPac Service Report'

#creates pdf instance DO NOT TOUCH YOU WILL BREAK IT
class PDF(FPDF):

    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self,label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6,(label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)



# intializes landing page
class MainWindow(Screen):
# function for on file report press (doesnt do anything at the moment)
    def filereport(self):
        now = datetime.now()
        now = now.strftime("%m-%d")
        # os.mkdir(f"{now}-report.rtf", "w")
        #pdf = PDF(unit="in")
        #pdf.add_page()
        #pdf.output(f'{now}-report.pdf', 'F')

# creates the customer inf opage
class FirstWindow(Screen):
# check function disables button "Next" until required fields are non-empty
    def check(self, text):

        if self.ids.Customer.text == "":
            pass


        elif self.ids.address.text == "":
            pass

        elif self.ids.date.text == "":
            pass

            pass
        elif self.ids.email.text == "":
            pass
        elif self.ids.contactName.text == "":
            pass
            
        elif self.ids.ProblemDesc.text == "":
            pass

        elif self.ids.ServiceDescription.text == "":
            pass


        elif self.ids.termInput == "PO":
            if self.ids.POBoxInput.text == "":
                pass
# else command activates if and only if all other fields are filled and dont pass
        else:
            self.ids.next1.disabled = False

    # name = ObjectProperty(None)
    # email = ObjectProperty(None)
    # terms = ObjectProperty(None)
    # termInput = ObjectProperty(StringProperty)
    def spinner_clicked(self, value):
        self.ids.termInput.text == f"{value}"
# country clicked handles the formatting and reformatting of the label names given the differing country ie in US Zip code is used but in Canada it's Postal code
    def country_clicked(self, value):
        time = datetime.now()
        time = time.strftime("%x")
        self.ids.date.text = f"{time}"
        self.ids.countryInput.text == f"{value}"
        if value == "Canada":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "City:"
            self.ids.addresslabel3.text = "Province:"
            self.ids.addresslabel4.text = "Postal Code:"
        if value == "USA":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "City:"
            self.ids.addresslabel3.text = "State:"
            self.ids.addresslabel4.text = "Zip Code:"
        if value == "Israel":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "City:"
            self.ids.addresslabel3.text = "State:"
            self.ids.addresslabel4.text = "Postal Code:"
            self.ids.state.text = "Israel"
        if value == "Australia":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "City:"
            self.ids.addresslabel3.text = "State:"
            self.ids.addresslabel4.text = "Postal Code:"
        if value == "Mexico":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "Municipality:"
            self.ids.addresslabel3.text = "City, State:"
            self.ids.addresslabel4.text = "Postal Code:"
        if value == "Chile":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "Locality:"
            self.ids.addresslabel3.text = "Country:"
            self.ids.addresslabel4.text = "Postal Code:"
            self.ids.state.text = "Chile"
        if value == "Portugal":
            self.ids.addresslabel1.text = "Street Address:"
            self.ids.addresslabel2.text = "Territorial Subdivision:"
            self.ids.addresslabel3.text = "Country:"
            self.ids.addresslabel4.text = "Postal Code:"
            self.ids.state.text = "Portugal"
        
        
        
# the function that saves all data in textfields for further use
    def submit(self):

#grabs time stamp for month-day
        now = datetime.now()
        now = now.strftime("%m-%d")
# saves all text in the texInput to a variable
        customer = self.ids.Customer.text
        address = self.ids.address.text
        date = self.ids.date.text
        email = self.ids.email.text
        contact = self.ids.contactName.text
        terminput = self.ids.termInput.text
        
        PO = self.ids.POBoxInput.text
        desc = self.ids.ProblemDesc.text
        serv = self.ids.ServiceDescription.text
        country = self.ids.countryInput.text
        zipcode = self.ids.zip.text
        city = self.ids.city.text
        state = self.ids.state.text
# unused experimental code creates a data frame (alternate to text files)
        cust_info = [customer, address, date, email, contact, terminput, desc, serv]
        cols = ["Customer Name", "Street Address", "Date", "Email", "Contact Name", "Terms",
        "Description of Problem", "Service Performed"]
        
        df = pd.DataFrame([{'Customer': customer},
                           {'Street Address': address},
                           {'Date': date},
                           {'Email': email},
                           {'Contact Name': email},
                           {'Terms': terminput},
                           {"PO": PO},
                           {"Description of Problem": desc},
                           {'Service Performed': serv}])
        
        #df.to_csv(f"Customer-{now}.csv")
            

#saves all text to a text file using f string to pass date          
        
        with open(f"{now}-service-desc.txt", "w") as f:
            f.write(f"Description of Problem: \n {desc}")
        with open(f"{now}-service-service.txt", "w") as f:
            f.write(f"Service Performed: \n {serv} ")

        with open(f"{now}-service-customer.txt", "w") as f:
            f.write(f"Customer: {customer} \n")


# saves the data differently depending on country         
        if country == "USA":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {city}, {state} {zipcode} \n")
                
        if country == "Canada":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {city}, {state} {zipcode} \n")
                
        if country == "Mexico":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {city} {zipcode} {state}  \n")
                
        if country == "Portugal":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {zipcode} {city} {state}  \n")
        
        if country == "Israel":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {city} {zipcode} {state} \n")
                
        if country == "Australia":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {city}, {state} {zipcode} \n")
        
        if country == "Chile":
            with open(f"{now}-service-address.txt", "w") as f:
                f.write(f"Address: {address} {zipcode} {city} {state} \n")
 
 
# saves the rest of the data       
        with open(f"{now}-service-date.txt", "w") as f:
            f.write(f"Date: {date} \n")
        with open(f"{now}-service-email.txt", "w") as f:
            f.write(f"EMAIL: {email} \n")
        with open(f"{now}-service-contact.txt", "w") as f:
            f.write(f"Contact: {contact} \n")
        with open(f"{now}-service-terms.txt", "w") as f:
            f.write(f"Terms: {terminput} \n")
            
        with open(f"{now}-service-PO.txt", "w") as f:
            if terminput == "PO":
                f.write(f"PO BOx: {PO} \n")
            
                
        

        # pdf = PDF.open(f'{now}-report.pdf')
        # pdf.set_xy(0.0, 0.0)
        # pdf.set_font('Arial', 'B', 16)
        # pdf.set_text_color(220, 50, 50)
        # pdf.cell(w=4, h=0.5, align='C', txt=f"{customer} Service Report")

    def checkbox_click(self, instance, value, terms):

        if value == True:
            print(terms)
            self.ids.termInput.text = f'{terms}'


# class Screen_One(Screen):
#     pass
#
# class Screen_Two(Screen):
#     pass

# instantiates the second window aka parts window
class SecondWindow(Screen):

# activates the saving (Maybe Deprecitated with submit function)
    def onpress(self):
        pricelist = [self.ids.price1, self.ids.price2, self.ids.price3, self.ids.price4,
                     self.ids.price5, self.ids.price6]
        quanlist = [self.ids.quan1, self.ids.quan2, self.ids.quan3, self.ids.quan4,
                    self.ids.quan5, self.ids.quan6]
        # ammountlist = [self.ids.ammount1, self.ids.ammount2, self.ids.ammount3, self.ids.ammount4,
        #                self.ids.ammount5, self.ids.ammount6]
        for i in range(0, 6):
            quan = quanlist[i].text
            price = pricelist[i].text
            if quan == '':
                i += 1
            elif price == '':
                i += 1
            else:
                quan = float(quan)
                price = float(price)
                total = price * quan
                # ammountlist[i].text = f"{total}"
# submit function saves all data to internal storage via a pandas dataframe
    def submit(self):
        quanlist = [self.ids.quan1, self.ids.quan2, self.ids.quan3, self.ids.quan4,
                    self.ids.quan5, self.ids.quan6, self.ids.quan7, self.ids.quan8, self.ids.quan9, self.ids.quan10]
        #partlist = [self.ids.part1, self.ids.part2, self.ids.part3, self.ids.part4,
                    #self.ids.part5, self.ids.part6, self.ids.part7, self.ids.part8, self.ids.part9]
        dclist = [self.ids.dc1, self.ids.dc2, self.ids.dc3, self.ids.dc4,
                  self.ids.dc5, self.ids.dc6, self.ids.dc7, self.ids.dc8, self.ids.dc9, self.ids.dc10]
        pricelist = [self.ids.price1, self.ids.price2, self.ids.price3, self.ids.price4,
                     self.ids.price5, self.ids.price6, self.ids.price7, self.ids.price8, self.ids.price9, self.ids.price10]
        # ammountlist = [self.ids.ammount1, self.ids.ammount2, self.ids.ammount3, self.ids.ammount4,
        #           self.ids.ammount5, self.ids.ammount6]
        date = datetime.now()
        now = date.strftime("%m-%d")
        
        try:
            #reads a dataframe
            df = pd.read_csv(f"Parts-{now}.csv")
            rowlist = []
#for every item get the text in the fields
            for i in range(0, 10):
                row = []
                quan = quanlist[i].text
                price = pricelist[i].text
                #partno = partlist[i].text
                dc = dclist[i].text
# if quantity or price is empty move on to the next item since calculation is impossible without both
                if quan == '':
                    i += 1
                elif price == '':
                    i += 1
                else:
                    total = float(price) * float(quan)
                    # ammount = ammountlist[i].text
                    row.append(quan)
                    #row.append(partno)
                    row.append(dc)
                    row.append(price)
                    row.append(f"{total}")
                    rowlist.append(row)
# append the row with the title to the data frame
            df = df.append(pd.DataFrame(rowlist, columns=["Quantity", "Description", "Price", "Amount"]))
#saves data to internal storage
            df.to_csv(f"Parts-{now}.csv")

# does everything commented above if the data frame doesnt already exist then creates data frame
        except:
            details = ["Quantity", "Description", "Price", "Amount"]
            rowlist = []

            for i in range(0, 6):
                row = []
                quan = quanlist[i].text
                price = pricelist[i].text
                #partno = partlist[i].text
                dc = dclist[i].text

                if quan == '':
                    i += 1
                elif price == '':
                    i += 1
                else:
                    total = float(price) * float(quan)
                    # ammount = ammountlist[i].text
                    row.append(quan)
                    #row.append(partno)
                    row.append(dc)
                    row.append(price)
                    row.append(f"{total}")
                    rowlist.append(row)
            df = pd.DataFrame(rowlist, columns=["Quantity", "Description", "Price", "Amount"])

            print(df)
            df.to_csv(f"Parts-{now}.csv")

            # df.append(series, ignore_index=True)
            # df.append(rowlist)
            # df["Quantity"] = float(quan)
            # df["PartNo"] = partno
            # df["Description"] = dc
            # df["Price"] = float(price)
            # df["Total"] = total
            #
            # df.to_csv(f"parts-{now}.csv")

        #for i in range(0, 5):
            #quanlist[i].text = ""
            #partlist[i].text = ""
            #dclist[i].text = ""
            #pricelist[i].text = ""
            # ammountlist[i].text = ""
            
# Updates the total price at the bottom of the page by multiplying each quantity by the price
    def update(self):
        try:
            q1 = self.ids.quan1.text
            p1 = self.ids.price1.text
            q11 = float(q1)
            p12 = float(p1)
            t1 = p12 * q11
        except:
            t1 = 0
        try:
            q2 = self.ids.quan2.text
            p2 = self.ids.price2.text
            q22 = float(q2)
            p22 = float(p2)
            t2 = p22 * q22
        except:
            t2 = 0
        try:
            q3 = self.ids.quan3.text
            p3 = self.ids.price3.text
            q31 = float(q3)
            p32 = float(p3)
            t3 = p32 * q31
        except:
            t3 = 0
        try:
            q4 = self.ids.quan4.text
            p4 = self.ids.price4.text
            q41 = float(q4)
            p42 = float(p4)
            t4 = p42 * q41
        except:
            t4 = 0
        try:
            q5 = self.ids.quan5.text
            p5 = self.ids.price5.text
            q51 = float(q5)
            p52 = float(p5)
            t5 = p52 * q51
        except:
            t5 = 0
        try:
            q6 = self.ids.quan6.text
            p6 = self.ids.price6.text
            q61 = float(q6)
            p62 = float(p6)
            t6 = p62 * q61
        except:
            t6 = 0
        try:
            q7 = self.ids.quan7.text
            p7 = self.ids.price7.text
            q71 = float(q7)
            p72 = float(p7)
            t7 = p72 * q71
        except:
            t7 = 0
        try:
            q8 = self.ids.quan8.text
            p8 = self.ids.price8.text
            q81 = float(q8)
            p82 = float(p8)
            t8 = p82 * q81
        except:
            t8 = 0
        try:
            q9 = self.ids.quan9.text
            p9 = self.ids.price9.text
            q91 = float(q9)
            p92 = float(p9)
            t9 = p92 * q91
        except:
            t9 = 0
            
        try:
            q10 = self.ids.quan10.text
            p10 = self.ids.price10.text
            q101 = float(q10)
            p102 = float(p10)
            t10 = p102 * q101
        except:
            t10 = 0
            self.ids.parttotal.text = ""
            
        try:
            tot = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10
            self.ids.parttotal.text = f"${tot}"
        except:
            self.ids.parttotal.text = "error"


class ThirdWindow(Screen):
# extra code
    # def Submitmore(self):
    #     startlist = [self.ids.Start1, self.ids.Start2, self.ids.Start3, self.ids.Start4,
    #                  self.ids.Start5]
    #     techlist = [self.ids.Tech1, self.ids.Tech2, self.ids.Tech3, self.ids.Tech4,
    #                  self.ids.Tech5]
    #     datelist = [self.ids.Date1, self.ids.Date2, self.ids.Date3, self.ids.Date4,
    #                 self.ids.Date5]
    #     stoplist = [self.ids.Stop1, self.ids.Stop2, self.ids.Stop3, self.ids.Stop4,
    #                 self.ids.Stop5]
    #     startam1list = [self.ids.StartAM1.active, self.ids.StartAM2.active, self.ids.StartAM3.active,
    #                     self.ids.StartAM4.active, self.ids.StartAM5.active]
    #     stopam1list = [self.ids.StopAM1.active, self.ids.StopAM2.active, self.ids.StopAM3.active,
    #                    self.ids.StopAM4.active, self.ids.StopAM5.active]
    #     # hrslist = [self.ids.Hrs1, self.ids.Hrs2, self.ids.Hrs3, self.ids.Hrs4, self.ids.Hrs5]
    #     # othrslist = [self.ids.OThrs1, self.ids.OThrs2, self.ids.OThrs3, self.ids.OThrs4, self.ids.OThrs5]
    #
    #     date = datetime.now()
    #     now = date.strftime("%m-%d")
    #     details = ["Date", "Tech", "Start", "StartAM?", "Stop", "StopAM?", "HRS", "OT HRS"]
    #     rows = []
    #     for i in range(0,5):
    #         rowlist = []
    #         rowlist.append(datelist[i].text)
    #         rowlist.append(techlist[i].text)
    #         rowlist.append(startlist[i].text)
    #         if startam1list[i] == True:
    #             rowlist.append("AM")
    #         else:
    #             rowlist.append("PM")
    #         rowlist.append(stoplist[i].text)
    #         if stopam1list[i] == True:
    #             rowlist.append("AM")
    #         else:
    #             rowlist.append("PM")
    #         rowlist.append(hrslist[i].text)
    #         rowlist.append(othrslist[i].text)
    #         rows.append(rowlist)
    #
    #     try:
    #
    #
    #         with open(f"labor-{now}.csv", "a") as f:
    #             writer = csv.writer(f)
    #
    #             # write the header
    #             writer.writerow(details)
    #
    #             # write multiple rows
    #             writer.writerows(rows)
    #         for i in range(0,5):
    #             datelist[i].text = ""
    #             techlist[i].text = ""
    #             startlist[i].text = ""
    #             stoplist[i].text = ""
    #
    #
    #
    #
    #     except:
    #         os.mkdir(f"{now}.csv")
    #         with open(f"{now}.csv", "a") as f:
    #             writer = csv.writer(f)
    #
    #             # write the header
    #             writer.writerow(details)
    #
    #             # write multiple rows
    #             writer.writerows(rows)
    #         for i in range(0,5):
    #             datelist[i].text = ""
    #             techlist[i].text = ""
    #             startlist[i].text = ""
    #             stoplist[i].text = ""
    
    
# deletes the most recent entry saved to labor csv other wise sets labels to none   
    def delete(self):
        now = datetime.now()
        now = now.strftime("%m-%d")
        try:
            data = pd.read_csv(f"labor-{now}.csv")
            df = pd.DataFrame()
            df["Date"] = data["Date"]
            df["Tech"] = data["Tech"]
            df["Start"] = data["Start"]
            df["Stop"] = data["Stop"]
            df["StopAM?"] = data["StopAM?"]
            df["StartAM?"] = data["StartAM?"]
            df["HRS"] = data["HRS"]
            df["OT HRS"] = data["OT HRS"]

            print(df)
            print("run")
            data1 = df.drop(index=df.index[-1])
            print(data1)
            data1.to_csv(f"labor-{now}.csv")
        except:
            self.ids.display1.text = "ERROR: NO DATA TO DELETE"

# Displays entries to Screen to error Correct

# TODO: add more rows of entries (idea.. add .iloc[-2],.iloc[-3], etc           
    def display(self):
        now = datetime.now()
        now =  now.strftime("%m-%d")
        try:
            data = pd.read_csv(f"labor-{now}.csv")
            length= len(data)
            try:
                date = data["Date"].iloc[-1]
                self.ids.display1.text = f"Date:{date}"
                NumofTechs = data["Tech"].iloc[-1]
                start = data["Start"].iloc[-1]
                stop = data["Stop"].iloc[-1]
                stopam = data["StopAM?"].iloc[-1]
                startam = data["StartAM?"].iloc[-1]
                hrs = data["HRS"].iloc[-1]
                othrs = data["OT HRS"].iloc[-1]
            except:
                self.ids.display1.text = "ERROR 1"
            self.ids.display0.text = f"Date:{date}"
            self.ids.display1.text = f"Techs:{NumofTechs}"
            self.ids.display2.text = f"Start:{start}{startam}"
            self.ids.display3.text = f"Stop:{stop}{stopam}"
            self.ids.display4.text = f"Hrs:{hrs} OT:{othrs}"
            cost = float(NumofTechs) * ((float(hrs)*165) + (float(othrs)*245))
            self.ids.display6.text = f"${cost}"
            try:
                current = self.ids.display5.text
                current1 = current.replace("$", " ")
                new = cost + float(current1)
                self.ids.display5.text = f"${new}"
            except:
                self.ids.display5.text  = f"${cost}"
        except:
            self.ids.display1.text = "NONE"
            self.ids.display2.text = "NONE"
            self.ids.display3.text = "NONE"
            self.ids.display4.text = "NONE"
            self.ids.display5.text = "NONE"
            pass
# sets start and stop values to selected value on dropdown        
    def spinner_clicked(self, value):
        now = datetime.now()
        now = now.strftime("%m-%d")
        if value == "1":
            self.ids.Start1.text = "1"
        if value == "2":
            self.ids.Start1.text = "2"
        if value == "3":
            self.ids.Start1.text = "3"
        if value == "4":
            self.ids.Start1.text = "4"
        if value == "5":
            self.ids.Start1.text = "5"
        if value == "6":
            self.ids.Start1.text = "6"
        if value == "7":
            self.ids.Start1.text = "7"
        if value == "8":
            self.ids.Start1.text = "8"
        if value == "9":
            self.ids.Start1.text = "9"
        if value == "10":
            self.ids.Start1.text = "10"
        if value == "11":
            self.ids.Start1.text = "11"
        if value == "12":
            self.ids.Start1.text = "12"
        if value == "1":
            self.ids.Stop1.text = "1"
        if value == "2":
            self.ids.Stop1.text = "2"
        if value == "3":
            self.ids.Stop1.text = "3"
        if value == "4":
            self.ids.Stop1.text = "4"
        if value == "5":
            self.ids.Stop.text = "5"
        if value == "6":
            self.ids.Stop1.text = "6"
        if value == "7":
            self.ids.Stop1.text = "7"
        if value == "8":
            self.ids.Stop1.text = "8"
        if value == "9":
            self.ids.Stop1.text = "9"
        if value == "10":
            self.ids.Stop1.text = "10"
        if value == "11":
            self.ids.Stop1.text = "11"
        if value == "12":
            self.ids.Stop1.text = "12"
        
            
            
            
# on saves all info           
    def Submitmore(self):
        startlist = self.ids.Start1.text
        stoplist = self.ids.Stop1.text
        startam1list = self.ids.StartAM1.text
        stopam1list = self.ids.StopAM1.text
        # hrslist = [self.ids.Hrs1, self.ids.Hrs2, self.ids.Hrs3, self.ids.Hrs4, self.ids.Hrs5]
        # othrslist = [self.ids.OThrs1, self.ids.OThrs2, self.ids.OThrs3, self.ids.OThrs4, self.ids.OThrs5]
        datelist = self.ids.Date1.text
        techlist = self.ids.Tech1.text
        rowlist = []
        now = datetime.now()
        now = now.strftime("%m-%d")

        # trys to read csv if no data frame exists same procedure occurs except it creates a data frame rather than append
        try:
            df = pd.read_csv(f"labor-{now}.csv")

            row = []
            start = startlist
            stop = stoplist
            row.append(datelist)
            row.append(techlist)
            row.append(startlist)
            row.append(startam1list)

            row.append(stoplist)
            row.append(stopam1list)
# if empty start or stop append 0
            if start == '':

                row.append("0")
                row.append("0")

            elif stop == '':

                row.append("0")
                row.append("0")

            else:

                # converts start/stop to int
                start = int(start)
                stop = int(stop)

                final = 0
# if start is in the am do this
                if startam1list == "AM":
# if stop is in the pm do this
                    if stopam1list == "PM":
                        count = 0
# while start is less than 12 add to a subsitute value count and add start til its = 12
                        while start < 12:
                            start += 1
                            count += 1
# if stop isnt at noon the final value is = 0+ however many hous start was prior to noon + stop time
                        if stop != 12:
                            final = final + count + stop
# if stop is at noon the final value = the number of hours start is prior to noon
                        else:
                            final = count
# if the final value is greater than 8 append the row with 8 for normal hours then subtract 8 and append the remainder as ot hours
                        if final > 8:

                            row.append("8")
                            final -= 8
                            row.append(f"{final}")
# if the value is not greater than 8. append the final value as hours and 0 as ot hours

                        else:
                            row.append(f"{final}")
                            row.append("0")
# if stop is in AM final value is stop time - start time 
                    else:
                        final = stop - start
# append the final value as hours and 0 as ot hours
                        row.append(f"{final}")
                        row.append("0")

# if start is in pm
                else:
# special case if start is at noon
                    if start == 12:
# if the stop time is after 8. append 8 to hours then subtract 8 to get OT time
                        if stop > 8:
                            row.append("8")
                            stop -= 8
                            row.append(f"{stop}")
# if stop is prior to 9 append stop hour to hours and Ot hours as 0
                        else:
                            row.append(f"{stop}")
                            row.append("0")
# if start is in the afternoon but not noon
                    else:
# stop time - start time gives total time
                        final = stop - start
# if the final value is greater than 8 append the row with 8 for normal hours then subtract 8 and append the remainder as ot hours 
                        if final > 8:
                            row.append("8")
                            final -= 8
                            row.append(f"{final}")
# if the value is not greater than 8. append the final value as hours and 0 as ot hours
                        else:
                            row.append(f"{final}")
                            row.append("0")


            rowlist.append(row)
            now = datetime.now()
            now = now.strftime("%m-%d")
            details = ["Date", "Tech", "Start", "StartAM?", "Stop", "StopAM?", "HRS", "OT HRS"]
            # attempts to save labor values then reset
            # if exception occurs trys alternative method
# trys to append to data frame and grab fresh start stop to prevent errors for the sake of redundacy
            try:

                startlist1 = self.ids.Start1.text
                stoplist1 = self.ids.Stop1.text


                df = df.append(pd.DataFrame(rowlist, columns=details))
                df.to_csv(f"labor-{now}.csv")
                self.ids.Date1.text = ""
                self.ids.Tech1.text = ""
                self.ids.Start1.text = ""
                self.ids.Stop1.text = ""
                self.ids.StartAM1.text = "AM/PM?"
                self.ids.StopAM1.text = "AM/PM?"



# if exception then forgets fresh values and runs
            except:

                df = df.append(pd.DataFrame(rowlist, columns=details))

                df.to_csv(f"labor-{now}.csv")
                self.ids.Date1.text = ""
                self.ids.Tech1.text = ""
                self.ids.Start1.text = ""
                self.ids.Stop1.text = ""
                self.ids.StartAM1.text = "AM/PM?"
                self.ids.StopAM1.text = "AM/PM?"

# if no csv exists runs through same logical process but creates csv in the end
        except:


            row = []
            start = startlist
            stop = stoplist
            row.append(datelist)
            row.append(techlist)
            row.append(startlist)
            if startam1list == "AM":
                row.append("AM")
            else:
                row.append("PM")
            row.append(stoplist)
            if stopam1list == "AM":
                row.append("AM")
            else:
                row.append("PM")

            if start == '':
                pass

            elif stop == '':
                pass

            else:

                    # converts start/stop to int
                start = int(start)
                stop = int(stop)

                final = 0

                if startam1list == "AM":

                    if stopam1list == "PM":
                        count = 0
                        while start < 12:
                            start += 1
                            count += 1
                        if stop != 12:
                            final = final + count + stop
                        else:
                            final = count

                        if final > 8:

                            row.append("8")
                            final -= 8
                            row.append(f"{final}")


                        else:
                            row.append(f"{final}")
                            row.append("0")

                    else:
                        final = stop - start

                        row.append(f"{final}")
                        row.append("0")


                else:
                    if start == 12:
                        if stop > 8:
                            row.append("8")
                            stop -= 8
                            row.append(f"{stop}")

                        else:
                            row.append(f"{stop}")
                            row.append("0")

                    else:
                        final = stop - start
                        if final > 8:
                            row.append("8")
                            final -= 8
                            row.append(f"{final}")

                        else:
                            row.append(f"{final}")
                            row.append("0")


                rowlist.append(row)
            now = datetime.now()
            now = now.strftime("%m-%d")
            details = ["Date", "Tech", "Start", "StartAM?", "Stop", "StopAM?", "HRS", "OT HRS"]
            # attempts to save labor values then reset
            # if exception occurs trys alternative method

            try:

                startlist1 = self.ids.Start1.text
                stoplist1 = self.ids.Stop1.text

                df = pd.DataFrame(rowlist, columns=details)

                df.to_csv(f"labor-{now}.csv")

                self.ids.Date1.text = ""
                self.ids.Tech1.text = ""
                self.ids.Start1.text = ""
                self.ids.Stop1.text = ""
                self.ids.StartAM1.text = "AM/PM?"
                self.ids.StopAM1.text = "AM/PM?"




            except:

                df = pd.DataFrame(rowlist, columns=details)

                df.to_csv(f"labor-{now}.csv")

                self.ids.Date1.text = ""
                self.ids.Tech1.text = ""
                self.ids.Start1.text = ""
                self.ids.Stop1.text = ""
                self.ids.StartAM1.text = "AM/PM?"
                self.ids.StopAM1.text = "AM/PM?"

# testing function can delete if neccessary
    checks = []
    def checkbox_click(self, instance, value, tech):
        if value == True:
            ThirdWindow.checks.append(tech)
        else:
            ThirdWindow.checks.remove(tech)
#       if len(checks) == 18:
#           self.ids.ee1.text = "31 - Shockme Shockti"
#           self.ids.ee2.text = "22 - Hasalalalalala"
#           self.ids.ee3.text = "32 - MADUDE"
#       else:
#           self.ids.ee1.text = "31 - Shakthi P"
#           self.ids.ee2.text = "22 - Hasala S"
#           self.ids.ee3.text = "32 - Madu T"

# custom drop down class for more personalized experience long term goal
class CustomDropDown(DropDown):
    pass


class FourthWindow(Screen):
    dropdown = ObjectProperty(None)
# spinner function
    def spinner_clicked(self, value):
        now = datetime.now()
        now = now.strftime("%m-%d")
        # if zone 1-8 is clicked sets value =  to respectie zone cost, also disables irrelevant fields
        if value == "Zone 1":
            self.ids.Zonecost.text = "234"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 2":
            self.ids.Zonecost.text = "342"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 3":
            self.ids.Zonecost.text = "498"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 4":
            self.ids.Zonecost.text = "825"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
        if value == "Zone 5":
            self.ids.Zonecost.text = "1120"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 6":
            self.ids.Zonecost.text = "1293"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 7":
            self.ids.Zonecost.text = "1470"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
        if value == "Zone 8":
            self.ids.Zonecost.text = "1668"
            self.ids.hour1.disabled = True
            self.ids.hour2.disabled = True
            self.ids.travel1.text = "0.0"
            self.ids.travel2.text = "0.0"
            self.ids.airtravelquery.text = "0"
            self.ids.airtravelquery.disabled = True
            self.ids.airvalue.text = "0.0"
# when pressed enables extra fields and sets zonecost to 0
        if value == "No Zone Fee":
            self.ids.Zonecost.text = "0"
            self.ids.hour1.disabled = False
            self.ids.hour2.disabled = False
            self.ids.airtravelquery.disabled = False
            
            
        


# TODO: calulates travel cost on different page(maybe uneccessary)
    def travel_clicked(self, value):
        pass

# calcutes all values
    def calculate(self):
        now = datetime.now()
        now = now.strftime("%m-%d")
        try:
            labordf = pd.read_csv(f"labor-{now}.csv")
            partsdf = pd.read_csv(f"Parts-{now}.csv")

            parts = partsdf["Amount"]

            hrs = labordf["HRS"]
            ot = labordf["OT HRS"]
            techs = labordf["Tech"]


            hrs = hrs.dropna()

            ot = ot.dropna()
            
            parts = parts.dropna()
            sumparts = parts.sum()

            sumhrs = hrs.sum()
            sumot = ot.sum()

            #customval = self.ids.customfield1.text

            #customval = customval.replace("$", "")

            #self.ids.customout1.text = customval

            p2pnorm = self.ids.hour1.text
            p2pot = self.ids.hour2.text
            val = self.ids.airtravelquery.text
            
            val = float(val)
            val = val*800
            self.ids.airvalue.text = f"{val}"
            
            val1 = self.ids.tq1.text
            val2 = self.ids.dq1.text
            
            val1 = float(val1)
            val2 = float(val2)
            
            val1  = val1*val2*95
            self.ids.perdiemval.text = f"{val1}"
            
            val3 = self.ids.tq2.text
            val4 = self.ids.dq2.text
            
            val3 = float(val3)
            val4 = float(val4)
            
            val6  = val3*val4*200
            self.ids.Hotel.text = f"{val6}"
            
            val5 = self.ids.dq3.text
            val5 = float(val5)
            val5 = val5*75
            self.ids.car.text =f"{val5}"

            if p2pnorm == "":
                p2pnorm = 0
            if p2pot == "":
                p2pot = 0

            try:
                p2pnorm = float(p2pnorm)
                p2pot = float(p2pot)
                print(p2pot)
                out1 = p2pnorm*60
                out2 = p2pot*90
                print(out1, out2)
                self.ids.travel1.text = f"{out1}"
                self.ids.travel2.text = f"{out2}"

            except:
                print("Error")


            self.ids.PartsTotal.text = f"{sumparts}"
# grabs the cost value from the labor
            cost = self.manager.get_screen("Labor").ids.display5.text
            cost = cost.replace("$", " ")
            cost = float(cost)
            self.ids.LaborCost.text = f"{cost}"

            

            zone = self.ids.Zonecost.text

            if zone == "":
                zone = 0

            tot = out1+out2+cost+float(sumparts)+float(zone)
            tot = tot+float(val)+float(val1)+float(val6)+float(val5)
            self.ids.Total.text = f"{tot}"
            
            df = pd.DataFrame([{'Air Travel': val},
                           {'Zone': zone},
                           {'Part Total': sumparts},
                           {'Hotel': val6},
                           {'P2P Norm': out1},
                           {'P2P OT': out2},
                           {"Labor": cost},
                           {"Rental Car": val5},
                           {'Per deim': val1}])
            df.to_csv("Cost-{now}.csv")
            


        except:

            print("error detect! Please check inputs and files"
                  "if no problem is apparent report bug to BRIAN FIGG")


class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(0.2,0.2,0.2)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        #print(touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        # self.export_to_png("roy.png")
        self.export_to_png("kivy-logo-black-64.png")
        print("RELEASED!", touch)

    def cleaner(self):
    
        print("cleaner: ", self)
        
        self.canvas.clear()
    def save(self):
        now = datetime.now()
        now = now.strftime("%m-%d")
        filename = f"sig.png"   
        self.export_to_png(filename)     
   
    	

class FifthWindow(Screen):

    draw = ObjectProperty()


    
      
        

    def random_number(self):
        pass

    def clean(self):
        print("clean: ", self)
        self.draw.cleaner()


class SixthWindow(Screen):
	
        def pdfcreate(self):
            now = datetime.now()
            time = now.strftime("%m-%d-%y")
            now = now.strftime("%m-%d")
            self.ids.error.text = "time stamp collected"
            
            pdf = PDF()
            self.ids.error.text = "PDF instance created"
            
            
            pdf.add_page()
            self.ids.error.text = "Created PDF page"
            
            pdf.cell(0)
            pdf.image("logo.png", x=0, y=0, w=60, h=25)
            
            self.ids.error.text = "Logo Added"
            
            pdf.cell(-200, align='left')
            try:
                pdf.chapter_body(f"{now}-service-customer.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading customer"

            try:
                pdf.chapter_body(f"{now}-service-date.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading date"
            try:
                pdf.chapter_body(f"{now}-service-address.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading address"

            try:
                pdf.chapter_body(f"{now}-service-email.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading email"
            try:
                pdf.chapter_body(f"{now}-service-terms.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading terms"

            try:
                pdf.chapter_body(f"{now}-service-PO.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading PO"
            try:
                pdf.chapter_body(f"{now}-service-contact.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading customer"
            try:
                pdf.chapter_body(f"{now}-service-desc.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading desc"
            try:
               
                pdf.chapter_body(f"{now}-service-service.txt")
                pdf.cell(-200)
            except:
                self.ids.error.text = "error reading service"
            self.ids.error.text = "Wrote Customer info"
            
            
            pdf.cell(-200)
            labordf = pd.read_csv(f"labor-{now}.csv")
           
            partsdf = pd.read_csv(f"Parts-{now}.csv")
            self.ids.error.text = "good check 6"
            q = partsdf["Quantity"]
            #pno = partsdf["PartNO"]
            d = partsdf["Description"]
            p = partsdf["Price"]
            a = partsdf["Amount"]
            pdf.add_page()
            pdf.cell(180, 10, "Parts Info", 0, 2, 'C')
            pdf.cell(90, 10, " ", 0, 2, 'C')
            self.ids.error.text = "good check 7"
            pdf.cell(30, 10, 'Quantity', 1, 0, 'C')
            #pdf.cell(40, 10, 'PartNo.', 1, 0, 'C')
            pdf.cell(60, 10, 'Desc', 1, 0, 'C')
            pdf.cell(30, 10, 'Price', 1, 0, 'C')
            pdf.cell(40, 10, 'Amount', 1, 2, 'C')
            for i in range(0, len(q)):
               pdf.cell(-120)
               pdf.cell(30, 10, '%s' % (q.iloc[i]), 1, 0, 'C')
               #pdf.cell(40, 10, '%s' % (pno.iloc[i]), 1, 0, 'C')
               pdf.cell(60, 10, '%s' % (d.iloc[i]), 1, 0, 'C')
               pdf.cell(30, 10, '%s' % (p.iloc[i]), 1, 0, 'C')
               pdf.cell(40, 10, '%s' % (a.iloc[i]), 1, 2, 'C')
            self.ids.error.text = "Part Info Loaded"
            pdf.cell(-65)
            # pdf.set_font('arial', 'I', 12)
            pdf.cell(75, 10, "Labor Info", 0, 2, 'C')
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.cell(-50)
            pdf.cell(30, 10, 'Date', 1, 0, 'C')
            pdf.cell(30, 10, 'Tech', 1, 0, 'C')
            pdf.cell(30, 10, 'Start Time', 1, 0, 'C')
            pdf.cell(30, 10, 'Stop Time', 1, 0, 'C')
            pdf.cell(30, 10, 'Normal Hours', 1, 0, 'C')
            pdf.cell(30, 10, 'OT Hours', 1, 2, 'C')
            self.ids.error.text = "Labor info created, Placing starting.."
            #pdf.cell(-90)
            pdf.set_font('arial', '', 12)
            labordf = labordf.dropna()
            dt = labordf["Date"]
            t = labordf["Tech"]
            strt = labordf["Start"]
            strta = labordf["StartAM?"]
            strt = strt.dropna()
            stp = labordf["Stop"]
            stpa = labordf["StopAM?"]
            hrs = labordf["HRS"]
            othrs = labordf["OT HRS"]
            fulllist1 = []
            fulllist2 = []
            for x in range(0, len(strt)):
                val = strta.iloc[x]
                print(val)
                val1 = strt.iloc[x]
                print(val1)
                if val1 == None:
                    pass
                else:
                    val2 = f"{val1} {val}"
                    print(val2)
                    fulllist1.append(val2)

            df = pd.DataFrame(fulllist1)
            self.ids.error.text = "start time compiled"

 
            for x in range(0, len(stp)):
                val = stpa.iloc[x]
                val1 = stp.iloc[x]
                if val1 == "":
                    pass
                else:
                    val2 = f"{val1} {val}"
                    fulllist2.append(val2)
                    
            df1 = pd.DataFrame(fulllist2)
            
            self.ids.error.text = "stop time compiled"
            pdf.image("logo.png", x=0, y=0, w=60, h=25)
            for i in range(0, len(t)):
                pdf.cell(-150)
                pdf.cell(30, 10, '%s' % (dt.iloc[i]), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (t.iloc[i]), 1, 0, 'C')
                s = df.iloc[i]
                s = s.to_string()
                pdf.cell(30, 10, '%s' % (s), 1, 0, 'C')
                s = df1.iloc[i]
                s = s.to_string()
                pdf.cell(30, 10, '%s' % (s), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (hrs.iloc[i]), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (othrs.iloc[i]), 1, 2, 'C')
                
                
            pdf.cell(-105)
            pdf.set_font('arial', 'I', 12)
            pdf.cell(90, 10, "Cost Overview", 0, 2, 'C')
            pdf.cell(90, 10, " ", 0, 2, 'C')
            costdf = pd.read_csv("Cost-{now}.csv")
            
            air = costdf["Air Travel"]
            zone = costdf["Zone"]
            Parts = costdf["Part Total"]
            hotel = costdf["Hotel"]
            norm = costdf["P2P Norm"]
            ot = costdf["P2P OT"]
            labor = costdf["Labor"]
            car = costdf["Rental Car"]
            per = costdf["Per deim"]
            pdf.cell(5)
            i=0
            pdf.cell(40, 10, 'Air Travel:', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (air.iloc[i]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Zone Cost', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (zone.iloc[i+1]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Part Cost', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (Parts.iloc[i+2]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Labor Cost', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (labor.iloc[i+6]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'P2P Normal Hours', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (norm.iloc[i+4]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'P2P OT Hours', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (ot.iloc[i+5]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Hotel', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (hotel.iloc[i+3]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Car Cost', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (car.iloc[i+7]), 1, 2, 'C')
            pdf.cell(-40)
            pdf.cell(40, 10, 'Per Diem', 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (per.iloc[i+8]), 1, 2, 'C')
            pdf.cell(-40)
            
            
                

            
            
            pdf.cell(-1)
            pdf.set_font('arial', 'I', 12)
            pdf.cell(75, 10, "Signature: ", 0, 2, 'C')
            self.ids.error.text = "PDF Contents Filled, Placing Signature"
            
            filename = f"sig.png"
            pdf.image(filename, w=100, h=25)
            self.ids.error.text = "Signature Done"
# 
# Environment = autoclass('android.os.Environment')
# if Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED:
#     # root = Environment.getExternalStorageDirectory().getAbsolutePath()
#     root = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOCUMENTS).getAbsolutePath() + '/'
# else:
#     # root = context.getExternalFilesDir().getAbsolutePath()
#     root = os.getcwd() + '/tmp/'
# 
            self.ids.error.text = f"{root}"
# # pdf.chapter_body(f"{now}-service-service.txt")
# 
# 
            pdf.output(f'{root}report5.pdf', 'F')
    	
    	
    	
    	
    	



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("layout.kv")


class ACPAC(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ACPAC().run()
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

